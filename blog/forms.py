from django import forms

from blog.models.posts import Article
from blog.models.categories import Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "description",
            "featured_image",
            "visibility",
            "publish_status",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
