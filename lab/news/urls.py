from django.urls import path
from .views import index, add, get, delete, update, updaterecord

urlpatterns = [
    path('news/', index, name='view_news'),
    path('news/add/', add, name="add"),
    path('news/<int:id>/', get, name='get'),
    path('news/<int:id>/del', delete, name='delete'),
    path('news/<int:id>/update', update, name='update'),
    path('news/<int:id>/updaterecord', updaterecord, name='updaterecord'),
]