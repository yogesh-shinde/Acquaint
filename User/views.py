from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Create your views here.


class User_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_list.html'

    def get(self, request):
        users = User.objects.all()
        # serializer = CategorySerializer(employee, many=True)
        return Response({'users': users})


class User_Register(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_register.html'

    def get(self, request):
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/user/login/')


class User_Login(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            try:
                user = User.objects.get(
                    user_username__exact=username, user_password__exact=password)
            except AttributeError:
                return Response('User Not Present')

            if user is not None:
                return redirect('/user/view/')
        else:
            return redirect('/user/login/')
