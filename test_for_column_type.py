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
    #app_name not string
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": 123
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_unit_id():
    #unit_id not int: string
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": "55665201314"
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    #unit_id not int: float
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314.0
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_request():
    #request not int:string
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": "100"
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

    #request not int:float
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100.0
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == False

def test_revenue():
    #revenue not Number:string
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": "0.00365325"
        , "imp": 23}
    assert validate(data) == False

    #revenue is Number:int
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 123
        , "imp": 23}
    assert validate(data) == True

def test_imp():
    #imp not int:string
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": "23"}
    assert validate(data) == False

    #imp not int:float
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23.0}
    assert validate(data) == False







