from django.db import models
from django.db.models import CASCADE


NULLABLE = {'null': True, 'blank': True}


class Poll(models.Model):
    subject = models.CharField(max_length=500)
    description = models.TextField()
    participants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.subject}, {self.participants}'


class Question(models.Model):
    context = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=CASCADE)
    is_start = models.BooleanField(default=False)
    participants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.context


class Answer(models.Model):
    context = models.TextField()
    question = models.ForeignKey(Question, on_delete=CASCADE, related_name='current_question')
    next_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='next_question', **NULLABLE)
    participants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.context
