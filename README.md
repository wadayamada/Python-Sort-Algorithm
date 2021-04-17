# Python-Sort-Algorithm
Pythonで選択ソートとクイックソートを実装しました

## 選択ソート

> データ列中で一番小さい値を探し、1番目の要素と交換する。次に、2番目以降のデータ列から一番小さい値を探し、2番目の要素と交換する。これを、データ列の最後まで繰り返す

[選択ソート \- Wikipedia](https://ja.wikipedia.org/wiki/%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88#:~:text=%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88%EF%BC%88%E8%8B%B1%3A%20selection%20sort,%E3%81%AA%E3%81%9F%E3%82%81%E3%80%81%E3%81%97%E3%81%B0%E3%81%97%E3%81%B0%E7%94%A8%E3%81%84%E3%82%89%E3%82%8C%E3%82%8B%E3%80%82)

## クイックソート

> 1. 適当な数（**[ピボット](https://ja.wikipedia.org/w/index.php?title=ピボット_(数学)&action=edit&redlink=1)（[英語版](https://en.wikipedia.org/wiki/Pivot_element)）**という）を選択する（この場合は[データ](https://ja.wikipedia.org/wiki/データ)の総数の[中央値](https://ja.wikipedia.org/wiki/中央値)が望ましい）
> 2. ピボットより小さい数を前方、大きい数を後方に移動させる （分割）
> 3. 二分割された各々のデータを、それぞれソートする

[クイックソート \- Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88#:~:text=%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88%20(quicksort)%20%E3%81%AF%E3%80%81,%E5%88%86%E5%89%B2%E7%B5%B1%E6%B2%BB%E6%B3%95%E3%81%AE%E4%B8%80%E7%A8%AE%E3%80%82)
