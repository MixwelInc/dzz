from django.db import models


class First(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.DateTimeField()
    film = models.CharField(verbose_name='Фильм', max_length=150)
    max = models.IntegerField(verbose_name='Количество мест')

    def __str__(self):
        return f'[{self.id}] {self.full_name}'


class Second(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Фамилия', max_length=150)
    tickets = models.IntegerField(verbose_name='Количество билетов', max_length=10000)
    fk = models.ForeignKey('First', on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.id}] {self.name}'

