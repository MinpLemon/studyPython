#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 20:35
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : pandas_to_json.py
# @Software: PyCharm

import pandas as pd


df = pd.DataFrame(['89','100'],['98','99'],
                  index=['数学','语文'],
                  columns=['小王','小屋'])
df.to_json(orient='split')
df.to_json(orient='index')
df.to_json(orient='records')
df.to_json(orient='table')
