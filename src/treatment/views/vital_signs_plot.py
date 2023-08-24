import pandas as pd
import plotly.express as px

from treatment.models.vital_sign_model import VitalSign

from ..models.treatment_model import Treatment


def create_plot(treatment: Treatment) -> str:
    all_signs = VitalSign.objects.filter(treatment=treatment)

    all_data = {
        "Time": [sign.datetime for sign in all_signs],
        "BP SYS": [sign.bp_sys for sign in all_signs],
        "BP DIA": [sign.bp_dia for sign in all_signs],
        "HR": [sign.hr for sign in all_signs],
        "SaO2": [sign.sao2 for sign in all_signs],
    }

    df = pd.DataFrame(all_data)

    df_long = pd.melt(
        df,
        id_vars=["Time"],
        value_vars=["BP SYS", "BP DIA", "HR", "SaO2"],
        var_name="Parameters",
        value_name="Parameter value",
    )

    fig = px.line(df_long, x="Time", y="Parameter value", color="Parameters")
    fig.update_traces(mode="lines+markers+text")

    plotly_html = fig.to_html(include_plotlyjs="cdn")

    return plotly_html
