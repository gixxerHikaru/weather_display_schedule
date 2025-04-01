
weather_conditions = [
    {"code": 1000, "day": "晴れ", "night": "晴れ", "icon": 113},
    {"code": 1003, "day": "晴れ時々曇り", "night": "晴れ時々曇り", "icon": 116},
    {"code": 1006, "day": "曇り", "night": "曇り", "icon": 119},
    {"code": 1009, "day": "どんよりした曇り", "night": "どんよりした曇り", "icon": 122},
    {"code": 1030, "day": "霧", "night": "霧", "icon": 143},
    {"code": 1063, "day": "所により雨の可能性", "night": "所により雨の可能性", "icon": 176},
    {"code": 1066, "day": "所により雪の可能性", "night": "所により雪の可能性", "icon": 179},
    {"code": 1069, "day": "所によりみぞれの可能性", "night": "所によりみぞれの可能性", "icon": 182},
    {"code": 1072, "day": "所により着氷性の霧雨の可能性", "night": "所により着氷性の霧雨の可能性", "icon": 185},
    {"code": 1087, "day": "雷雨の可能性", "night": "雷雨の可能性", "icon": 200},
    {"code": 1114, "day": "地吹雪", "night": "地吹雪", "icon": 227},
    {"code": 1117, "day": "吹雪", "night": "吹雪", "icon": 230},
    {"code": 1135, "day": "霧", "night": "霧", "icon": 248},
    {"code": 1147, "day": "着氷性の霧", "night": "着氷性の霧", "icon": 260},
    {"code": 1150, "day": "所により小雨の霧雨", "night": "所により小雨の霧雨", "icon": 263},
    {"code": 1153, "day": "小雨の霧雨", "night": "小雨の霧雨", "icon": 266},
    {"code": 1168, "day": "着氷性の霧雨", "night": "着氷性の霧雨", "icon": 281},
    {"code": 1171, "day": "大量の着氷性の霧雨", "night": "大量の着氷性の霧雨", "icon": 284},
    {"code": 1180, "day": "所により小雨", "night": "所により小雨", "icon": 293},
    {"code": 1183, "day": "小雨", "night": "小雨", "icon": 296},
    {"code": 1186, "day": "時々中程度の雨", "night": "時々中程度の雨", "icon": 299},
    {"code": 1189, "day": "中程度の雨", "night": "中程度の雨", "icon": 302},
    {"code": 1192, "day": "時々大雨", "night": "時々大雨", "icon": 305},
    {"code": 1195, "day": "大雨", "night": "大雨", "icon": 308},
    {"code": 1198, "day": "小さな着氷性の雨", "night": "小さな着氷性の雨", "icon": 311},
    {"code": 1201, "day": "中程度または大量の着氷性の雨", "night": "中程度または大量の着氷性の雨", "icon": 314},
    {"code": 1204, "day": "小さなみぞれ", "night": "小さなみぞれ", "icon": 317},
    {"code": 1207, "day": "中程度または大量のみぞれ", "night": "中程度または大量のみぞれ", "icon": 320},
    {"code": 1210, "day": "所により小さな雪", "night": "所により小さな雪", "icon": 323},
    {"code": 1213, "day": "小さな雪", "night": "小さな雪", "icon": 326},
    {"code": 1216, "day": "所により中程度の雪", "night": "所により中程度の雪", "icon": 329},
    {"code": 1219, "day": "中程度の雪", "night": "中程度の雪", "icon": 332},
    {"code": 1222, "day": "所により大雪", "night": "所により大雪", "icon": 335},
    {"code": 1225, "day": "大雪", "night": "大雪", "icon": 338},
    {"code": 1237, "day": "アイスペレット", "night": "アイスペレット", "icon": 350},
    {"code": 1240, "day": "小雨のにわか雨", "night": "小雨のにわか雨", "icon": 353},
    {"code": 1243, "day": "中程度または大雨のにわか雨", "night": "中程度または大雨のにわか雨", "icon": 356},
    {"code": 1246, "day": "激しいにわか雨", "night": "激しいにわか雨", "icon": 359},
    {"code": 1249, "day": "小さなにわかみぞれ", "night": "小さなにわかみぞれ", "icon": 362},
    {"code": 1252, "day": "中程度または大量のにわかみぞれ", "night": "中程度または大量のにわかみぞれ", "icon": 365},
    {"code": 1255, "day": "小さなにわか雪", "night": "小さなにわか雪", "icon": 368},
    {"code": 1258, "day": "中程度または大量のにわか雪", "night": "中程度または大量のにわか雪", "icon": 371},
    {"code": 1261, "day": "小さなにわかのアイスペレット", "night": "小さなにわかのアイスペレット", "icon": 374},
    {"code": 1264, "day": "中程度または大量のにわかのアイスペレット", "night": "中程度または大量のにわかのアイスペレット", "icon": 377},
    {"code": 1273, "day": "所により雷を伴う小雨", "night": "所により雷を伴う小雨", "icon": 386},
    {"code": 1276, "day": "雷を伴う中程度または大雨", "night": "雷を伴う中程度または大雨", "icon": 389},
    {"code": 1279, "day": "所により雷を伴う小さな雪", "night": "所により雷を伴う小さな雪", "icon": 392},
    {"code": 1282, "day": "雷を伴う中程度または大雪", "night": "雷を伴う中程度または大雪", "icon": 395}
]

def func(weather_condition_code):
    # 入力されたコードと一致する日本語の天気情報を返す。
    for i in weather_conditions:
        if i['code'] == weather_condition_code:
            return i['day']
        
    return False

if __name__ == '__main__':
    weather_condition_code = input("Plaease Enter weather_condition_code")
    func(weather_condition_code)
