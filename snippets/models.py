from django.conf import settings
from django.db import models


# モデルマネージャーのカスタマイズ
class  DraftSnippetManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(is_draft=True)

class Snippet(models.Model):

  title = models.CharField('title', max_length=128)
  code = models.TextField('code', blank=True)
  # 空文字とnullが混在している
  # description = models.TextField('description', blank=True)
  description = models.TextField('description', null=False, default="", blank=True)
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)
  
  created_at = models.DateTimeField("投稿日", auto_now_add=True)
  updated_at = models.DateTimeField("更新日", auto_now=True)

  is_draft = models.BooleanField(_('Draft'), default=True)

  objects = models.Manager
  draft = DraftSnippetManager()

  # djangoアプリケーションで定義したモデルのテーブル名は「アプリ名_クラス名」になるので、snippets_snippetになる
  # Metaクラスでdb_tableを設定すると、テーブル名が変更できる
  class Meta:
    db_table = 'snippets'

  def __str__(self) -> str:
    return f'{self.pk} {self.title}'

class Comment(models.Model):

  title = models.TextField('本文', blank=False)
  commented_to = models.ForeignKey(Snippet, verbose_name="スニペット", on_delete=models.CASCADE)

  class Meta:
    db_table = 'comments'

  def __str__(self) -> str:
    return f'{self.pk} {self.text}'

class Tag(models.Model):

  name = models.CharField('タグ名', max_length=32)
  # ManyToManyFieldはDjangoが自動でsnippetクラスとtagクラスの中間クラスを自動生成する
  snippets = models.ManyToManyField(Snippet, related_name="tags", related_query_name='tag')

  class Meta:
    db_table = 'tags'

  def __str__(self) -> str:
    return f'{self.pk} {self.name}'
