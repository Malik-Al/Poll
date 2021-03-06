from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст')
    poll = models.ForeignKey('webapp.Poll', verbose_name='Опрос', on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', verbose_name='Опрос', on_delete=models.CASCADE, related_name='answers')
    choice = models.ForeignKey('webapp.Choice', verbose_name="Вариант ответа", on_delete=models.CASCADE,
                               related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return '{} - {} '.format(self.poll, self.choice)