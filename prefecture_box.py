import os
import streamlit as st
import prefectures_jp_en_list, forcast, prefectures_convert as p_convert

#https://www.weatherapi.com/
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def func(day):
    prefecture_jp_day = st.selectbox(
    day + 'に滞在する都道府県名を選択',
     prefectures_jp_en_list.prefectures_jp_en
    )
    prefecture_en_day = p_convert.func(prefecture_jp_day)
    url = "http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=7&aqi=no&alerts=no".format(WEATHER_API_KEY, prefecture_en_day)
    data = forcast.forcast(url)
    return prefecture_jp_day, prefecture_en_day, data
