from django.urls import path

from . import views

urlpatterns = [
  # Book一覧画面のルーティング
  path('book/', views.ListBookView.as_view(), name='list-book'),
  # Book詳細画面のルーティング
  path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
  # Book登録画面のルーティング
  path('book/create/', views.CreateBookView.as_view(), name='create-book'),
  # Book削除画面のルーティング
  path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
  # Book更新画面のルーティング
  path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
]