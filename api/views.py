from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class GetComponents(APIView):
    def get(self, request):
        data = Component.objects.all()
        print(data)
        serializers = ComponentSerializer(data, many=True)

        return Response({"status": "success", "data": serializers.data}, status=200)


class CreateComponents(APIView):
    def post(self, request):
        print(request.data)
        serializers = ComponentSerializer1(data=request.data)
        # print(serializers.data)÷
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        else:
            return Response(serializers.errors)


class UpdateComponents(APIView):
    def put(self, request):
        component = request.GET['component']
        update = Component.objects.get(id=component)
        serializer = ComponentSerializer(
            update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return serializer.errors


class DeleteComponents(APIView):
    def delete(self, request, pk):
        erase = Component.objects.get(pk=pk)
        erase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteComponents(APIView):
    def delete(self, request):
        component = request.GET['component']
        erase = Component.objects.get(id=component)
        erase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetComponentById(APIView):
    def get(self, request):
        component = request.GET['component']
        data = Component.objects.get(id=component)
        serializer = ComponentSerializer(data)
        return Response(serializer.data)
