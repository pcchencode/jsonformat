### 套件安裝
```
$ pip install pytest
```

### 檔案說明
* `json_schema_validation.py`: 驗證主程式
* `test_for_{}.py`: 測試程式
	- `test_for_normal.py`: 測試正常資料格式
	- `test_for_null_value.py`: 測試資料含有空值
	- `test_for_column_type.py`: 測試欄位格式正確性
	- `test_for_column_miss.py`: 測試欄位缺漏
	- `test_for_column_redundant.py`: 測試多餘欄位

### 執行方法
```
$ git clone {this repo}
$ cd {this repo}
$ pytest #直接進行測試
```
```
$ pytest -v #列出詳細函式的測試結果
```

### 執行結果
* `test_for_col_redundant` will fail, 因為在主程式 `json_schema_validation.py` 沒有定義何謂多餘的欄位。