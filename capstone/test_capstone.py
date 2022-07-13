import pytest
from capstone import Cli
import logging
from testfixtures import LogCapture
import os
import random
from tempfile import tempdir
import json
from pathlib import Path


def cli_mock(index):
    return Cli(index)


@pytest.mark.parametrize("index,expected",  [(["--file_count","0", "--data_schema","try.json"], True)])
def test_schema(index, expected):
    cli_object = cli_mock(index)
    cli_object.parse_analysis()
    response = cli_object.create_jsons()
    assert response == expected


@pytest.mark.parametrize("key,expression",  [("age",{'age': 'int:rand(1,9)'})])
def test_data_types(key, expression):
    cli_object = cli_mock(['--data_schema',f'{expression}'])
    value = cli_object.sintax_check(key, expression)
    assert type(value) is int


@pytest.mark.parametrize("index,expected",  [(["--file_count","2", "--data_schema","try.json"], 2)])
def test_saving_file(index, expected):
    cli_object = cli_mock(index)
    cli_object.parse_analysis()
    cli_object.create_jsons()
    len_files = len(os.listdir(r"JSON"))
    assert expected == len_files


@pytest.fixture
def temp_path(tmpdir):
    return Path(tmpdir)


def test_temporary_json(tmpdir, temp_path):
    p = tmpdir.mkdir("sub").join('temp_js.json')
    p.write("{\"date\": \"timestamp:\",\"name\": \"str:rand\","
            "\"type\": \"['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"}")
    cli_object = cli_mock(['--data_schema', f'{p}', "--file_count", "1"])
    cli_object.parse_analysis()
    cli_object.create_jsons()
    data_schema = cli_object.json_analysis(cli_object.data)
    assert type(data_schema) is dict


@pytest.mark.parametrize("index,expected",
                         [(["--file_count", "2", "--data_schema", "try.json", "--multiprocessing", "2"], 2)])
def test_saving_file(index, expected):
    cli_object = cli_mock(index)
    cli_object.parse_analysis()
    cli_object.create_jsons()
    len_files = len(os.listdir(r"JSON"))
    assert expected == len_files


def test_own_test(tmpdir, temp_path):
    p = tmpdir.mkdir("sub").join('temp_js.json')
    p.write("{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\","
            "\"age\": \"int:rand(1, 90)\"}")
    cli_object = cli_mock(['--data_schema', f'{p}', "--file_count", "1"])
    cli_object.parse_analysis()
    cli_object.create_jsons()
    data_schema = cli_object.json_analysis(cli_object.data)
    assert type(data_schema['age']) is int
    assert type(data_schema['name']) is str

# Different number of files than existed before


@pytest.mark.parametrize("index",  [["--file_count", f"{random.randint(1,9)}",
                                     "--data_schema", "try.json", "--clear_path", "True"]])
def test_saving_file(index):
    old_len_files = len(os.listdir(r"JSON"))
    cli_object = cli_mock(index)
    cli_object.parse_analysis()
    cli_object.create_jsons()
    len_files = len(os.listdir(r"JSON"))
    assert old_len_files != len_files
