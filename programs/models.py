from django.db import models

# Create your models here.

class Program(models.Model):
    code = models.CharField(max_length = 30, unique = True, verbose_name="Код акции")
    title = models.CharField(max_length = 100, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(verbose_name="Программа действует")

    def __str__(self):
        return "{0}: {1}".format(self.code, self.title)

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"
