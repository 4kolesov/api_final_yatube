### API Yatube
REST API для Yatube. Документация: http://127.0.0.1:8000/redoc/.
Возможность пользоваться величайшей социальной сетью Yatube с помощью API.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:4kolesov/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В директории с файлом manage.py выполнить миграции:

```
python3 manage.py migrate
```

В директории с файлом manage.py запустить проект

```
python manage.py runserver
```

> GET Получение публикаций api/v1/posts/
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
Статус код ```200:```

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

> POST Создание публикации api/v1/posts/{post_id}/comments/
Добавление нового комментария к публикации. Анонимные запросы запрещены.
Статус код ```200:```

Запрос:
```
{
"text": "string"
}
```

Ответ сервера:
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```

Статус код ```404:```

```
{
"detail": "Страница не найдена."
}
```