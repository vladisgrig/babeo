from django.db import models

# Create your models here.
class Sertificate(models.Model):
    number = models.CharField(max_length = 16, verbose_name = "Код сертификата")
    program = models.ForeignKey('programs.Program')
    is_active = models.BooleanField(verbose_name="Купон использован", default=False)
    activation_date = models.DateTimeField(verbose_name="Дата активации", blank=True, null=True)
    user = models.ForeignKey('auth.User', blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.number)

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
