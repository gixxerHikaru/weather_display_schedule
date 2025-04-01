import os
import requests
import json
import prefectures_check, prefectures_convert

#https://www.weatherapi.com/
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def forcast(url):
    try:
            response = requests.get(url)
            response.raise_for_status()  # エラーレスポンスを例外として処理

            data = response.json()  # JSONデータをPythonの辞書に変換
            
            return data
    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
    except json.JSONDecodeError as e:
        print(f"JSONデータの解析に失敗しました: {e}")

def display(prefecture_jp, prefecture_en, data):
    print(prefecture_jp + "(" + prefecture_en + ")の一週間の天気予報")
    forecast_days = data['forecast']['forecastday']
    for day in forecast_days:
        date = day['date']
        max_temp = day['day']['maxtemp_c']
        min_temp = day['day']['mintemp_c']
        condition = day['day']['condition']['text']
        print(f"{date}: 最高気温{max_temp}℃, 最低気温{min_temp}℃, 天気: {condition}")

def display_day(prefecture_jp, prefecture_en, data, day):
    forecast_days = data['forecast']['forecastday']
    day = forecast_days[day]
    # for day in forecast_days:
    date = day['date']
    max_temp = day['day']['maxtemp_c']
    min_temp = day['day']['mintemp_c']
    daily_chance_of_rain = day['day']['daily_chance_of_rain']
    condition = day['day']['condition']['text']
    condition_code = day['day']['condition']['code']
    print(prefecture_jp + "(" + prefecture_en + ")の" + date + "の天気予報")
    print(f"{date}: 最高気温{max_temp}℃, 最低気温{min_temp}℃, 降水確率: {daily_chance_of_rain}, 天気: {condition}")
    return [max_temp, min_temp, daily_chance_of_rain, condition, condition_code]
def func(prefecture_jp, display_option):
    try:
        prefectures_check.func(prefecture_jp)
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
    else:
        prefecture_en = str(prefectures_convert.func(prefecture_jp))
        url = "http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=7&aqi=no&alerts=no".format(WEATHER_API_KEY, prefecture_en)

        data = forcast(url)
        if display_option:
            display(prefecture_jp, prefecture_en, data)
        return data
        
def func_day(prefecture_jp, day):
    try:
        prefectures_check.func(prefecture_jp)
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
    else:
        prefecture_en = str(prefectures_convert.func(prefecture_jp))
        url = "http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=7&aqi=no&alerts=no".format(WEATHER_API_KEY, prefecture_en)

        data = forcast(url)
        
        display_day(prefecture_jp, prefecture_en, data, day)

if __name__ == '__main__':
    prefecture_jp = input("都道府県を日本語で入力してください:")
    func(prefecture_jp, True)
    