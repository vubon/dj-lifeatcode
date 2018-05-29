from django.conf.urls import url
from blog.article_views import AllArticlesView, CreateNewArticleView

urlpatterns = [
    url(r'^all-articles/$', AllArticlesView.as_view(), name='all_articles'),
    url(r'^new-article/$', CreateNewArticleView.as_view(), name='new_article'),
]


