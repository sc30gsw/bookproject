from secrets import choice
from unicodedata import category
from django.db import models

# カテゴリーを管理するタプル
CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class Book(models.Model):
  """本の情報を管理するModelクラス

  Args:
      models (_type_): models.Model
  """
  # タイトル
  title = models.CharField(max_length=100)
  # 説明
  text = models.TextField()
  # カテゴリー
  category = models.CharField(
    max_length=100,
    choices=CATEGORY
  )
  
  def __str__(self) -> str:
    """管理画面で表示するBookモデルの見出しをタイトルにする

    Returns:
        str: タイトル
    """
    return self.title
