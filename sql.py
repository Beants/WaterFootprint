#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 1:08 AM
# @Author : maxu
# @Site : 
# @File : sql.py
# @Software: PyCharm
import pymongo


class Sql:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["WF"]

    def newS(self, add, s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, avg):
        table = self.mydb['s']
        temp = {
            'add': add,
            's2004': s2004,
            's2005': s2005,
            "s2006": s2006,
            's2007': s2007,
            's2008': s2008,
            's2009': s2009,
            's2010': s2010,
            's2011': s2011,
            "s2012": s2012,
            "s2013": s2013,
            "avg": avg
        }
        table.insert_one(temp)

    def newN(self, add, s2004, s2005, s2006, s2007, s2008, s2009, s2010, s2011, s2012, s2013, avg):
        table = self.mydb['n']
        temp = {
            'add': add,
            's2004': s2004,
            's2005': s2005,
            "s2006": s2006,
            's2007': s2007,
            's2008': s2008,
            's2009': s2009,
            's2010': s2010,
            's2011': s2011,
            "s2012": s2012,
            "s2013": s2013,
            "avg": avg
        }
        table.insert_one(temp)

    def reg(self, username, password, name, email):
        table = self.mydb['user']
        data = None
        error = 0
        temp = table.find_one({'username': username})
        if temp:
            # 'Account already exists'
            error = 1
        else:
            temp = {
                'username': username,
                'password': password,
                'name': name,
                'email': email
            }
            table.insert_one(temp)
            data = temp
            data['_id'] = str(data['_id']).replace('ObjectId(', '').replace(')', '')
            # print(data)
        return {
            'type': 'reg',
            'code': error,
            'data': data,
        }

    def login(self, username, password):
        table = self.mydb['user']
        data = None
        error = 0
        temp = table.find_one({'username': username, 'password': password, })
        if temp:
            data = {
                'name': temp['name']
            }
        else:
            error = 1
        return {
            'type': 'reg',
            'code': error,
            'data': data,
        }

    def getS_add(self, add):
        table = self.mydb['s']
        res = table.find_one({'add': add})
        res['_id'] = str(res['_id']).replace('ObjectId(', '').replace(')', '')
        return res

    def getS_all(self):
        table = self.mydb['s']
        temp = table.find({})
        res = []
        for i in temp:
            i['_id'] = str(i['_id']).replace('ObjectId(', '').replace(')', '')
            res.append(i)
        return res

    def getN_all(self):
        table = self.mydb['n']
        temp = table.find({})
        res = []
        for i in temp:
            i['_id'] = str(i['_id']).replace('ObjectId(', '').replace(')', '')
            res.append(i)
        return res


if __name__ == '__main__':
    sql = Sql()
    temp = sql.getS_all()
    print(temp)
