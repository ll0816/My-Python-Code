import pandas as pd

df = pd.DataFrame([(1, 'Kolter', 'Zico'),
                   (2, 'Wong', 'Eric'),
                   (3, 'Eswaran', 'Dhivya')],
                  columns=["Person ID", "Last Name", "First Name"])

df.set_index("Person ID", inplace=True)

#df = pd.read_csv()

print df.head()

print df.loc[:, "Last Name"]
print df.loc[:, ["Last Name"]]
print df.loc[[1,2], :]
df.loc[1, "Last Name"] = "Kilter"
df.loc[7, :] = ("Moore", "Andrew")
print df.iloc[0,0]

import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE role;")
conn.commit()
cursor.execute("""
CREATE TABLE role (
    id INTEGER PRIMARY KEY,
    name TEXT)""")
cursor.execute("INSERT INTO role VALUES (1, 'Instructor')")
cursor.execute("INSERT INTO role VALUES (2, 'TA')")
cursor.execute("INSERT INTO role VALUES (3, 'Student')")
conn.commit()
cursor.execute("DELETE FROM role WHERE id == 3")
conn.commit()
# conn.rollback()

for row in cursor.execute('SELECT * FROM role'):
    print row

pd.read_sql_query("SELECT * FROM role", conn, index_col="id")
#conn.close()


