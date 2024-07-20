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