import json
import os
import tempfile

from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from task.api_for_image_annotation.backends import CustomAuthentication


class FileUploadView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        FileUploadParser,
    )

    def post(self, request):
        up_file = request.data["file"]

        # with open(
        #     os.path.abspath(os.path.dirname(__file__))
        #     + "/uploaded_images/"
        #     + up_file.name,
        #     "wb",
        # ) as destination:
        #     for chunk in up_file.chunks():
        #         destination.write(chunk)

        with tempfile.NamedTemporaryFile() as destination:
            for chunk in up_file.chunks():
                destination.write(chunk)

        with open(
            os.path.abspath(os.path.dirname(__file__)) + "/image_annotations.json"
        ) as json_file:
            data = json.load(json_file)
            return Response(data, status.HTTP_201_CREATED)
