import psycopg2 as pg
dsn="host=localhost dbname=postgres user=postgres password=postgres"

def login(username,password):
    user=None
    print(username, password)
    #connect to database
    conn=pg.connect(dsn)
    #Create new cursor
    cursor=conn.cursor()
    login_query="SELECT * FROM ecommerce.user where username='"+username+"' and password='"+password+"'"
    print(login_query)
    try:
        cursor.execute(login_query)
        user=cursor.fetchone()
        conn.commit()
    except:
        print("In Exception")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    return user

