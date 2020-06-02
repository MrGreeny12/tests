import unittest
import requests

class YaTest(unittest.TestCase):

    #разбирали на вебинаре
    def test_smoke(self):
        responce = requests.get('http://yandex.ru/')
        self.assertEqual(responce.status_code, 200)
        data = responce.content
        self.assertNotEqual(data, '')

class YaTranslateTest(unittest.TestCase):

    def setUp(self) -> None:
        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {
            'key': API_KEY,
            'text': 'hello',
            'lang': 'en-ru'
        }

    def test_smoke(self):
        resp = requests.get(
            self.URL,
            params=self.params
        )
        self.assertEqual(resp.status_code, 200)
        json_ = resp.json()
        text =  json_['text']
        self.assertEqual(text[0], 'привет')