import cx_Oracle
from aiogram.types import Message

dsn = cx_Oracle.makedsn(host='192.168.8.19', port=1521, service_name='ORCLPDB1')
username = 'telegram'
password = 'telegrambase'


def insert_user_message(message: Message):
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

    cursor = connection.cursor()
    print(message.date)
    date_str = str(int(message.date.timestamp()))
    print(date_str)
    str_sql = f''

    cursor.execute("""
        INSERT INTO MESSAGES (MESSAGE_ID, OWNER_MSG, TEXT_MSG, DATE_MSG)
        VALUES (:message_id, :owner_msg, :text_msg, to_date('YYYY-MM-DD H24:MI:SS',SUBSTR(:date_msg,1,20))
    """, message_id=str(message.message_id), owner_msg=str(message.from_user.id), text_msg=str(message.text), date_msg=message.date)

    connection.commit()
    cursor.close()
    connection.close()