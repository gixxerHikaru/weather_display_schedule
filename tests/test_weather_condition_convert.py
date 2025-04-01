from weather_condition_convert import func
import pytest
# テスト使い方
# 全通し pytest test_xxx.py
# クラス実行 pytest test_xxx.py::ClassName

class TestNormal:
    def test_func_valid_code1(self):
        assert func(1000) == "晴れ"
    def test_func_valid_code2(self):
        assert func(1006) == "曇り"
    def test_func_valid_code3(self):
        assert func(1282) == "雷を伴う中程度または大雪"

class TestFalse:
    def test_func_invalid_code4(self):
        assert func(9999) == False
    def test_func_invalid_code5(self):        
        assert func("invalid") == False

class TestEdge:
    def test_func_edge_cases1(self):
        assert func("1000") == False  # 文字列のコードも受け付けるか確認
    def test_func_edge_cases2(self):
        assert func(0) == False       # 存在しないコード0の確認
