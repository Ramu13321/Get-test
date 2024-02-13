import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'  # Замените на URL, по которому нужно выполнить GET-запрос

response = requests.get(url)

if response.status_code == 200:  # Проверяем успешность запроса
    data = response.json()  # Получаем данные в формате JSON
    print(data)  # Выводим полученные данные
else:
    print('Ошибка при выполнении GET-запроса:', response.status_code)