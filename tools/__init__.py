#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 12:27 AM
# @Author : maxu
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
import sql

sql = sql.Sql()


def initS():
    with open('../static/file/waterS.csv', 'r', encoding='utf-8', newline='')as f:
        import csv

        reader = csv.reader(f)
        index = 0
        for row in reader:
            if index == 0:
                pass
            else:
                for i in range(len(row)):
                    row[i] = str(row[i]).replace(' ', '')
                print(row)
                sql.newS(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                         row[11])
            index += 1


def initN():
    with open('../static/file/waterN.csv', 'r', encoding='utf-8', newline='')as f:
        import csv

        reader = csv.reader(f)
        index = 0
        for row in reader:
            if index == 0:
                pass
            else:
                for i in range(len(row)):
                    row[i] = str(row[i]).replace(' ', '')
                print(row)
                sql.newN(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                         row[11])
            index += 1


if __name__ == '__main__':
    # initN()
    pass
