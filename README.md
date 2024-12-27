# Интернет-магазин

Backend часть для интернет-магазина. В магазине существует около 100 товарных позиций товаров. Пользователь должен иметь возможность авторизоваться, посмотреть каталог товаров, добавить товар в корзину и купить его.


<p align="center">
  <img src="./docs/logo.png" width="250" height="250" alt="logo"/>
</p>

## Запуск проекта
1. Выполните клонирование проекта `git clone https://github.com/Wh4tisl0ve/Internet_Shop_DRF.git`
2. Выполните установку Docker
3. Создайте .env файл и заполните переменные окружения  
4. Выполните сборку Docker-image `docker build -t ***** -f .\Dockerfile.dev .`
5. Выполните команду `docker-compose -f ****** up -d --build`  

## Описание эндпоинтов
* `Get` -> `/products` -> Получение товаров по категории. `query_string` для фильтрации - category_id, min_price, max_price.  

Пример ответа:
```
[
    {
        "id": 1,
        "name": "Product name",
        "description": "Product desription",
        "image": "http://127.0.0.1:8000/media/products/images/example_36aBTmX.jpg",
        "price": "24.43",
        "characteristics": "Water popular hundred major religious.",
        "category": {
            "id": 10,
            "name": "size",
            "description": null,
            "parent": null
        }
    },
    {
        "id": 2,
        "name": "Product name",
        "description": "Product desription",
        "image": "http://127.0.0.1:8000/media/products/images/example_36aBTmX.jpg",
        "price": "24.43",
        "characteristics": "Water popular hundred major religious.",
        "category": {
            "id": 10,
            "name": "size",
            "description": null,
            "parent": null
        }
    },
]
```
* `Get` -> `/product/1` -> Получение карточки конкретного товара  

Пример ответа:
```
{
    "id": 1,
    "name": "Product",
    "description": "Product desription",
    "image": "http://127.0.0.1:8000/media/products/images/example_36aBTmX.jpg",
    "price": "24.43",
    "characteristics": "Water popular hundred major religious.",
    "category": {
        "id": 10,
        "name": "size",
        "description": null,
        "parent": null
    }
}
```
* `GET` -> `/categories ` -> Возвращение списка категорий. У категорий может быть несколько уровней вложенности.  

Пример ответа:
```
[
    {
        "id": 1,
        "name": "Root Category",
        "description": null,
        "children": [
            {
                "id": 2,
                "name": "New Subcategory",
                "description": "This is a new subcategory",
                "children": []
            }
        ]
    },
    {
        "id": 2,
        "name": "New Subcategory",
        "description": "This is a new subcategory",
        "children": []
    }
]
```

## База данных(структура)
В качестве системы управления базами данных была выбрана PostgreSQL. 
Для управления объектами бд была использована Django ORM.
База данных содержит в себе * таблицы:
1. `` - таблица, содержащая информацию о.
2. `` - таблица, содержащая информацию о .
3. `` - таблица, содержащая информацию о.
4. `` - таблица, содержащая информацию о.
5. `` - таблица, содержащая информацию о.
6. `` - таблица, содержащая информацию о.
7. `` - таблица, содержащая информацию о.


## Тесты
В качестве фреймворка для тестирования был использован unittest.
Юнит тестами был покрыты основные эндпоинты приложения. 

## Стек 

* Python 3.12
* Poetry
* Django Rest Framework
* PostgreSQL
* Redis
* Unit test