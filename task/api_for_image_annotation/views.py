import os

from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):
    parser_classes = (
        MultiPartParser,
        FileUploadParser,
    )

    def post(self, request, format="jpg"):
        up_file = request.data["file"]
        with open(
            os.path.abspath(os.path.dirname(__file__))
            + "/uploaded_images/"
            + up_file.name,
            "wb+",
        ) as destination:
            for chunk in up_file.chunks():
                destination.write(chunk)

        return Response(up_file.name, status.HTTP_201_CREATED)
