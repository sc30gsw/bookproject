from django.urls import path

from . import views

urlpatterns = [
  # Book一覧画面に遷移するURLと呼び出すクラスを指定
  path('book/', views.ListBookView.as_view()),
]