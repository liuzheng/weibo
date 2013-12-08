#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#


import happybase

connection = happybase.Connection('hostname')
table = connection.table('table-name')

table.put('row-key', {'family:qual1': 'value1',
                      'family:qual2': 'value2'})

row = table.row('row-key')
print row['family:qual1']  # prints 'value1'

for key, data in table.rows(['row-key-1', 'row-key-2']):
    print key, data  # prints row key and data for each row

for key, data in table.scan(row_prefix='row'):
    print key, data  # prints 'value1' and 'value2'

row = table.delete('row-key')
