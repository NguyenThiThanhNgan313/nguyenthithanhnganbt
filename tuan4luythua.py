# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:06:08 2024

@author: ASUS
"""

n=int(input("Nhập n = "))
if n >0:
    giaithua=1
    for i in range(1,n+1):
        giaithua = giaithua * i
    print("giai thừa= ",giaithua)
else: 
    print("Số bạn vừa nhập không phải là số nguyên dương")