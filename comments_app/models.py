from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Article'

    def __str__(self):
        return self.name


class Comments(models.Model):
    text = models.TextField('текст коментария', max_length=500)
    parent = models.ForeignKey('self', verbose_name='Родитель',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name="children")
    article = models.ForeignKey(Article,
                                verbose_name='Статья',
                                on_delete=models.CASCADE,default='',
                                related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


