from django.apps import AppConfig
from django.db.models.signals import post_migrate


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self) -> None:
        post_migrate.connect(self._create_initial_staff_admin_group, sender=self)

    def _create_initial_staff_admin_group(self, sender, **kwargs) -> None:
        from django.contrib.auth.models import Group, Permission

        permission_add_user = Permission.objects.get(codename="add_user")
        permission_change_user = Permission.objects.get(codename="change_user")
        permission_delete_user = Permission.objects.get(codename="delete_user")

        user_group, created = Group.objects.get_or_create(name="User admin group")
        if created:
            user_group.permissions.add(permission_add_user, permission_change_user, permission_delete_user)
            user_group.save()
