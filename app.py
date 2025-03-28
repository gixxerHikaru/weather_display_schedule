import streamlit as st
import datetime
import forcast, prefecture_box

today = str(datetime.datetime.now())[0:10]
today1 = str(datetime.datetime.now() + datetime.timedelta(days=1))[0:10]
today2 = str(datetime.datetime.now() + datetime.timedelta(days=2))[0:10]

st.write("直近お天気予報")

[prefecture_jp_day, prefecture_en_day, data] = prefecture_box.func(today)
[prefecture_jp_day1, prefecture_en_day1, data1] = prefecture_box.func(today1)
[prefecture_jp_day2, prefecture_en_day2, data2] = prefecture_box.func(today2)

if st.button("予報！"):
    day_list = [today, today1, today2]
    prefecture_jp_day_list = [prefecture_jp_day, prefecture_jp_day1, prefecture_jp_day2]
    prefecture_en_day_list = [prefecture_en_day1, prefecture_en_day1, prefecture_en_day2]
    data_list = [data, data1, data2]
    for i in range(3):
        st.write(day_list[i] + ":" + prefecture_jp_day_list[i] + "の天気は下記です。")
        st.write(forcast.display_day(prefecture_jp_day_list[i], prefecture_en_day_list[i], data_list[i], i))
