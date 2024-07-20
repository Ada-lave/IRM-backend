# Вводная часть
Проект разрабатывается для проведения тестирования сотрудников компании.

# API
## Тесты
<details>
<summary><code>GET</code> <code>/api/v1/tests/{id}</code> <code>Возвращает все доступные тесты</code></summary>

### Параметры
*Не требует*

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