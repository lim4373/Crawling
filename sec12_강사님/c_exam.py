# Note (Example is valid for Python v2 and v3)
from __future__ import print_function

import sys

#sys.path.insert(0, 'python{0}/'.format(sys.version_info[0]))

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost'
}
cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
##cur.execute("SHOW STATUS LIKE 'Ssl_cipher'")
cur.execute("select  * from my_emp.emp")
res=cur.fetchall()
for  r  in res:
    print(r)
cur.close()
cnx.close()