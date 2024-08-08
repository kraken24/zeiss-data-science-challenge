from pathlib import Path
import pandas as pd
from zeiss_iot.util import DATA_PATH


def read_temp_data(csv_filepath: str | Path = DATA_PATH) -> pd.DataFrame:
    """Read temperature data from csv file.""

    Args:
        csv_filepath (str | Path, optional): The csv file path of the data.
            Defaults to DATA_PATH.

    Returns:
        pd.DataFrame: The df with the temp data.
    """
    temp_data_df = pd.read_csv(csv_filepath)

    return temp_data_df


def process_datetime(
    temp_data_df: pd.DataFrame,
    datetime_col: str = "datetime"
) -> pd.DataFrame:
    """
    Process the datetime column in the provided DataFrame. This step is only
    necessary during the initial data exploration. Similar functions can be
    written for further data processing as well.

    Args:
        temp_data_df (pd.DataFrame): The input DataFrame.
        datetime_col (str, optional): The name of the datetime column.
            Defaults to "datetime".

    Returns:
        pd.DataFrame: The processed DataFrame with separated date, time,
            month and year columns.
    """
    if datetime_col not in temp_data_df.columns:
        raise ValueError(f"The dataframe does not contain {datetime_col} column.")

    temp_data_df[datetime_col] = pd.to_datetime(temp_data_df[datetime_col])
    temp_data_df["date"] = temp_data_df[datetime_col].apply(lambda x: x.date())
    temp_data_df["time"] = temp_data_df[datetime_col].apply(lambda x: x.time())
    temp_data_df["month"] = temp_data_df[datetime_col].dt.to_period("M")
    temp_data_df["year"] = temp_data_df[datetime_col].dt.to_period("Y")

    temp_data_df.sort_values(by=["date", "time"], inplace=True)

    return temp_data_df


if __name__ == "__main__":
    print("Reading data...")
    df = read_temp_data()
    df = process_datetime(df)
    print(df.head())

