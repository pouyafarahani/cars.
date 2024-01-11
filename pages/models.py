from django.db import models


class CarModel(models.Model):
    tag = models.CharField(max_length=7)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.tag}: {self.postal_code}'

    class Meta:
        verbose_name = 'Login users'
        verbose_name_plural = 'Login users'
