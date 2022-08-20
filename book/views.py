from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class ListBookView(ListView):
  """一覧画面に遷移するためのクラス

  Args:
      ListView (_type_): ListView
  """
  template_name = 'book/book_list.html'
  model = Book
  context_object_name = 'book_list'
