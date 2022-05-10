from django.db import models
from django.urls import reverse


class Category(models.Model):
    """atribute for Note"""
    title = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    owner = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories_page', kwargs={'category_slug': self.slug})


class Teg(models.Model):
    """teg for Note"""
    title = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Tegs'

    def __str__(self):
        return self.title


class Post(models.Model):
    """ information for theme"""
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    teg = models.ManyToManyField(Teg)
    slug = models.SlugField(db_index=True, verbose_name="URL", max_length=50, unique=True, )
    image = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['title', 'date_update']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:200]}..."
        else:
            return f"{self.text[:200]}"

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
