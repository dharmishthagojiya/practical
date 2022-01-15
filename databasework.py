import psycopg2
if __name__ == "__main__":
    conn = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="ahir1234@",
        database="student")
    cur = conn.cursor()
 #   cur.execute('''INSERT INTO result(ID, name, subject, Marks
 #    ) VALUES ('5', 'Maddy ', 'chemistry', 90)''')
#   cur.execute('''INSERT INTO result(ID, name, subject, Marks
#          ) VALUES ('4', 'priya', 'english', 80)''')

    print("Table Before updating record ")
    sql_select_query = """select * from result"""
    cur.execute(sql_select_query)
    record = cur.fetchall()
    print(record)
    print("Table Before updating record table student ")
    sql_select_query1 = """select * from student"""
    cur.execute(sql_select_query1)
    record1 = cur.fetchall()
    print(record1)
  #  sql = '''SELECT * from student INNER JOIN result\
  #  ON student.name = result.name '''
# sql = '''SELECT * from student FULL JOIN result\
 #       ON student.name = result.name '''
  #  sql = '''SELECT * from student LEFT JOIN result\
#     ON student.name = result.name '''
# sql = '''SELECT * from student RIGHT JOIN result\
 #       ON student.name = result.name '''
    sql = '''SELECT result.name,result.Marks,
      student.name from result cross JOIN student'''
    cur.execute(sql)
    results = cur.fetchall()
    for i in results:
        print(i)

    conn.commit()
    conn.close()
    #table create
#  create_table = '''CREATE TABLE result
#                   (ID INT PRIMARY KEY NOT NULL,
#                    name TEXT NULL,
#                   subject TEXT NULL,
#                   Marks REAL);'''
'''cur.execute(create_table)
   conn.commit()
   print("table created")
'''
