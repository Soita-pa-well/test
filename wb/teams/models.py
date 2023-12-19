from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название команды')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Имя члена команды')
    second_name = models.CharField(max_length=100,
                                   verbose_name='Фамилия')
    image = models.ImageField('Фото участника',
                              null=True)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             verbose_name='Название команды',
                             related_name='members')
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# /Users/Panisher/Desktop/wb_tech/test/wb/media/media/2.jpeg
# /Users/Panisher/Desktop/wb_tech/test/wb/media