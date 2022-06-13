from django.shortcuts import render

from .serializers import *
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class GetComponents1(APIView):
    def get(self, request):
        data = Component1.objects.all()
        print(data)
        serializers = ComponentSerializer2(data, many=True)
        print(serializers.data)

        return Response({"status": "success", "data": serializers.data}, status=200)


class CreateComponents1(APIView):
    def post(self, request):
        serializers = CreateComponentSerializer1(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        else:
            return Response(serializers.errors)


class UpdateComponents1(APIView):
    def put(self, request):
        component = request.GET['component']
        update = Component1.objects.get(id=component)
        serializers = CreateComponentSerializer1(
            update, data=request.data, partial=True)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return serializers.errors


class DeleteComponentsApi(APIView):
    def delete(self, request):
        component = request.GET['component']
        erase = Component1.objects.get(id=component)
        erase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetComponentId(APIView):
    def get(self, request):
        component = request.GET['component']
        data = Component1.objects.get(id=component)
        serializers = ComponentSerializer2(data)
        return Response(serializers.data)
