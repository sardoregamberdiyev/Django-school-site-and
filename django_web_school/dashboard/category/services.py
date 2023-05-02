from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import dict_fetchall, dict_fetchone


def ctg_list(pk):
    sql = "select * from school_category"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = []
        for i in dict_fetchall(cursor):
            result.append(_format(i))

    return result


def ctg_one(pk):
    sql = 'select * from school_category where id=%s'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None
    return result


def ctg_delete(pk):
    sql = 'delete from school_category where id=%s'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])


def ctg_rec_delete(pk):
    sql = 'delete from school_recipe where ctg_id=%s'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])


def _format(date):
    return OrderedDict([
        ('id', date['id']),
        ('slug', date['slug']),
        ('content', date['content']),
    ])
