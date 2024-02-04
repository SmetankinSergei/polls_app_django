from django.shortcuts import render

from polls.constants import COMPLETED_SURVEY_MESSAGE, NEXT_QUESTION_MESSAGE, FIRST_QUESTION_MESSAGE
from polls.models import Poll, Question, Answer
from polls.poll_session import poll_session


def start_page(request):
    return render(request, 'polls/start_page.html', {'title': 'start page'})


def show_results(request):
    results = poll_session.session.get_poll_statistics()
    context = {
        'title': 'results',
        'results': results,
    }
    return render(request, 'polls/show_results.html', context)


def poll(request):
    current_poll_pk = request.GET.get('poll_pk')
    current_poll = Poll.objects.get(pk=current_poll_pk)
    if request.GET.get('is_start'):
        create_session(current_poll)
    session_data = handle_session_data(request)

    if session_data['next_question_pk']:
        message = NEXT_QUESTION_MESSAGE
        question = Question.objects.get(pk=session_data['next_question_pk'])
        answers = Answer.objects.filter(question=question)
    elif session_data['is_start']:
        message = FIRST_QUESTION_MESSAGE
        question = Question.objects.filter(poll=current_poll, is_start=True).first()
        answers = Answer.objects.filter(question=question)
    else:
        message = COMPLETED_SURVEY_MESSAGE
        question = None
        answers = None

    question_statistics = None
    if question:
        question_statistics = poll_session.session.get_question_statistics(question)

    context = {
        'title': 'poll',
        'poll': current_poll,
        'question': question,
        'answers': answers,
        'message': message,
        'statistics': question_statistics,
    }

    return render(request, 'polls/poll.html', context)


def create_session(current_poll):
    poll_session.session = poll_session.PollSession(current_poll)


def handle_session_data(request):
    session_data = {'question_pk': request.GET.get('question_pk'),
                    'answer_pk': request.GET.get('answer_pk'),
                    'is_start': request.GET.get('is_start'),
                    'next_question_pk': request.GET.get('next_question'),
                    }
    poll_session.session.update_statistic(session_data['question_pk'], session_data['answer_pk'])
    return session_data
