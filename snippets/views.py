from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from snippets.models import Snippet
from snippets.forms import SnippetForm

def top(request):

  snippets = Snippet.objects.all()
  context = {"snippets": snippets}
  
  # templateを返す
  return render(request, "snippets/top.html", context)

  # httpレスポンスを返す
  # return HttpResponse(b"Hello World")

# login_requiredはユーザーログインが必要なことを示すデコレータ
@login_required
def snippet_new(request):
  if request.method == 'POST':
    form = SnippetForm(request.POST)
    if form.is_valid():
      snippet = form.save(commit = False)
      snippet.created_by = request.user
      snippet.save()

      return redirect(snippet_detail, snippet_id = snippet.pk)
    
    else:
      form = SnippetForm()

    return render(request, "snippets/snippet_new.html", {'form': form})


  # return HttpResponse('スニペットの登録')

def snippet_edit(request):
  return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
  snippet = get_object_or_404(Snippet, pk = snippet_id)
  return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})

