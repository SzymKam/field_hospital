import pandas as pd
import plotly.express as px

from treatment.models.vital_sign_model import VitalSign

from ..models.treatment_model import Treatment


class TreatmentPlot:
    @staticmethod
    def __create_data_dict(treatment: Treatment) -> dict:
        all_signs = VitalSign.objects.filter(treatment=treatment)

        return {
            "Time": [sign.datetime for sign in all_signs],
            "BP SYS": [sign.bp_sys for sign in all_signs],
            "BP DIA": [sign.bp_dia for sign in all_signs],
            "HR": [sign.hr for sign in all_signs],
            "SaO2": [sign.sao2 for sign in all_signs],
        }

    @staticmethod
    def __reshape_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        return pd.melt(
            df,
            id_vars=["Time"],
            value_vars=["BP SYS", "BP DIA", "HR", "SaO2"],
            var_name="Parameters",
            value_name="Parameter value",
        )

    @staticmethod
    def __create_figure(df_long: pd.DataFrame) -> str:
        fig = px.line(df_long, x="Time", y="Parameter value", color="Parameters")
        fig.update_traces(mode="lines+markers+text")
        return fig.to_html(include_plotlyjs="cdn")

    @staticmethod
    def create_plot(treatment: Treatment) -> str:
        all_data = TreatmentPlot.__create_data_dict(treatment)
        df = pd.DataFrame(all_data)
        df_long = TreatmentPlot.__reshape_dataframe(df)
        plotly_html = TreatmentPlot.__create_figure(df_long)
        return plotly_html
