from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer
from blog.models import User
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserViewSet(APIView):
#     def get(self, request):
#         data = User.objects.all()
#         data_serial = UserSerializer(data, many=True).data
#         return Response(data_serial)
#
#
# class UserDetail(APIView):
#     def get(self, request, pk):
#         user = get_object_or_404(User, id=pk)
#         data_serial = UserSerializer(user).data
#         print(UserSerializer(user).data)
#         return Response(data_serial)
# class UserViewSet(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class CreateUserApi(generics.CreateAPIView):
#     serializer_class = UserSerializer

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


