from django.contrib import admin
from .models import Book

# 管理画面にBookModelを追加
admin.site.register(Book)