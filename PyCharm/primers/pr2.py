#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class River:
    all_rivers = []

    def __init__(self, name, lenght):
        self.name = name
        self.lenght = lenght
        River.all_rivers.append(self)

volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

for river in River.all_rivers:
    print(river.name)