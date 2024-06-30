from django.test import TestCase
from django.test import Client

from materials.models import Theme
from .models import Test, Answer, Question
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class TestTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.preare_full_test_for_test()

    def test_get_a_first_test(self):
        response = self.client.get("/api/v1/tests/1")
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "title": "Тест по теме тестов",
                "questions": [
                    {
                        "id": 1,
                        "title": "Вопрос 1",
                        "answers": [
                            {"id": 1, "title": "Ответ 1"},
                            {"id": 2, "title": "Ответ 2"},
                        ],
                    },
                    {
                        "id": 2,
                        "title": "Вопрос 2",
                        "answers": [{"id": 3, "title": "Ответ 1"}],
                    },
                ],
            },
        )

    def test_accept_test(self):
        User.objects.create_user(password="secretpass", username="user 1")
        self.client.login(username="user 1", password="secretpass")
        test_id = 1
        body = {
            "id": test_id,
            "title": "Тест по теме тестов",
            "questions": [
                {
                    "id": 1,
                    "title": "Вопрос 1",
                    "answers": [
                        {"id": 1, "title": "Ответ 1", "is_right": True},
                        {"id": 2, "title": "Ответ 2"},
                    ],
                },
                {
                    "id": 2,
                    "title": "Вопрос 2",
                    "answers": [{"id": 3, "title": "Ответ 1", "is_right": True}],
                },
            ],
        }

        response = self.client.post(
            f"/api/v1/tests/{test_id}/check/", body, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"id": 1, "score": 1, "total": 2, "user": 1, "test": 1}
        )

    def preare_full_test_for_test(self):
        theme = Theme.objects.create(title="Тестовая тема")
        test = Test.objects.create(title="Тест по теме тестов", theme=theme)
        question_1 = Question.objects.create(title="Вопрос 1", test=test)
        answer_1 = Answer.objects.create(
            title="Ответ 1", question=question_1, is_right=True
        )
        answer_1 = Answer.objects.create(title="Ответ 2", question=question_1)

        question_2 = Question.objects.create(title="Вопрос 2", test=test)
        answer_3 = Answer.objects.create(title="Ответ 1", question=question_2)
