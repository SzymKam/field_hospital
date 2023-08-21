import pandas as pd
import plotly.express as px

from treatment.models.vital_sign_model import VitalSign


def create_plot():
    data_BP = VitalSign.objects.filter(name="BP")
    data_HR = VitalSign.objects.filter(name="HR")
    data_SpO2 = VitalSign.objects.filter(name="SpO2")

    all_data = {
        "Time": [BP.datetime for BP in data_BP],
        # 'BP_DIA_datetime': [BP.datetime for BP in data_BP],
        # 'HR_datetime': [HR.datetime for HR in data_HR],
        "SpO2_datetime": [SpO2.datetime for SpO2 in data_SpO2],
        "BP_SYS_value": [BP.value for BP in data_BP],
        # 'BP_DIA_value': [BP.extra_value for BP in data_BP],
        # 'HR_value': [HR.value for HR in data_HR],
        "Spo2_value": [SpO2.value for SpO2 in data_SpO2],
    }
    #
    # bp_data = [{'datetime': bp.datetime, 'value': bp.value} for bp in data_BP]
    # hr_data = [{'datetime': hr.datetime, 'value': hr.value} for hr in data_HR]
    # spo2_data = [{'datetime': spo2.datetime, 'value': spo2.value} for spo2 in data_SpO2]
    #
    # df_bp = pd.DataFrame(bp_data)
    # df_hr = pd.DataFrame(hr_data)
    # df_spo2 = pd.DataFrame(spo2_data)
    #
    # all_datetimes = sorted(set(df_bp['datetime']).union(df_hr['datetime']).union(df_spo2['datetime']))
    # alL_data = []
    #
    # for datetime_val in all_datetimes:
    #     row = {'Time': datetime_val}
    #
    #     bp_row = df_bp[df_bp['datetime'] == datetime_val]
    #     row['BP_SYS_value'] = bp_row['value'].values[0] if not bp_row.empty else None
    #
    #     hr_row = df_hr[df_hr['datetime'] == datetime_val]
    #     row['HR_value'] = hr_row['value'].values[0] if not hr_row.empty else None
    #
    #     spo2_row = df_spo2[df_spo2['datetime'] == datetime_val]
    #     row['spo2_value'] = spo2_row['value'].values[0] if not spo2_row.empty else None
    #     alL_data.append(row)
    #
    # final_df = pd.DataFrame(alL_data)
    #
    # data_frames = [df_bp, df_hr, df_spo2]
    #
    # melted_data = []
    #
    # for df, var_name in zip(data_frames, ['BP_SYS_value', 'HR_value', 'spo2_value']):
    #     melted_df = pd.melt(df, id_vars=['datetime'], value_vars=['value'], var_name=var_name, value_name="Value")
    #     melted_data.append(melted_df)
    #
    # melted_df = pd.concat(melted_data)
    # final_df = pd.merge(final_df, melted_df, left_on=['Time', var_name],
    #                     right_on=['datetime', var_name], how='left')
    #
    # print(final_df)

    all_data = {
        "Time": ["2023-08-01", "2023-08-04", "2023-08-05", "2023-08-07"],
        "BP_DIA_datetime": ["2023-08-01", "2023-08-02", "2023-08-04", "2023-08-06"],
        "HR_datetime": ["2023-08-01", "2023-08-05", "2023-08-07", "2023-08-09"],
        "SpO2_datetime": ["2023-08-01", "2023-08-05", "2023-08-09", "2023-08-11"],
        "BP_SYS_value": [1, 2, 3, 1],
        "BP_DIA_value": [3, 2, 1, 2],
        "HR_value": [1, 1, 1, 1],
        "Spo2_value": [3, None, 3, 3],
    }

    df = pd.DataFrame(all_data)

    df_long = pd.melt(
        df,
        id_vars=[
            "Time",
            # 'BP_DIA_datetime', 'HR_datetime',
            # 'SpO2_datetime'
        ],
        value_vars=[
            "BP_SYS_value",
            # 'BP_DIA_value', 'HR_value',
            "Spo2_value",
        ],
        var_name="Parameters",
        value_name="Parameter value",
    )

    fig = px.line(df_long, x="Time", y="Parameter value", color="Parameters", title="Vital signs plot")

    plotly_html = fig.to_html(include_plotlyjs="cdn")

    fig.show()
    return plotly_html
