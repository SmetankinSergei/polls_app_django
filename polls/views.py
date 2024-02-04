from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render

from polls.constants import COMPLETED_SURVEY_MESSAGE
from polls.models import Poll, Question, Answer


def start_page(request):
    return render(request, 'polls/start_page.html', {'title': 'start page'})


def poll(request):
    is_start = request.GET.get('is_start')
    question_pk = request.GET.get('question')
    current_poll_pk = request.GET.get('poll_pk')
    current_poll = Poll.objects.get(pk=current_poll_pk)
    message = ''

    if question_pk:
        question = Question.objects.get(pk=question_pk)
        answers = Answer.objects.filter(question=question)
    elif is_start:
        question = Question.objects.filter(poll=current_poll_pk, is_start=True).first()
        answers = Answer.objects.filter(question=question)
    else:
        message = COMPLETED_SURVEY_MESSAGE
        question = None
        answers = None

    context = {
        'title': 'poll',
        'poll': current_poll,
        'question': question,
        'answers': answers,
        'message': message,
    }
    return render(request, 'polls/poll.html', context)
