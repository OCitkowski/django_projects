from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]


class Category(models.Model):
    """atribute for Note"""
    title = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=90, unique=True, db_index=True, verbose_name="URL")
    owner = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories_page', kwargs={'category_slug': self.slug})


class Tag(models.Model):
    """teg for Note"""
    objects = None
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=90, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags_page', kwargs={'tag_slug': self.slug})


class Post(models.Model):
    """ information for theme"""
    objects = None
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(db_index=True, verbose_name="URL", max_length=200, unique=True, )
    image = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['title', 'date_update']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_tegs(self):
        return "\n".join([p.title for p in self.tag.all()])

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:150]}..."
        else:
            return f"{self.text[:150]}"

    def get_absolute_url(self):
        return reverse("categories_page")


class Comment(models.Model):
    title = models.CharField(max_length=80)
    email = models.EmailField(max_length=250, blank=True)
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"


class Pub(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Art(models.Model):
    title = models.CharField(max_length=100)
    pub = models.ManyToManyField(Pub)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
