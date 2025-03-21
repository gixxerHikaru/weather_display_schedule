import os
import requests
import json
import prefectures_check, prefectures_convert

#https://www.weatherapi.com/
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def func():
    try:
        prefecture_jp = input("都道府県を日本語で入力してください:")
        prefectures_check.func(prefecture_jp)
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
        func()
    else:
        prefecture_en = str(prefectures_convert.func(prefecture_jp))
        url = "http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=7&aqi=no&alerts=no".format(WEATHER_API_KEY, prefecture_en)

        try:
            response = requests.get(url)
            response.raise_for_status()  # エラーレスポンスを例外として処理

            data = response.json()  # JSONデータをPythonの辞書に変換
            
            # データの例: 検索場所の7日間の天気予報を表示
            print(prefecture_jp + "(" + prefecture_en + ")" + "の一週間の天気予報")
            forecast_days = data['forecast']['forecastday']
            for day in forecast_days:
                date = day['date']
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                condition = day['day']['condition']['text']
                print(f"{date}: 最高気温{max_temp}℃, 最低気温{min_temp}℃, 天気: {condition}")

        except requests.exceptions.RequestException as e:
            print(f"エラーが発生しました: {e}")
        except json.JSONDecodeError as e:
            print(f"JSONデータの解析に失敗しました: {e}")

if __name__ == '__main__':
    func()
