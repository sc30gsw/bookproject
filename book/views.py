from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class ListBookView(ListView):
  """一覧画面のビュー

  Args:
      ListView (_type_): ListView
  """
  template_name = 'book/book_list.html'
  model = Book
  context_object_name = 'book_list'

class DetailBookView(DetailView):
  """詳細画面のビュー

  Args:
      DetailView (_type_): DetailView
  """
  template_name: str = 'book/book_detail.html'
  model = Book
  context_object_name = 'book'