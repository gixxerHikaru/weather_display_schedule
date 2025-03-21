from prefectures_convert import func
import pytest
# テスト使い方
# 全通し pytest test_xxx.py
# クラス実行 pytest test_xxx.py::ClassName


# Error
class TestError:
    def test_error1(self):
        prefecture_jp = "a"
        with pytest.raises(ValueError) as e:
            func(prefecture_jp)
        assert "正しい都道府県名を入力してください。" == str(e.value)
    def test_error2(self):
        prefecture_jp = "東京"
        with pytest.raises(ValueError) as e:
            func(prefecture_jp)
        assert "正しい都道府県名を入力してください。" == str(e.value)
    def test_error3(self):
        prefecture_jp = "あおもりけん"
        with pytest.raises(ValueError) as e:
            func(prefecture_jp)
        assert "正しい都道府県名を入力してください。" == str(e.value)
    def test_error4(self):
        prefecture_jp = "Hokkaido"
        with pytest.raises(ValueError) as e:
            func(prefecture_jp)
        assert "正しい都道府県名を入力してください。" == str(e.value)


# 47prefecturesTest
class TestHokkaido:
    def test_hokkaido(self):
        prefecture_jp = "北海道"
        assert "Hokkaido" == func(prefecture_jp)

class TestTohoku:
    def test_aomori(self):
        prefecture_jp = "青森県"
        assert "Aomori" == func(prefecture_jp)

    def test_iwate(self):
        prefecture_jp = "岩手県"
        assert "Iwate" == func(prefecture_jp)

    def test_miyagi(self):
        prefecture_jp = "宮城県"
        assert "Miyagi" == func(prefecture_jp)

    def test_akita(self):
        prefecture_jp = "秋田県"
        assert "Akita" == func(prefecture_jp)

    def test_yamagata(self):
        prefecture_jp = "山形県"
        assert "Yamagata" == func(prefecture_jp)

    def test_fukushima(self):
        prefecture_jp = "福島県"
        assert "Fukushima" == func(prefecture_jp)

class TestKanto:
    def test_ibaraki(self):
        prefecture_jp = "茨城県"
        assert "Ibaraki" == func(prefecture_jp)

    def test_tochigi(self):
        prefecture_jp = "栃木県"
        assert "Tochigi" == func(prefecture_jp)

    def test_gunma(self):
        prefecture_jp = "群馬県"
        assert "Gunma" == func(prefecture_jp)

    def test_saitama(self):
        prefecture_jp = "埼玉県"
        assert "Saitama" == func(prefecture_jp)

    def test_chiba(self):
        prefecture_jp = "千葉県"
        assert "Chiba" == func(prefecture_jp)

    def test_tokyo(self):
        prefecture_jp = "東京都"
        assert "Tokyo" == func(prefecture_jp)

    def test_kanagawa(self):
        prefecture_jp = "神奈川県"
        assert "Kanagawa" == func(prefecture_jp)

class TestChubu:
    def test_niigata(self):
        prefecture_jp = "新潟県"
        assert "Niigata" == func(prefecture_jp)

    def test_toyama(self):
        prefecture_jp = "富山県"
        assert "Toyama" == func(prefecture_jp)

    def test_ishikawa(self):
        prefecture_jp = "石川県"
        assert "Ishikawa" == func(prefecture_jp)

    def test_fukui(self):
        prefecture_jp = "福井県"
        assert "Fukui" == func(prefecture_jp)

    def test_yamanashi(self):
        prefecture_jp = "山梨県"
        assert "Yamanashi" == func(prefecture_jp)

    def test_nagano(self):
        prefecture_jp = "長野県"
        assert "Nagano" == func(prefecture_jp)

    def test_gifu(self):
        prefecture_jp = "岐阜県"
        assert "Gifu" == func(prefecture_jp)

    def test_shizuoka(self):
        prefecture_jp = "静岡県"
        assert "Shizuoka" == func(prefecture_jp)

    def test_aichi(self):
        prefecture_jp = "愛知県"
        assert "Aichi" == func(prefecture_jp)

class TestKinki:
    def test_mie(self):
        prefecture_jp = "三重県"
        assert "Mie" == func(prefecture_jp)

    def test_shiga(self):
        prefecture_jp = "滋賀県"
        assert "Shiga" == func(prefecture_jp)

    def test_kyoto(self):
        prefecture_jp = "京都府"
        assert "Kyoto" == func(prefecture_jp)

    def test_osaka(self):
        prefecture_jp = "大阪府"
        assert "Osaka" == func(prefecture_jp)

    def test_hyogo(self):
        prefecture_jp = "兵庫県"
        assert "Hyogo" == func(prefecture_jp)

    def test_nara(self):
        prefecture_jp = "奈良県"
        assert "Nara" == func(prefecture_jp)

    def test_wakayama(self):
        prefecture_jp = "和歌山県"
        assert "Wakayama" == func(prefecture_jp)

class TestChugoku:
    def test_tottori(self):
        prefecture_jp = "鳥取県"
        assert "Tottori" == func(prefecture_jp)

    def test_shimane(self):
        prefecture_jp = "島根県"
        assert "Shimane" == func(prefecture_jp)

    def test_okayama(self):
        prefecture_jp = "岡山県"
        assert "Okayama" == func(prefecture_jp)

    def test_hiroshima(self):
        prefecture_jp = "広島県"
        assert "Hiroshima" == func(prefecture_jp)

    def test_yamaguchi(self):
        prefecture_jp = "山口県"
        assert "Yamaguchi" == func(prefecture_jp)

class TestShikoku:
    def test_tokushima(self):
        prefecture_jp = "徳島県"
        assert "Tokushima" == func(prefecture_jp)

    def test_kagawa(self):
        prefecture_jp = "香川県"
        assert "Kagawa" == func(prefecture_jp)

    def test_ehime(self):
        prefecture_jp = "愛媛県"
        assert "Ehime" == func(prefecture_jp)

    def test_kochi(self):
        prefecture_jp = "高知県"
        assert "Kochi" == func(prefecture_jp)

class TestKyushuOkinawa:
    def test_fukuoka(self):
        prefecture_jp = "福岡県"
        assert "Fukuoka" == func(prefecture_jp)

    def test_saga(self):
        prefecture_jp = "佐賀県"
        assert "Saga" == func(prefecture_jp)

    def test_nagasaki(self):
        prefecture_jp = "長崎県"
        assert "Nagasaki" == func(prefecture_jp)

    def test_kumamoto(self):
        prefecture_jp = "熊本県"
        assert "Kumamoto" == func(prefecture_jp)

    def test_oita(self):
        prefecture_jp = "大分県"
        assert "Oita" == func(prefecture_jp)

    def test_miyazaki(self):
        prefecture_jp = "宮崎県"
        assert "Miyazaki" == func(prefecture_jp)

    def test_kagoshima(self):
        prefecture_jp = "鹿児島県"
        assert "Kagoshima" == func(prefecture_jp)

    def test_okinawa(self):
        prefecture_jp = "沖縄県"
        assert "Okinawa" == func(prefecture_jp)
