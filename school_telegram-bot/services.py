import sqlite3

con = sqlite3.connect('register.db', check_same_thread=False)
cur = con.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE "user" (
        "user_id"	INTEGER,
        "user_name"	TEXT UNIQUE,
        "first_name"	TEXT,
        "number"	TEXT,
        "location"	TEXT,
        PRIMARY KEY("user_id" AUTOINCREMENT)
        );
        """)
    con.commit()


def create_table_log():
    cur.execute("""
        CREATE TABLE "Log" (
        "user_id"	INTEGER UNIQUE,
        "message"	TEXT,
        PRIMARY KEY("user_id")
        );
        """)
    con.commit()
    return True


def get_one(pk):
    cur.execute(f"select * from user where user_id={pk}")
    root = cur.fetchone()
    return root


def create_user(user_id, username):
    sql = f"insert into user (user_id, user_name) values ({user_id}, '{username}')"
    cur.execute(sql)
    con.commit()
    return get_one(user_id)


def create_user_log(user_id):
    a = "{\'state\': 0}"
    sql = f"""insert into Log (user_id, message) values({user_id}, "{a}")"""
    cur.execute(sql)
    con.commit()
    return True


def user_log(user_id):
    cur.execute(f"select message from Log where user_id={user_id}")
    cur.fetchone()


def create_log(user_id):
    sql = f"insert into user (user_id, message) values (%s,'%s')"
    cur.execute(sql, [user_id, "{}"])
    con.commit()
    return user_log(user_id)


def get_user_log(user_id):
    cur.execute(f"""select message from Log where user_id={user_id}""")
    return cur.fetchone()


def change_log(user_id, message):
    sql = f""" 
    update Log
    set message = "{message}"   
    where user_id = {user_id}
    """
    cur.execute(sql)
    con.commit()
    return get_user_log(user_id)


def clear_state(user_id, clear=1):
    a = {'state': clear}
    sql = f""" 
       update Log
       set message = "{a}"   
       where user_id = {user_id}
       """
    cur.execute(sql)
    con.commit()
    return get_user_log(user_id)


def edit_user(log, user_id):
    sql = f"""
    update user
    set first_name='{log.get("ism", "")}{log.get("familya", "")}',
    number = '{log.get("phone", "")}',
    location = '{log.get("vil", "")}'
    where user_id={user_id}
    """
    cur.execute(sql)
    con.commit()


def get_ctgs():
    sql = "SELECT * from Category"
    cur.execute(sql)
    return cur.fetchall()

