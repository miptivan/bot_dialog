import cx_Oracle

# Параметры подключения
dsn = cx_Oracle.makedsn(host='192.168.8.19', port=1521, service_name='ORCLPDB1')
username = 'telegram'
password = 'telegrambase'

# Подключение к базе данных
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

# Создание курсора
cursor = connection.cursor()

# Вставка данных
cursor.execute("""
    INSERT INTO MESSAGES (column1)
    VALUES (:value1)
""", value1=12)

# Фиксация изменений
connection.commit()

# Закрытие курсора и соединения
cursor.close()
connection.close()