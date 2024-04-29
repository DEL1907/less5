from django.db import models


class Disease(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'

    def __str__(self) -> str:
        return self.name
# Create your models here.


class Patient(models.Model):
    name2 = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self) -> str:
        return self.name2