from django.db import models

class Film(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    review = models.TextField('Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title