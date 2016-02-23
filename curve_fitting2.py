# -*- coding; utf-8 -*-

import os

import matplotlib.pyplot as plt
import scipy as sp


def plot_data(csv_file):
    """
    データをプロットする関数
    csv_file:

    以下のような形式のCSVファイル
    ---------------
    1,1
    2,10
    3,100
    ・・・・・・・・
     ---------------
    """

    data = sp.genfromtxt(csv_file, delimiter=",")

    x = data[:, 0]
    y = data[:, 1]
    """
    ↑のように書くと、
    x = [1, 2, 3, ・・・]
    y = [1, 10, 100, ・・・]
    のように、CSVファイルの列のデータを取り出すことができます。
    便利。
    """

    """
    データをプロットします。
    """
    plt.scatter(x, y)


    """
    曲線フィッティングを描画します。
    scipyで曲線フィッティングしてくれるpolyfitという関数があります。

    polyfit とは、 polynomial fitting の略で、polinomial とは「多項式」のことなので、
    厳密には多項式フィッティングというべきでしょうか。

    色々な値が返ってきますが、aの中に多項式の説明のところにあるa_0、a_1、・・・のデータが入っているので、
    aだけを使います。

    dim の数を増やすことで、曲線の波の個数が増えていきます。
    """
    dim = 10
    a, residuals, rank, sv, rcond = sp.polyfit(x, y, dim, full=True)

    """
    aを使って、曲線（多項式）を求めます。
    """
    f = sp.poly1d(a)

    """
    多項式を描画します。
    描画する横軸xの範囲を指定(fx)し、描画します。
    """
    fx = sp.linspace(0, x[-1], 1000)
    plt.plot(fx, f(fx), "r", linewidth=6)

    """
    lavelは自由に変更しても構いません。
    """
    plt.xlabel("カウント")
    plt.ylabel("実データ")

    """
    グラフを表示するときのスケールを設定できます。
    """
    plt.autoscale(tight=True)


    """
    プロットされたグラフを表示します。
    """
    plt.show()

if __name__ == '__main__':

    plot_data("./access_data.csv")