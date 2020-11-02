from django.shortcuts import render, redirect, HttpResponse
from .models import Admin
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Create your views here.


class Admin_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_list.html'

    def get(self, request):
        admins = Admin.objects.all()
        return Response({'admins': admins})


class Admin_Register(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_register.html'

    def get(self, request):
        serializer = AdminSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/admin-gui/login/')


class Admin_Login(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            try:
                admin = Admin.objects.get(
                    admin_username__exact=username, admin_password__exact=password)
            except AttributeError:
                return Response('Admin Not Present')

            if admin is not None:
                return redirect('/product/add_category/')
        else:
            return redirect('/admin-gui/login/')
