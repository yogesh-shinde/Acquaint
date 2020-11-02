from django.urls import path, include
from .views import *

urlpatterns = [
    path('view_category/', Category_View.as_view(), name='view'),
    path('add_category/', Category_Create.as_view(), name='create-category'),
    path('update_category/<int:id>/', Category_Update.as_view(), name='update'),
    path('delete_category/<int:id>/', Category_Delete.as_view(), name='delete'),

    path('view_subcategory/', Subcategory_View.as_view(), name='view'),
    path('add_subcategory/', Subcategory_Create.as_view(),
         name='create-subcategory'),
    path('update_subcategory/<int:id>/',
         Subcategory_Update.as_view(), name='update'),
    path('delete_subcategory/<int:id>/',
         Subcategory_Delete.as_view(), name='delete'),

    path('view_product/', Product_View.as_view(), name='view'),
    path('add_product/', Product_Create.as_view(), name='create-product'),
    path('update_product/<int:id>/', Product_Update.as_view(), name='update'),
    path('delete_product/<int:id>/', Product_Delete.as_view(), name='delete'),


]
