import prefectures_jp_en_list

def func(prefecture_jp):
    for i in prefectures_jp_en_list.prefectures_jp_en[:,0]:
        if i == prefecture_jp:
            return True
    raise ValueError("正しい都道府県名を入力してください。")

if __name__ == '__main__':
    print("都道府県名チェック")
    try:
        prefecture_jp = input("都道府県名入力してください。")
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
    else:
        print("入力　:" + prefecture_jp)
        print("都道府県名チェック")
        if(func(prefecture_jp)):
            print("OK")
        else:
            print("NG")
