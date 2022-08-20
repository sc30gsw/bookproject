from django.urls import path

from . import views

urlpatterns = [
  # Book一覧画面のルーティング
  path('book/', views.ListBookView.as_view()),
  # Book詳細画面のルーティング
  path('book/<int:pk>/detail/', views.DetailBookView.as_view()),
]