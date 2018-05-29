from django.db import models
from django.db.models import Q, F, Value
from django.db.models.functions import Concat


class ArticleQuerySet(models.QuerySet):

    def article_filter_by_author(self, request_user):
        return self.filter(Q(writer=request_user)).annotate(
            author=Concat(F('writer__first_name'), Value(' '), F('writer__last_name')),
            category_name=F('category__name'),
            publish_date=F('timestamp')
        ).values(
            'title', 'category_name', 'author', 'publish_date'
        ).order_by('-timestamp')
