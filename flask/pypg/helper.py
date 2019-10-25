import psycopg2 as pg

pg_local = {
    'host':"localhost",
    'user':"postgres",
    'dbname':"postgres",
    'password':"Ska25zns!"
}

#postgres://dbuser:1234@postgres/dbapp
#localhost == 127.0.0.1
#postgres://postgress:빕번@127.0.0.1/postgres

db_connector = pg_local 

connect_string = "host={host} user={user} dbname={dbname} password={password}".format(
    **db_connector)

def read_tables():
    tables =[]
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
                cur.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
                for table in cur.fetchall():
                    tables.append(table)
    return tables

# with pg.connect(connect_string) as conn:
#     with conn.cursor() as cur:
#         cur.execute(
#             "CREATE TABLE guser (      id integer primary key,      name varchar(20),      email varchar(20)    );")

def read_dbs():
    sql = '''SELECT datname FROM pg_database;'''
    with pg.connect(connect_string) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            for db in cur.fetchall():
                print(db)

def create_table(table_name):
    sql = f'''CREATE TABLE {table_name} (
            id integer primary key,
            name varchar(20),
            email varchar(20)
            );
        '''
    print(sql)
    try:
        conn = pg.connect(connect_string)#db 연결
        cur = conn.cursor()#작업할 지시자 정하기
        cur.execute(sql)#실행

        #db 저장하고 마무리
        conn.commit()#select 제외 commit 필요 db에 저장하는 거
        conn.close()
        #db 연결 해제
    except pg.OperationalError as e:
        print(e)

def insert(table_name):
    sql = f'''INSERT INTO {table_name}
            VALUES({sid},\'{name}\', \'{email}\');
        '''
    print(sql)
    try:
        conn = pg.connect(connect_string)#db 연결
        cur = conn.cursor()#작업할 지시자 정하기
        cur.execute(sql)#실행

        #db 저장하고 마무리
        conn.commit()#select 제외 commit 필요 db에 저장하는 거
        conn.close()
        #db 연결 해제
    except pg.OperationalError as e:
        print(e)
        return -1
    return 0

def main():
    print("pg!")
    read_dbs()
    create_table("student")
    read_tables()

#if __name__ == ("__main__"):
#    main()
