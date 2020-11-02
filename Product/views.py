from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Create your views here.

# Category


class Category_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cate_list.html'

    def get(self, request):
        category = Category.objects.all()
        # serializer = CategorySerializer(employee, many=True)
        return Response({'category': category})


class Category_Create(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cate_add.html'

    def get(self, request):
        serializer = CategorySerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/product/add_subcategory/')


class Category_Update(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(emp_id=id)
        except Category.DoesNotExist:
            return HttpResponse('Category id not found')

    def get(self, request, id):
        categoey = self.get_object(id)
        serializer = CategorySerializer(categoey)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Category_Delete(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(category_id=id)
        except Category.DoesNotExist:
            return HttpResponse('Category id not found')

    def get(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, id):
        category = self.get_object(id)
        category.delete()
        return HttpResponse('Category record is deleted!!!')

# Sub-Category


class Subcategory_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sub_list.html'

    def get(self, request):
        category = Subcategory.objects.all()
        # serializer = SubcategorySerializer(employee, many=True)
        return Response({'category': category})


class Subcategory_Create(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sub_add.html'

    def get(self, request):
        serializer = SubcategorySerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = SubcategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/admin-gui/view/')


class Subcategory_Update(APIView):

    def get_object(self, id):
        try:
            return Subcategory.objects.get(emp_id=id)
        except Subcategory.DoesNotExist:
            return HttpResponse('Subcategory id not found')

    def get(self, request, id):
        subcategoey = self.get_object(id)
        serializer = SubcategorySerializer(subcategoey)
        return Response(serializer.data)

    def put(self, request, id):
        subcategory = self.get_object(id)
        serializer = SubcategorySerializer(subcategory, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Subcategory_Delete(APIView):
    def get_object(self, id):
        try:
            return Subcategory.objects.get(subcategory_id=id)
        except Category.DoesNotExist:
            return HttpResponse('Subcategory id not found')

    def get(self, request, id):
        subcategory = self.get_object(id)
        serializer = SubcategorySerializer(subcategory)
        return Response(serializer.data)

    def delete(self, request, id):
        subcategory = self.get_object(id)
        subcategory.delete()
        return HttpResponse('SubCategory record is deleted!!!')


# Product

class Product_View(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'prod_list.html'

    def get(self, request):
        products = Product.objects.all()
        return Response({'products': products})


class Product_Create(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'prod_add.html'

    def get(self, request):
        serializer = ProductSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/product/view_product/')


class Product_Update(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(emp_id=id)
        except Product.DoesNotExist:
            return HttpResponse('Product id not found')

    def get(self, request, id):
        product = self.get_object(id)
        serializer = CategorySerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Product_Delete(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(product_id=id)
        except Product.DoesNotExist:
            return HttpResponse('Product id not found')

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return HttpResponse('Product record is deleted!!!')
