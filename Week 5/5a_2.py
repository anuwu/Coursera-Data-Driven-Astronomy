import psycopg2
import numpy as np

def column_stats(table_name, column_name) :
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('select {} from {}'.format(column_name, table_name))
  dat = np.array(cursor.fetchall())
  return np.mean(dat), np.median(dat)
