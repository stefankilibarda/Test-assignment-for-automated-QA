import unittest
import requests
import json


class TestCreate(unittest.TestCase):
    def test_create(self):
        api_url = "https://gorest.co.in/public/v2/users"

        data = json.dumps({'id': '2511', 'name': 'John Do', 'email': 'john.do@email.com', 'gender': 'male', 'status': 'active'})
        resp = requests.post(api_url, data)
        print(resp)


if __name__ == '__main__':
    unittest.main()


class TestUpdate(unittest.TestCase):

    def test_update(self):
        api_url = "https://gorest.co.in/public/v2/comments"

        data = json.dumps({'id': '1125', 'name': 'Dohn Jo', 'email': 'dohn.jo@email.com', 'gender': 'female', 'status': 'inactive'})
        resp = requests.put(api_url, data)
        print(resp)

if __name__ == "__main__":
    unittest.main()


class TestDelete(unittest.TestCase):

    def test_delete(self):
        api_url = "https://gorest.co.in/public/v2/todos"

        resp = requests.delete(api_url)
        print(resp)

if __name__ == "__main__":
    unittest.main()