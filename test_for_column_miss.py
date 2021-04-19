import pytest
from json_schema_validation import validate

def test_miss_ad_net_work():
    data = {
        "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_miss_app_name():
    data = {"ad_network": "FOO"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_miss_unit_id():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_miss_request():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_miss_revenue():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "imp": 23}
    assert validate(data) == False

def test_miss_imp():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325}
    assert validate(data) == False