from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from blog.models.posts import Article
from blog.models.categories import Category
from blog.forms import ArticleForm, CategoryForm


class AllArticlesView(View):
    template = 'dashboard/article/all_articles.html'

    def get(self, request):
        """
        A request user all articles
        :param request:
        :return: a list or blank list if no article
        """
        articles = Article.objects.article_by_author(request.user)
        return render(request, self.template, {"all_articles": articles})


class CreateNewArticleView(View):
    template = 'dashboard/article/new_article.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
            "form": form,
        }

        return render(request, self.template, context)


class CreateCategory(View):
    template_name = 'dashboard/article/new_category.html'

    def get(self, request):
        categories = Category.objects.all().order_by("-timestamp")
        return render(request, self.template_name, {"categories": categories})

    def post(self, request):
        if not request.user.is_staff:
            raise Http404
        form = CategoryForm(request.POST)
        categories = Category.objects.all().order_by("-timestamp")

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
            return render(request, self.template_name, {"categories": categories})
        # message error
        messages.error(request, "Category with this Name already exists")
        return render(request, self.template_name, {"categories": categories})

    def delete(self, pk=None):
        pass

