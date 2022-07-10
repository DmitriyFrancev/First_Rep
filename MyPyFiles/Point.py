# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:07:28 2022

@author: PK
"""

class Point:
    def __init__(self, x, y):   # Конструктор класса. __init__ - метод-конструктор (дандер метод)
        self.x = x
        self.y = y

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    