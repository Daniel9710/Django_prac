from django.urls import path
from . import views

urlpatterns = [
    path('color/GET/<int:pk>', views.color_get, name='color_get'),
    path('color/PATCH/<int:pk>', views.color_patch, name='color_patch'),
    path('text/GET/<int:pk>', views.text_get, name='text_get'),
    path('text/PUT/<int:pk>', views.text_put, name='text_put'),
    path('text/PATCH/<int:pk>', views.text_patch, name='text_patch'),
    path('text/DELETE/<int:pk>', views.text_delete, name='text_delete'),
]