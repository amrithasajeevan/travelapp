from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import  SafetyService

from rest_framework.permissions import IsAuthenticated, AllowAny



class SafetyInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        country_code = self.request.query_params.get('country_code')

        # Replace 'https://api.safetyprovider.com/' with the actual base URL
        safety_service = SafetyService(base_url='https://www.travel-advisory.info/api')

        country_safety_info = safety_service.get_safety_information(country_code)

        if country_safety_info is not None:
            response_data = {'country_safety_info': country_safety_info}
            return Response(response_data)
        else:
            return Response({'error': 'Unable to fetch safety information'}, status=500)
