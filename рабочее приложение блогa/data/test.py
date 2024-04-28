from requests import get, post, delete

print(get('http://localhost:5000/api/news').json()) #правильный

print(get('http://localhost:5000/api/news/999').json()) #ошибка: нет такого id
print(get('http://localhost:5000/api/news/dkdkk').json()) #ошибка: id передано строкой


print(post('http://localhost:5000/api/news',  #ошибка: не правильные ключи
           json={'ооааооа': 'Заголовок',
                 'лвлвлвл': 'Текст новости',
                 'лвлв': 1,
                 'влвллв': False}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())
print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/news/1').json())