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