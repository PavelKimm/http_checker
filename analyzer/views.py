import openpyxl

import requests
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
)

from analyzer.models import Website

START_ROW = 2


@api_view(['POST'])
def load_websites_to_check(request):
    """
    insertion of website urls to the database from .xlsx files
    """

    inserted_urls_count = 0
    passed_urls_count = 0

    xlsx_files = request.FILES.getlist('files')
    for xlsx_file in xlsx_files:
        try:
            wb_obj = openpyxl.load_workbook(xlsx_file)
        except Exception as e:
            return Response({"detail": str(e)}, status=HTTP_400_BAD_REQUEST)

        # if you need to get specific sheet
        # first_sheet = wb_obj.get_sheet_names()[0]
        # sheet = wb_obj.get_sheet_by_name(first_sheet)

        sheet = wb_obj.active

        for row in sheet.iter_rows(min_row=START_ROW, max_row=sheet.max_row):
            for cell in row:
                try:
                    Website.objects.create(url=cell.value.strip())
                    inserted_urls_count += 1
                except Exception as e:
                    # print(str(e))
                    passed_urls_count += 1

    return Response(f"The insertion has been completed. Inserted urls number: {inserted_urls_count}. "
                    f"Passed urls number: {passed_urls_count}", status=200)
