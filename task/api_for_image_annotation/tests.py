import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient


class MyTest(TestCase):
    client_class = APIClient

    def test_it(self):
        file = SimpleUploadedFile(
            name="Spirit.jpg",
            content=open(
                os.path.abspath(os.path.dirname(__file__)) + "/images/Spirit.jpg", "rb"
            ).read(),
            content_type="image/jpeg",
        )
        payload = {"file": file}
        response = self.client.post(
            "",
            payload,
        )

        self.assertEqual(response.status_code, 201)


class MyTest2(TestCase):
    client_class = APIClient

    def test_it(self):
        file = SimpleUploadedFile(
            name="the_Great_Spirit.jpg",
            content=open(
                os.path.abspath(os.path.dirname(__file__))
                + "/images/the_Great_Spirit.jpg",
                "rb",
            ).read(),
            content_type="image/jpeg",
        )
        payload = {"file": file}

        # headers = {
        #     "Content-type": "binary/octet-stream",
        #     "Content-Disposition": "attachment; filename=the_Great_Spirit.jpg",
        #     "filename": "the_Great_Spirit.jpg",
        # }

        # headers = {
        #     "Content-Type": "binary/octet-stream",
        #     "Content-Disposition": "attachment; filename=the_Great_Spirit.jpg"
        # }

        response = self.client.post(
            "?filename=the_Great_Spirit.jpg",
            payload,
            content_type="binary/octet-stream",
        )

        self.assertEqual(response.status_code, 201)
