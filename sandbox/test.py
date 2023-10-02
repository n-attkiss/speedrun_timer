from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="speedrun_timer"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("DESCRIBE categories")
            for item in cursor.fetchall():
                print(item)
except Error as e:
    print(e)

