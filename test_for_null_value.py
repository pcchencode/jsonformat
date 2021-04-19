import pytest
from json_schema_validation import validate

def test_ad_network_null():
    data = {"ad_network": None
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False
    data = {"ad_network": ""
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_date_null():
    data = {"ad_network": "FOO"
        , "date": ""
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False
    data = {"ad_network": "FOO"
        , "date": None
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_app_name_null():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": None
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

def test_unit_id_null():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": None
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_request_null():
    data = {"ad_network": ""
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": None
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_revenue_null():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": None
        , "imp": 23}
    assert validate(data) == False

def test_imp_null():
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": None}
    assert validate(data) == False