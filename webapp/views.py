from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound

from webapp.models import Category, Product


def articles_list_view(request):
    pass
    articles = Article.objects.order_by("-updated_at")
    context = {"articles": articles}
    return render(request, "index.html", context)


def article_create_view(request):
    pass
    if request.method == "GET":
        sections = Section.objects.all()
        return render(request, "create_article.html", {"sections": sections})
    else:
        article = Article.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            author=request.POST.get("author"),
            section_id=request.POST.get("section_id")
        )
        return redirect("article_view", pk=article.pk)

        # url = reverse("article_view", kwargs={"pk": article.pk})
        # return HttpResponseRedirect(url)


def article_view(request, *args, pk, **kwargs):
    pass
    article = get_object_or_404(Article, id=pk)
    # try:
    #     article = Article.objects.get(id=pk)
    # except Article.DoesNotExist:
    #     return HttpResponseNotFound()
    #     raise Http404()
    return render(request, "article.html", {"article": article})