import unittest
import no76_tsurukame as tsurukame

# $ python3 -m unittest no78.py 
class TestTsurukame(unittest.TestCase):

    def setUp(self):
        '''前準備'''
        # インスタンスを前もって準備する
        self.tsuru = tsurukame.Tsuru()
        self.kame = tsurukame.Kame()
        self.tako = tsurukame.Tako()
        self.ika = tsurukame.Ika()

    def tearDown(self):
        '''後片付け'''
        pass

    def test_legs(self):
        # 鶴と亀の足の数を確認
        self.assertEqual(self.tsuru.get_legs(), 2, "足の数")
        self.assertEqual(self.kame.get_legs(), 4, "足の数")

    def test_basic(self):
        # 鶴亀算を計算
        tsuru, kame = tsurukame.calc_tsurukame(
            self.tsuru,
            self.kame,
            heads = 10,
            legs = 28
        )
        self.assertEqual((tsuru, kame), (6, 4), "鶴と亀の計算")

    def test_tsuru_ika(self):
        # 鶴亀算を計算
        tsuru, ika = tsurukame.calc_tsurukame(
            self.tsuru,
            self.ika,
            heads = 6,
            legs = 36
        )
        self.assertEqual((tsuru, ika), (3, 3), "鶴とイカの計算")

        # ---
        # 頭= 10 足= 28
        # 鶴 = 6
        # 亀 = 4
        # ..---
        # 頭= 6 足= 36
        # 鶴 = 3
        # イカ = 3
        # .
        # ----------------------------------------------------------------------
        # Ran 3 tests in 0.001s
        #
        # OK
