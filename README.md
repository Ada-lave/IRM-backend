# Вводная часть
Проект разрабатывается для проведения тестирования сотрудников компании.

# Запуск с помощью Docker
## Сборка образа
для первоначальной сборки проекта запустите команду
```sh
docker build -t irm_backend:latest .
```

## Запуск образа
```sh
docker run -p 8000:8000 --name IRM -d irm_backend:latest
```

## Последующие запуски
```sh
docker start IRM
```

# API
## Тесты
<details>
<summary><code>GET</code> <code>/api/v1/tests/{id}</code> <code>Возвращает все доступные тесты</code></summary>

### Параметры
|Name     | required       | Type                |
|---------|----------------|---------------------|
|id       |true            | int(query)          |

### Ответ
|Code| Content-Type   | Response            |
|----|----------------|---------------------|
|200 |application/json|```json```           |

### Структура ответа

> Code 200
```json
{
    "title": "string",
    "theme": "int",
    "questions": [
        {
            "title": "string",
            "test": "int",
            "answers": [
                {
                    "title": "string",
                    "is_right": "boolean!"
                }
            ]
        }
    ]
}
```
</details>

## Система авторизации
<details>
<summary><code>POST</code> <code>/auth/token/login</code> <code>Возращает токен авторизации</code></summary>

### Параметры
|Name     | required       | Type                |
|---------|----------------|---------------------|
|username |true            | string              |
|password |true            | string              |

### Ответ
|Code| Content-Type   | Response            |
|----|----------------|---------------------|
|200 |application/json|```json```           |
|400 |application/json|```json```           |

### Структура ответа

> Code 200
```json
{
    "auth_token": "string"
}
```

> Code 400
```json
{
    "non_field_errors": [
        "Невозможно войти с предоставленными учетными данными."
    ]
}
```
</details>

<details>
<summary><code>POST</code> <code>/api/v1/auth/users/</code> <code>Регистрирует пользователя</code></summary>

### Параметры
|Name     | required       | Type                |
|---------|----------------|---------------------|
|username |true            | string              |
|password |true            | string              |

### Ответ
|Code| Content-Type   | Response            |
|----|----------------|---------------------|
|200 |application/json|```json```           |
|400 |application/json|```json```           |

### Структура ответа

> Code 200
```json
{
    "email": "string",
    "username": "string",
    "id": "int"
}
```

> Code 400
```json
{
    "password": [
        "Введённый пароль слишком похож на имя пользователя.",
        "Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.",
        "Введённый пароль слишком широко распространён."
    ]
}
```
</details>

## Темы
<details>
<summary><code>GET</code> <code>/api/v1/themes/</code> <code>Отдает все темы</code></summary>

### Параметры
*Не требует*

### Ответ
|Code| Content-Type   | Response            |
|----|----------------|---------------------|
|200 |application/json|```json```           |

### Структура ответа
```json
{
    [
        {
            "title": "string",
            "attachments": [
                {
                    "id": "int",
                    "name": "string",
                    "path": "string:path_like",
                    "theme": "int",
                    "file_type": "int"
                }
            ]
        },
        {
            "title": "string",
            "attachments": [
                {
                    "id": "int",
                    "name": "string",
                    "path": "string:path_like",
                    "theme": "int",
                    "file_type": "int"
                }
            ]
        }
    ]
}
```
</details>

<details>
<summary><code>GET</code> <code>/api/v1/themes/{id}</code> <code>Отдает тему по id</code></summary>

### Параметры
|Name     | required       | Type                |
|---------|----------------|---------------------|
|id       |true            | int(query)          |

### Ответ
|Code| Content-Type   | Response            |
|----|----------------|---------------------|
|200 |application/json|```json```           |
|404 |application/json|```json```           |

### Структура ответа
> Code 200
```json   
{
    "title": "string",
    "attachments": [
        {
            "id": "int",
            "name": "string",
            "path": "string:path_like",
            "theme": "int",
            "file_type": "int"
        }
    ]
}
```

>Code 404
```json
{
    "detail": "data not found"
}
```
</details>