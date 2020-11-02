from django.shortcuts import render, redirect, HttpResponse
from .models import Owner
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Create your views here.


class Owner_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'owner_list.html'

    def get(self, request):
        owners = Owner.objects.all()
        # serializer = CategorySerializer(employee, many=True)
        return Response({'owners': owners})


class Owner_Register(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'owner_register.html'

    def get(self, request):
        serializer = OwnerSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/owner/login/')


class Owner_Login(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'owner_login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            try:
                user = Owner.objects.get(
                    owner_username__exact=username, owner_password__exact=password)
            except AttributeError:
                return Response('User Not Present')

            if user is not None:
                return redirect('/product/add_product/')
        else:
            return redirect('/owner/login/')
