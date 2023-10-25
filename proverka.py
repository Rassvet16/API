
import pandas as pd
from api import DatabaseAPI
api = DatabaseAPI()

# Создание таблицы
dataframe = pd.DataFrame({"id": [1, 2, 3], "Brand": ["Apple", "Samsung", "Huawei"]})
api.create_table(dataframe, "phone")

# data = api.read_sql("SELECT * FROM phone")
# print(data)
# # Удаление строк из таблицы
#
# api.delete_from_table("phone", "id = 3")
# data = api.read_sql("SELECT * FROM phone")
# print(data)
# Очистка таблицы
# api.truncate_table("phone")
#
# # Чтение данных из таблицы
# data = api.read_sql("SELECT * FROM phone")
# print(data)
#
# Запись данных в таблицу
# new_data = pd.DataFrame({"id": [4, 5], "Brand": ["Honor", "Nokia"]})
# api.insert_sql(new_data, "phone", mode="append")
# data = api.read_sql("SELECT * FROM phone")
# print(data)

# # Пример использования execute
# query = "SELECT * FROM phone"
# api.execute(query)
# print(api.execute(query))