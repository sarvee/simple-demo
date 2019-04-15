'''
Created on Mar 8, 2017

@author: rishi.kumar02
'''
import cx_Oracle
'''
Having the core DB operations in one place reduces rework and increases modularity
'''


def create_connection():
    return cx_Oracle.Connection('T753033/T753033@10.123.79.56/georli01')

def create_cursor(con):
    return cx_Oracle.Cursor(con)