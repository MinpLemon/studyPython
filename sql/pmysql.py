#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 16:15
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : pmysql.py
# @Software: PyCharm

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://root@localhost:3306/mystock')

print(engine)