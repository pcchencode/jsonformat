import os
from datetime import datetime
import jsonschema

def validate(data):
    try:
        #檢查欄位存在性
        assert "ad_network" in data
        assert "date" in data
        assert "app_name" in data
        assert "unit_id" in data
        assert "request" in data
        assert "revenue" in data
        assert "imp" in data

        #檢查缺漏值
        assert data['ad_network'] is not None
        assert len(data['ad_network'])>1
        assert data['date'] is not None
        assert len(data['date'])>1
        assert data['app_name'] is not None
        assert len(data['app_name'])>1
        assert data['unit_id'] is not None
        assert data['request'] is not None
        assert data['revenue'] is not None
        assert data['imp'] is not None

        #檢查欄位格式
        assert type(data['ad_network']) is str
        assert datetime.strptime(data['date'], '%Y-%m-%d') #正確日期格式
        assert type(data['app_name']) is str
        assert type(data['unit_id']) is int
        assert type(data['request']) is int
        assert type(data['revenue']) in (int, float) #number
        assert type(data['imp']) is int
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == '__main__':
    data = {"ad_network": "FOO"
            , "date": "2019-06-05"
            , "app_name": "LINETV"
            , "unit_id": 55665201314
            , "request": 100
            , "revenue": 0.00365325
            , "imp": 23}

    result = validate(data)
    print(result)
    os._exit(0)
