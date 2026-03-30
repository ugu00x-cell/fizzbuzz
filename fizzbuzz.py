"""
FizzBuzz モジュール

3の倍数で "Fizz"、5の倍数で "Buzz"、両方で "FizzBuzz" を返す。
それ以外は数字を文字列として返す。
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def fizzbuzz(n: int) -> str:
    """1つの数値に対して FizzBuzz の結果を返す。

    Args:
        n: 判定する整数

    Returns:
        "Fizz" / "Buzz" / "FizzBuzz" / 数字の文字列

    Raises:
        TypeError: n が整数でない場合
        ValueError: n が 0 以下の場合
    """
    # 型チェック
    if not isinstance(n, int):
        raise TypeError(f'整数を渡してください（受け取った型: {type(n).__name__}）')

    # 値チェック（0以下は対象外とする）
    if n <= 0:
        raise ValueError(f'1以上の整数を渡してください（受け取った値: {n}）')

    # 15の倍数（3と5の公倍数）を先に判定する
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


def fizzbuzz_range(start: int, end: int) -> list[str]:
    """指定した範囲の FizzBuzz 結果をリストで返す。

    Args:
        start: 開始値（1以上）
        end: 終了値（start 以上）

    Returns:
        FizzBuzz 結果の文字列リスト

    Raises:
        ValueError: start > end の場合
    """
    if start > end:
        raise ValueError(f'start は end 以下にしてください（start={start}, end={end}）')

    results = [fizzbuzz(n) for n in range(start, end + 1)]
    logger.info(f'FizzBuzz 実行完了: {start}〜{end}（{len(results)}件）')
    return results


if __name__ == '__main__':
    # 1〜30 を実行してコンソールに表示
    for result in fizzbuzz_range(1, 30):
        print(result)
