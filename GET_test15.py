import requests

url = ' https://api.travelpayouts.com/v1/prices/cheap?origin=MOW&destination=HKT&depart_date=2016-11&return_date=2016-12&token=PutHereYourToken'  # Замените на URL, по которому нужно выполнить GET-запрос

response = requests.get(url)

if response.status_code == 200:  # Проверяем успешность запроса
    data = response.json()  # Получаем данные в формате JSON
    print(data)  # Выводим полученные данные
else:
    print('Ошибка при выполнении GET-запроса:', response.status_code)