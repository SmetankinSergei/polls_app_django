from django.contrib import admin

from polls.models import Poll, Question, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    list_editable = ['subject', 'description']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'context', 'poll', 'is_start']
    list_editable = ['context', 'poll', 'is_start']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'context', 'question', 'next_question']
    list_editable = ['context', 'question', 'next_question']
