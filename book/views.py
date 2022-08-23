from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book

class ListBookView(ListView):
  """一覧画面のビュー

  Args:
      ListView (_type_): ListView
  """
  # HTMLファイル名
  template_name: str = 'book/book_list.html'
  # 使用するテーブル
  model = Book
  # テンプレートで使用するオブジェクト名
  context_object_name: str = 'book_list'

class DetailBookView(DetailView):
  """詳細画面のビュー

  Args:
      DetailView (_type_): DetailView
  """
  # HTMLファイル名
  template_name: str = 'book/book_detail.html'
  # 使用するテーブル
  model = Book
  # テンプレートで使用するオブジェクト名
  context_object_name: str = 'book'
  
class CreateBookView(CreateView):
  """登録画面のビュー

  Args:
      CreateView (_type_): CreateView
  """
  # HTMLファイル名
  template_name: str = 'book/book_create.html'
  # 使用するテーブル
  model = Book
  # フォームの子要素
  fields = ('title', 'text', 'category')
  # リダイレクト先
  success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
  """削除画面のビュー

  Args:
      DeleteView (_type_): DeleteView
  """
  # HTMLファイル名
  template_name: str = 'book/book_confirm_delete.html'
  # 使用するテーブル
  model = Book
  # リダイレクト先
  success_url = reverse_lazy('list-book')
  # テンプレートで使用するオブジェクト名
  context_object_name: str = 'book'

class UpdateBookView(UpdateView):
  """更新画面のビュー

  Args:
      UpdateView (_type_): UpdateView
  """
  # HTMLファイル名
  template_name: str = 'book/book_update.html'
  # 使用するテーブル
  model = Book
  # フォームの子要素
  fields = ('title', 'text', 'category')
  # リダイレクト先
  success_url = reverse_lazy('list-book')