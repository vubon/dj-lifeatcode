from django import forms

from blog.models.posts import Article


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