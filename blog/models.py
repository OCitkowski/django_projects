from django.db import models


class Category(models.Model):
    """atribute for Note"""
    title = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

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
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True,)
    image = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'date_update']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"