"""

Birleşim Kümesi : union() metodu
Bu metod, iki kümenin birleşim kümesini döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.union(küme2)
{-2, -1, 1, 2, 3, 10, 23, 34, 100}
Birleşim Kümesi ve update : update() metodu
Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)
küme1
{-2, -1, 1, 2, 3, 10, 23, 34, 100}

"""
