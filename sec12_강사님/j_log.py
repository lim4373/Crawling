from my_log import connect_to_mysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "0000",
    "database": "my_emp",
}

cnx = connect_to_mysql(config, attempts=3)

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:

        result = cursor.execute("SELECT * FROM emp LIMIT 5")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()

else:
    print("Could not connect")