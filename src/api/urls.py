from rest_framework.routers import SimpleRouter

from .views.event_view import EventViewSet
from .views.user_view import UserViewSet

router = SimpleRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"event", EventViewSet)


urlpatterns = [] + router.urls
