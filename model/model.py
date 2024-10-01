import cx_Oracle
from aiogram.types import Message

dsn = cx_Oracle.makedsn(host='192.168.8.19', port=1521, service_name='ORCLPDB1')
username = 'telegram'
password = 'telegrambase'


def insert_user_message(message: Message):
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO MESSAGES (column1)
        VALUES (:value1)
    """, value1=12)

    connection.commit()
    cursor.close()
    connection.close()