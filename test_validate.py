import os
import pytest
from json_schema_validation import validate

def test_for_normal():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == True

def test_for_null():
    data = {"ad_network": ""
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": ""
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": ""
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": None
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": ""
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": None
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": None
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": None}
    assert validate(data) == False

def test_for_col_type():
    data = {"ad_network": 123
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": 123
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": 123
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": "55665201314"
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": "100"
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "20190605"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": "0.00365325"
        , "imp": 23}
    assert validate(data) == False

    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": "23"}
    assert validate(data) == False


def test_for_col_miss():
    data = {"ad_network": "FOO"
        , "date": "20190605"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_for_col_redundant():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23
        , "redundant":"value"}
    assert validate(data) == False

