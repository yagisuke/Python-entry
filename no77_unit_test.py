import unittest
import no76_tsurukame as tsurukame


class TestTsurukame(unittest.TestCase):

    # $ python3 -m unittest no77_unit_test.py
    def test_tsurukame(self):
        # 鶴亀算を計算
        tsuru, kame = tsurukame.calc_tsurukame(
            tsurukame.Tsuru(),
            tsurukame.Kame(),
            heads = 10,
            legs = 28
        )

        # 結果を検証する
        self.assertEqual(tsuru, 6, "基本的な計算で鶴の数")
        self.assertEqual(kame, 4, "基本的な計算で亀の数")
        # ---
        # 頭= 10 足= 28
        # 鶴 = 6
        # 亀 = 4
        # .
        # ----------------------------------------------------------------------
        # Ran 1 test in 0.000s
        #
        # OK
