from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from account.models import Author
from blog.models.categories import Category

from blog.models.post_queryset import ArticleQuerySet

from django.utils.text import slugify


class ArticleManager(models.Manager):

    def get_queryset(self):
        """
        Initialize queryset
        :return:
        """
        return ArticleQuerySet(self.model, using=self._db)

    def article_by_author(self, request_user):
        """

        :param request_user:
        :return: article list of request user
        """
        return self.get_queryset().article_filter_by_author(request_user)


class Article(models.Model):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
    PUBLISH_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'
    VISIBILITY_STATUS = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private')
    )

    writer = models.ForeignKey(Author)
    title = models.CharField(max_length=200, default='---')
    slug = models.SlugField(unique=True)
    description = RichTextField()
    category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField()
    reading_times = models.IntegerField(default=0)
    updated_at = models.DateTimeField(null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    publish_status = models.CharField(max_length=20, choices=PUBLISH_STATUS, default=DRAFT)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_STATUS, default=PUBLIC)
    featured_image = models.ImageField(upload_to='article/', height_field='height_field', width_field='width_field',
                                       null=True, blank=True)

    objects = ArticleManager()

    def category_name(self):
        """
        Many to many field does not show directly in list display.
        This method are helping display the category name of the article.
        :return: name of the category in admin list display
        """
        return "\n".join([p.name for p in self.category.all()])

    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.title)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
