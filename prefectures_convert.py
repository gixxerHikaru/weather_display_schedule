import prefectures_jp_en_list

def func(prefecture_jp):
    for i in prefectures_jp_en_list.prefectures_jp_en:
        if i[0] == prefecture_jp:
            return i[1]
    raise ValueError("正しい都道府県名を入力してください。")

if __name__ == '__main__':
    try:
        prefecture_jp = input("都道府県名を入力してください。")
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
    else:
        print("入力　:" + prefecture_jp)
        print("英字名:" + func(prefecture_jp))
