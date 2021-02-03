from django.db import models


# from django.contrib.auth.models import User


class User(models.Model):
    """Пользователь"""

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField()
    karma = models.IntegerField(default=0)
    land = models.CharField(max_length=3, )
    date_of_registration = models.DateField()

    def __str__(self):
        return self.name


class Meta:
    verbose_name_plural = "Пользователь"


class Community(models.Model):
    """Сообщество"""
    name = models.SlugField(max_length=25, verbose_name="Имя сообщества")
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)
    adress = models.SlugField("адресс сервера")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Подписки"


class Subscribes(models.Model):
    """Подписки"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, )
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Подписки"


class Posts(models.Model):
    """Посты"""
    link = models.SlugField("Ссылка")
    hash = models.CharField(max_length=100)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Посты"


class Comments(models.Model):
    """Коментарии"""
    link = models.SlugField("Ссылка")
    hash = models.CharField(max_length=100)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Коментарии"


class AnswersOfInterviews(models.Model):
    """Ответы на опросы"""
    interview_id = models.IntegerField("id опроса ")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, )
    answer_number = models.IntegerField("Номер ответа")

    class Meta:
        verbose_name_plural = "Ответы на опросы"


class Likes(models.Model):
    """Лайки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
