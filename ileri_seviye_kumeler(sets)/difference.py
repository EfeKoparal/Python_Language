"""
İki kümenin farkı : difference() metodu
Bu metod birinci kümenin ikinci kümeden farkını döner.

    küme1.difference(küme2) # Küme1'in Küme2'den farkı
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.difference(küme2)
{-2, 3, 10, 100}
küme2.difference(küme1)
{-1, 23}
küme1
{-2, 1, 2, 3, 10, 34, 100}
İki kümenin farkı ve güncelleme : difference_update() metodu
Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.

küme1.difference_update(küme2) # Küme1'in Küme2'den farkı
küme1
{-2, 1, 2, 3, 10, 34, 100}
küme2
{-1, 1, 2, 23, 34}
küme1.difference_update(küme2)
küme1 # Farka göre güncellendi.
{-2, 3, 10, 100}
"""
