"""
FizzBuzz のテストコード

pytest で実行する：
    pytest test_fizzbuzz.py -v
"""

import pytest
from fizzbuzz import fizzbuzz, fizzbuzz_range


# ===================================================
#  fizzbuzz() の正常系テスト
# ===================================================

class TestFizzbuzzNormal:
    """fizzbuzz() の正常な入力に対するテスト。"""

    def test_fizz_3の倍数はFizzを返す(self):
        assert fizzbuzz(3) == 'Fizz'

    def test_fizz_6はFizz(self):
        assert fizzbuzz(6) == 'Fizz'

    def test_fizz_9はFizz(self):
        assert fizzbuzz(9) == 'Fizz'

    def test_buzz_5の倍数はBuzzを返す(self):
        assert fizzbuzz(5) == 'Buzz'

    def test_buzz_10はBuzz(self):
        assert fizzbuzz(10) == 'Buzz'

    def test_buzz_20はBuzz(self):
        assert fizzbuzz(20) == 'Buzz'

    def test_fizzbuzz_15の倍数はFizzBuzzを返す(self):
        assert fizzbuzz(15) == 'FizzBuzz'

    def test_fizzbuzz_30はFizzBuzz(self):
        assert fizzbuzz(30) == 'FizzBuzz'

    def test_fizzbuzz_45はFizzBuzz(self):
        assert fizzbuzz(45) == 'FizzBuzz'

    def test_number_それ以外は数字の文字列を返す(self):
        assert fizzbuzz(1) == '1'

    def test_number_2はそのまま(self):
        assert fizzbuzz(2) == '2'

    def test_number_7はそのまま(self):
        assert fizzbuzz(7) == '7'

    def test_number_戻り値は文字列型(self):
        # int ではなく str を返すことを確認
        assert isinstance(fizzbuzz(1), str)


# ===================================================
#  fizzbuzz() の境界値テスト
# ===================================================

class TestFizzbuzzBoundary:
    """境界値に対するテスト。"""

    def test_boundary_1は最小値(self):
        assert fizzbuzz(1) == '1'

    def test_boundary_14はFizzでもBuzzでもない(self):
        assert fizzbuzz(14) == '14'

    def test_boundary_15はFizzBuzz(self):
        # 15 = 3×5 なので FizzBuzz
        assert fizzbuzz(15) == 'FizzBuzz'

    def test_boundary_16は数字(self):
        assert fizzbuzz(16) == '16'

    def test_boundary_100はBuzz(self):
        # 100 = 4×25 → 5の倍数
        assert fizzbuzz(100) == 'Buzz'

    def test_boundary_1000はBuzz(self):
        assert fizzbuzz(1000) == 'Buzz'


# ===================================================
#  fizzbuzz() の異常系テスト
# ===================================================

class TestFizzbuzzError:
    """不正な入力に対するテスト。"""

    def test_error_0はValueError(self):
        with pytest.raises(ValueError):
            fizzbuzz(0)

    def test_error_負の数はValueError(self):
        with pytest.raises(ValueError):
            fizzbuzz(-1)

    def test_error_floatはTypeError(self):
        with pytest.raises(TypeError):
            fizzbuzz(3.0)  # type: ignore

    def test_error_文字列はTypeError(self):
        with pytest.raises(TypeError):
            fizzbuzz('3')  # type: ignore

    def test_error_Noneはtypeerror(self):
        with pytest.raises(TypeError):
            fizzbuzz(None)  # type: ignore


# ===================================================
#  fizzbuzz_range() のテスト
# ===================================================

class TestFizzbuzzRange:
    """fizzbuzz_range() のテスト。"""

    def test_range_1から3の結果(self):
        assert fizzbuzz_range(1, 3) == ['1', '2', 'Fizz']

    def test_range_1から15の結果(self):
        expected = [
            '1', '2', 'Fizz', '4', 'Buzz',
            'Fizz', '7', '8', 'Fizz', 'Buzz',
            '11', 'Fizz', '13', '14', 'FizzBuzz',
        ]
        assert fizzbuzz_range(1, 15) == expected

    def test_range_同じ値を指定すると1件返る(self):
        assert fizzbuzz_range(5, 5) == ['Buzz']

    def test_range_件数が正しい(self):
        result = fizzbuzz_range(1, 100)
        assert len(result) == 100

    def test_range_startがendより大きいとValueError(self):
        with pytest.raises(ValueError):
            fizzbuzz_range(10, 5)

    def test_range_FizzBuzzの件数が正しい(self):
        # 1〜30 の FizzBuzz（15, 30）は2件
        result = fizzbuzz_range(1, 30)
        assert result.count('FizzBuzz') == 2

    def test_range_Fizzの件数が正しい(self):
        # 1〜15 の Fizz（3,6,9,12）は4件（15はFizzBuzz）
        result = fizzbuzz_range(1, 15)
        assert result.count('Fizz') == 4

    def test_range_Buzzの件数が正しい(self):
        # 1〜15 の Buzz（5,10）は2件（15はFizzBuzz）
        result = fizzbuzz_range(1, 15)
        assert result.count('Buzz') == 2
