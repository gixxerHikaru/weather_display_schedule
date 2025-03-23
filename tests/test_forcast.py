import os
import pytest
import requests
import json
import prefectures_check, prefectures_convert
from unittest.mock import patch, Mock
from forcast import func

# サンプルAPIキー
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def test_prefectures_check_valid():
    """正しい都道府県名が与えられた場合、エラーが発生しないこと"""
    prefectures_check.func("東京都")

def test_prefectures_check_invalid():
    """正しくない都道府県名が与えられた場合、ValueErrorが発生すること"""
    with pytest.raises(ValueError):
        prefectures_check.func("存在しない都道府県")

def test_prefectures_convert():
    """正しい都道府県名が与えられた場合、正しい英語名が返されること"""
    assert prefectures_convert.func("東京都") == "Tokyo"

@patch("requests.get")
def test_api_success(mock_get):
    """APIから正常にデータが取得できること"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "forecast": {
            "forecastday": [
                {
                    "date": "2023-10-27",
                    "day": {
                        "maxtemp_c": 20,
                        "mintemp_c": 10,
                        "condition": {"text": "晴れ"},
                    },
                }
            ]
        }
    }
    mock_get.return_value = mock_response

    prefecture_en = "Tokyo"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={prefecture_en}&days=7&aqi=no&alerts=no"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {
        "forecast": {
            "forecastday": [
                {
                    "date": "2023-10-27",
                    "day": {
                        "maxtemp_c": 20,
                        "mintemp_c": 10,
                        "condition": {"text": "晴れ"},
                    },
                }
            ]
        }
    }

@patch("requests.get")
def test_api_error(mock_get):
    """APIからエラーレスポンスが返された場合、エラーが適切に処理されること"""
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Bad Request")
    mock_get.return_value = mock_response

    prefecture_en = "Tokyo"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={prefecture_en}&days=7&aqi=no&alerts=no"
    with pytest.raises(requests.exceptions.HTTPError):
        requests.get(url).raise_for_status()

@patch("requests.get")
def test_json_decode_error(mock_get):
    """JSONデータが不正な形式の場合、エラーが適切に処理されること"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "doc", 0)
    mock_get.return_value = mock_response

    prefecture_en = "Tokyo"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={prefecture_en}&days=7&aqi=no&alerts=no"
    response = requests.get(url)
    with pytest.raises(json.JSONDecodeError):
        response.json()

@patch("requests.get")
def test_func_success(mock_get, capsys):
    """正しい都道府県名が与えられた場合、天気予報が表示されること"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "forecast": {
            "forecastday": [
                {
                    "date": "2023-10-27",
                    "day": {
                        "maxtemp_c": 20,
                        "mintemp_c": 10,
                        "condition": {"text": "晴れ"},
                    },
                }
            ]
        }
    }
    mock_get.return_value = mock_response

    func("東京都", True)
    captured = capsys.readouterr()
    assert "東京都(Tokyo)の一週間の天気予報" in captured.out
    assert "2023-10-27: 最高気温20℃, 最低気温10℃, 天気: 晴れ" in captured.out

@patch("builtins.input", return_value="存在しない都道府県")
def test_func_invalid_prefecture(mock_input, capsys):
    """正しくない都道府県名が与えられた場合、エラーメッセージが表示されること"""
    func("存在しない都道府県", True)
    captured = capsys.readouterr()
    assert "エラーが発生しました: 正しい都道府県名を入力してください。" in captured.out
    