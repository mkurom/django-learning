from django.shortcuts import render
from django.http import HttpResponse

def top(request):

  # templateを返す
  return render(request, "snippets/top.html")

  # httpレスポンスを返す
  # return HttpResponse(b"Hello World")

def snippet_new(request):
  return HttpResponse('スニペットの登録')

def snippet_edit(request):
  return HttpResponse('スニペットの編集')

def snippet_detail(request):
  return HttpResponse('スニペットの詳細閲覧')

