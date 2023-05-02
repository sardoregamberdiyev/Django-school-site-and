def dict_fetchall(curcor):
    columns = [i[0] for i in curcor.description]
    return [
        dict(zip(columns, row)) for row in curcor.fetchall()
    ]


def dict_fetchone(curcor):
    root = curcor.fetchone()
    if root is None:
        return None
    columns = [i[0] for i in curcor.description]
    return dict(zip(columns, root))
