import sqlite3
from collections import OrderedDict
from contextlib import closing

from django.db import connection


def dict_fetchall(cursor):
    columns = [i[0] for i in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    root = cursor.fetchall()
    if root is None:
        return None
    columns = [i[0] for i in cursor.description]
    return dict(zip(columns, root))


def get_recipes_all(pk):
    sql = "select * from school_category"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = []
        for i in dict_fetchall(cursor):
            result.append(_format(i))

    return result


def get_recipes_one(pk):
    sql = "select * from school_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None

    return result


def _format(data):
    return OrderedDict([
        ('id', data['id']),
        ('s', data['slug']),
        ('c', data['content']),
    ])
