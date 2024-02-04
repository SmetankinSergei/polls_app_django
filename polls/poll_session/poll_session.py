from django.db.models import F

from polls.models import Question, Answer, Poll


class PollSession:
    def __init__(self, poll):
        self.poll = poll
        self.questions = {}
        self.answers = {}

    def update_statistic(self, question_pk, answer_pk):
        if question_pk:
            self.questions[question_pk] = self.questions.get(question_pk, 0) + 1
        if answer_pk:
            self.answers[answer_pk] = self.answers.get(answer_pk, 0) + 1

    def get_question_statistics(self, question):
        percentage_poll_participants = 0
        if self.poll.participants and question.participants:
            percentage_poll_participants = int((100 / self.poll.participants) * question.participants)
        return {
            'poll_participants': self.poll.participants,
            'question_participants': question.participants,
            'percentage_poll_participants': percentage_poll_participants,
        }

    def get_poll_statistics(self):
        self.poll.participants = F('participants') + 1

        questions_to_update = [Question(pk=question_pk, participants=F('participants') + count)
                               for question_pk, count in self.questions.items()]

        answers_to_update = [Answer(pk=answer_pk, participants=F('participants') + count)
                             for answer_pk, count in self.answers.items()]

        poll_to_update = [self.poll]

        Poll.objects.bulk_update(poll_to_update, ['participants'])
        Question.objects.bulk_update(questions_to_update, ['participants'])
        Answer.objects.bulk_update(answers_to_update, ['participants'])

        return {'poll': self.poll,
                'questions': self.questions,
                'answers': self.answers}


session = None
