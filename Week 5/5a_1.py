import psycopg2

def select_all (table_name) :
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('select * from {}'.format(table_name))
  return cursor.fetchall()
