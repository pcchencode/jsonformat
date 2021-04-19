import pytest
from json_schema_validation import validate

# 因為沒有定義是否有多的欄位，因此會跳錯
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
