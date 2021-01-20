import json
import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase


class AuthorizationTest(TestCase):
    def test_without_the_correct_token_you_will_get_a_403_error(self):
        response = self.client.post(
            "",
            data=open(
                os.path.abspath(os.path.dirname(__file__))
                + "/images/the_Great_Spirit.jpg",
                "rb",
            ).read(),
            content_type="binary/octet-stream",
            HTTP_CONTENT_DISPOSITION="attachment; filename=the_Great_Spirit.jpg",
            Authorization="Bearer: invalid token",
        )

        self.assertEqual(response.status_code, 403)


class ImageUploadTest(TestCase):
    def test_image_upload_in_multipart_form_data_and_getting_the_response_in_json(self):
        file = SimpleUploadedFile(
            name="Spirit.jpg",
            content=open(
                os.path.abspath(os.path.dirname(__file__)) + "/images/Spirit.jpg", "rb"
            ).read(),
            content_type="image/jpg",
        )
        payload = {"file": file}
        response = self.client.post(
            "",
            payload,
            Authorization=f"Bearer: {settings.TOKEN}",
        )

        self.assertEqual(response.status_code, 201)

        json_file = open(
            os.path.abspath(os.path.dirname(__file__)) + "/image_annotations.json"
        ).read()

        parsed = json.loads(response.content.decode())

        self.assertEqual(json_file, json.dumps(parsed, indent=2))

    def test_image_upload_in_binary_octet_stream_and_getting_the_response_in_json(self):

        response = self.client.post(
            "",
            data=open(
                os.path.abspath(os.path.dirname(__file__))
                + "/images/the_Great_Spirit.jpg",
                "rb",
            ).read(),
            content_type="binary/octet-stream",
            HTTP_CONTENT_DISPOSITION="attachment; filename=the_Great_Spirit.jpg",
            Authorization=f"Bearer: {settings.TOKEN}",
        )

        self.assertEqual(response.status_code, 201)

        json_file = open(
            os.path.abspath(os.path.dirname(__file__)) + "/image_annotations.json"
        ).read()

        parsed = json.loads(response.content.decode())

        self.assertEqual(json_file, json.dumps(parsed, indent=2))
