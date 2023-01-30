from django.conf import settings
from django.db import models

class Snippet(models.Model):

  title = models.CharField('title', max_length=128)
  code = models.TextField('code', blank=True)
  # 空文字とnullが混在している
  # description = models.TextField('description', blank=True)
  description = models.TextField('description', null=False, default="", blank=True)
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)
  
  created_at = models.DateTimeField("投稿日", auto_now_add=True)
  updated_at = models.DateTimeField("更新日", auto_now=True)

  def __str__(self) -> str:
    return self.title

  # djangoアプリケーションで定義したモデルのテーブル名は「アプリ名_クラス名」になるので、snippets_snippetになる
  # Metaクラスでdb_tableを設定すると、テーブル名が変更できる
  class Meta:
    db_table = 'snippets'
