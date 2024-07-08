import json
import os
import sys
from unittest.mock import patch

import pandas as pd
import pytest

from backend.services.create_file import create_file

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def sample_json_data():
    return [{"key1": "value1", "key2": "value2"}]


@pytest.fixture
def sample_csv_data():
    return pd.DataFrame([{"key1": "value1", "key2": "value2"}])


def test_create_json_file(tmpdir, sample_json_data):
    file_name = "test.json"
    file_path = os.path.join(tmpdir, file_name)
    create_file(sample_json_data, file_path, "json")

    with open(file_path, "r") as file:
        data = json.load(file)
        assert data == sample_json_data


def test_create_csv_file(tmpdir, sample_csv_data):
    file_name = "test.csv"
    file_path = os.path.join(tmpdir, file_name)
    create_file(sample_csv_data.to_dict(orient="records"), file_path, "csv")

    df = pd.read_csv(file_path)
    assert df.equals(sample_csv_data)

