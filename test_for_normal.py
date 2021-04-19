import pytest
from json_schema_validation import validate

def test_for_normal():
	#正常資料
    data = {"ad_network": "FOO"
        , "date": "2019-06-05"
        , "app_name": "LINETV"
        , "unit_id": 55665201314
        , "request": 100
        , "revenue": 0.00365325
        , "imp": 23}
    assert validate(data) == True