import unittest
import time
import requests
from parameterized import parameterized
from main import get_doc_owner_name
from ya_disk_api import YaUploader



class TestFunctions(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("10006"), "Аристарх Павлов")


class TestApi(unittest.TestCase):

    @classmethod
    def setUp(self):
        token = ""
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {token}"
        }
        params = {"path": "/test3", "force_async": True, "permanently": False}
        response = requests.delete(url, headers=headers, params=params)
        time.sleep(1)

    def test_creating_a_folder(self):
        d = YaUploader("")
        self.assertEqual(d.creating_a_folder("/test3"), 201)


