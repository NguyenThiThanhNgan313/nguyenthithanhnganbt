# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:38:36 2024

@author: ASUS
"""

def tinhtong(*args,**kwargs):
    return sum(args)
def tich_tong(*args,**kwargs):
    tich=1
    for i in args:
        tich*=i
    return tich
if __name__=="__main__":
    ds=[1,2,3,4,5]
    print(tinhtong(*ds))
    print(tich_tong(*ds))