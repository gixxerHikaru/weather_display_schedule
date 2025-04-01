import streamlit as st
import datetime
import forcast, prefecture_box, weather_condition_convert as wc_convert
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

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
        condition_list.append(wc_convert.func(result[4]))
    
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

    # グラフの設定
    plt.figure(figsize=(12, 6))
    japanize_matplotlib.japanize()  # 日本語表示を有効にする

    # 最高気温と最低気温の折れ線グラフ
    ax1 = plt.gca()  # 現在の軸を取得
    ax1.plot(df['日程'] + '\n' + df['都道府県'], df['最高気温'], marker='o', label='最高気温', color='red')
    ax1.plot(df['日程'] + '\n' + df['都道府県'], df['最低気温'], marker='o', label='最低気温', color='blue')
    # ax1.set_xlabel('日程\n都道府県')
    ax1.set_ylabel('気温 (℃)')
    ax1.tick_params(axis='y', labelcolor='black')

    # 降水確率の棒グラフ
    ax2 = ax1.twinx()  # 2つ目のy軸を作成
    ax2.bar(df['日程'] + '\n' + df['都道府県'], df['降水確率'], alpha=0.5, label='降水確率', color='skyblue')
    ax2.set_ylabel('降水確率 (%)')
    ax2.tick_params(axis='y', labelcolor='black')

    # グラフの装飾
    plt.title('日程別 都道府県別 気温と降水確率')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()

    # グラフの表示
    st.pyplot(plt)

    st.write(df)
