# ─────────────────────────────────────────────────────────────
# Iris — генератор цветовых палитр
# (c) 2025 Mitori Vancody Firelight
#
# Разработка и код: Mitori Vancody Firelight
# Связаться со мной:
#   VK:        https://vk.com/mitori_territory
#   Telegram:  https://t.me/Vancody_Firelight
#   GitHub:    https://github.com/Vancody
#   Discord:   @vancodyfirelight
#
# Этот код распространяется без лицензии, но с сохранением авторства.
# Копирование и использование разрешено при указании автора.
# ─────────────────────────────────────────────────────────────

import mysql.connector
from mysql.connector import Error
from .config import db_config

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"[DB_HANDLER ОШИБКА]: Ошибка '{e}' при подключении к MySQL.")
        return None

def check_connection_status(connection):
    if connection is None:
        return False, "Объект соединения не был создан."
    if not connection.is_connected():
        return False, "Соединение с БД потеряно."

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        cursor.close()
        return True, result[0] if result else "N/A"
    except Error as e:
        print(f"[DB_HANDLER ОШИБКА]: Ошибка при проверке соединения: {e}")
        if cursor: cursor.close()
        return False, str(e)
    except Exception as ex:
        print(f"[DB_HANDLER ОШИБКА]: Непредвиденная ошибка при проверке: {ex}")
        if cursor: cursor.close()
        return False, str(ex)

def close_connection(connection):
    if connection and connection.is_connected():
        try:
            connection.close()
        except Error as e:
            print(f"[DB_HANDLER ОШИБКА]: Ошибка при закрытии соединения: {e}")