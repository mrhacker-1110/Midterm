from django.db import models

class Contact(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    photo = models.ImageField(upload_to='contacts/', blank=True, null=True, verbose_name='Фото')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'