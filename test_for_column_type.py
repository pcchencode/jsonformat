import pytest
from json_schema_validation import validate

def test_ad_network():
	#ad_network not string
    data = {"ad_network": 123
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_date():
    #date format YYYYMMDD
    data = {"ad_network": "FOO"
        , "date": "20190605"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    #date format YYYY-MM-DD HH:MM:SS
    data = {"ad_network": "FOO"
        , "date": "2019-06-05 00:00:00"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    #date format not string
    data = {"ad_network": "FOO"
        , "date": 20190605
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_app_name():
    #app_name not int
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
        , "unit_id": 55665201314.1
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False






