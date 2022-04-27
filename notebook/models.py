from django.db import models


class StarsNote(models.Model):
    """Rating for note"""

    level = models.PositiveSmallIntegerField(max_length=1, default=0, verbose_name='level')

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'


class CategoryNote(models.Model):
    """Category for note"""

    name = models.CharField('Category', max_length=200)
    description = models.TextField(default='', verbose_name='Text')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class CommentsNote(models.Model):
    """Comments for note"""

    name = models.CharField('Name comment', max_length=200)
    image = models.ImageField('Image', upload_to=None, height_field=100, width_field=100, max_length=100)
    comment = models.TextField('Comment', default='')
    date_create = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Note(models.Model):
    """ Note """
    name = models.CharField('Name note', default='', max_length=200)
    stars = models.ForeignKey(StarsNote, on_delete=models.CASCADE)
    comment = models.ManyToManyField(CommentsNote)
    category = models.ManyToManyField(CategoryNote)

    text = models.TextField('Text', default='')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Image', upload_to=None, height_field=500, width_field=500)
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
