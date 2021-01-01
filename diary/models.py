from django.db import models
from mdeditor.fields import MDTextField
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class ArticleManager(models.Manager):
    def archive(self):
        archive_list = []
        date_list = self.values('date')
        for date in date_list:
            date = date['date'].strftime('%Y年%m月')
            if date not in archive_list:
                archive_list.append(date)
        return archive_list

class Article(models.Model):
    title = models.CharField(max_length=50,blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    date = models.DateField(default=date.today,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,blank=True, null=True)
    body = MDTextField()

    objects = ArticleManager()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

