import datetime
import forcast, prefectures_check, prefectures_convert

today = str(datetime.datetime.now())[0:10]
today1 = str(datetime.datetime.now() + datetime.timedelta(days=1))[0:10]
today2 = str(datetime.datetime.now() + datetime.timedelta(days=2))[0:10]

def forcast_day(day, day_num):
    try:
        day_pre_jp = input(day + ":")
        prefectures_check.func(day_pre_jp)
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
    else:   
        # 回答表示処理
        forcast.func_day(day_pre_jp, day_num)
    finally:
        print("-" * 60)


def func():
    # 都道府県入力処理
    print("直近３日間のあなたの所在地を教えてください。")
    forcast_day(today, 0)

    forcast_day(today1, 1)

    forcast_day(today2, 2)
    

if __name__ == '__main__':
    func()
    