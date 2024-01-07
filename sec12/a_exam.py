from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(user='root',password='0000', database='employees')
print(cnx)

####https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
##### https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html