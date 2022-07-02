import unittest
import time
import requests
from main import get_doc_owner_name, add_new_doc, delete_doc
from ya_disk_api import YaUploader



class TestFunctions(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("2207 876234"), "Василий Гупкин")

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc("10304", "паспорт", "Кирилл","3"), "3")

    def test_delete_doc(self):
        self.assertEqual(delete_doc("10006"), ('10006', True))


class TestApi(unittest.TestCase):

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

    @unittest.expectedFailure
    def test_creating_a_folder_fail(self):
        d = YaUploader("")
        self.assertEqual(d.creating_a_folder(4), 201)

