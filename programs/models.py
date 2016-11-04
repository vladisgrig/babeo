from django.db import models

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(verbose_name="Программа действует")
    category = models.ForeignKey('Category')

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
