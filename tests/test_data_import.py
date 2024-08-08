import pytest
import pandas as pd
from pathlib import Path
from zeiss_iot.data.data_import import read_temp_data, process_datetime


def test_read_temp_data():
    """Test the read_temp_data function for output
    """
    df = read_temp_data()
    assert isinstance(df, pd.DataFrame), "The function output is not pandas DF"


def test_process_datetime():
    """Test creation of date, time, month, year columns
    """
    df = read_temp_data()
    df = process_datetime(df)
    assert "date" in df.columns, "date column is missing"
    assert "time" in df.columns, "time column is missing"
    assert "year" in df.columns, "year column is missing"
    assert "month" in df.columns, "month column is missing"


if __name__ == '__main__':
    pytest.main(['-v', '--capture=tee-sys'])
