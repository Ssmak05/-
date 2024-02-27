import psycopg2
con=psycopg2.connect(dbname='test',user='postgres', password='Q1w2e3r4', host='localhost')
cursor=con.cursor()
#id="WHERE id=1"

def select(id):
    cursor = con.cursor()
    id = "WHERE id=1"
    qwery = f"""SELECT * FROM public.logins {id};"""
    cursor.execute(qwery)
    data=cursor.fetchone()
    print(data)
select(int(input('введите id')))
def update():
    qwery=f"""UPDATE public.logins SET password= '23www' {id};"""
    cursor.execute(qwery)
    con.commit()
    data=cursor.fetchone()
    print(data)




# cursor=con.cursor()
# qwery='SELECT id, login, password FROM public.logins;'
# qwery="UPDATE public.logins SET password= '232323www' WHERE id=1;"
# cursor.execute(qwery)
# con.commit()
# data=cursor.fetchall()
# print(data)
