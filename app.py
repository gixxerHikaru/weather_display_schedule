import streamlit as st
import datetime
import forcast, prefecture_box
import pandas as pd
import numpy as np

today = str(datetime.datetime.now())[0:10]
today1 = str(datetime.datetime.now() + datetime.timedelta(days=1))[0:10]
today2 = str(datetime.datetime.now() + datetime.timedelta(days=2))[0:10]

# 予報したい都道府県入力処理
st.write("直近お天気予報")
[prefecture_jp_day, prefecture_en_day, data] = prefecture_box.func(today)
[prefecture_jp_day1, prefecture_en_day1, data1] = prefecture_box.func(today1)
[prefecture_jp_day2, prefecture_en_day2, data2] = prefecture_box.func(today2)

# 予報ボタン押下後の処理
if st.button("予報！"):
    day_list = [today, today1, today2]
    prefecture_jp_day_list = [prefecture_jp_day, prefecture_jp_day1, prefecture_jp_day2]
    prefecture_en_day_list = [prefecture_en_day1, prefecture_en_day1, prefecture_en_day2]
    data_list = [data, data1, data2]
    max_temp_list = []
    min_temp_list = []
    condition_list = []
    daily_chance_of_rain_list = []
    result = np.array([])
    for i in range(3):
        result = forcast.display_day(prefecture_jp_day_list[i], prefecture_en_day_list[i], data_list[i], i)
        max_temp_list.append(result[0])
        min_temp_list.append(result[1])
        daily_chance_of_rain_list.append(result[2])
        condition_list.append(result[3])
    
    # 天気予報テーブル
    df = pd.DataFrame({
        '日程': day_list,
        '都道府県': prefecture_jp_day_list,
        '最高気温': max_temp_list,
        '最低気温': min_temp_list,
        '降水確率': daily_chance_of_rain_list,
        '天気': condition_list
        })

    # 天気予報表示
    st.write("予報結果はこちら！")
    st.write(df)
