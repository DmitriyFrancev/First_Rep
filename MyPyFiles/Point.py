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
    
    def __str__(self):      # Определяем строковое представление объекта
        class_info = 'Point({0:.5f}, {1:.5f})'.format(self.x, self.y)   # 'Point({0:.5f}, {1:.5f})' - форматирование строки вывода (до 5 знаков для каждого аргумента)
        return class_info

class Point3D(Point):
    def __init__ (self, x, y, z):
        Point.__init__(self, x, y)   # Инициализация свойств родителя
        self.z = z                   # Инициализация дополнительного свойства потомка