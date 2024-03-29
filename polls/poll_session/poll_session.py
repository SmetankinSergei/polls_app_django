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
        self.__update_database()

        # poll = Poll.objects.get(pk=self.poll.pk)
        poll = Poll.objects.raw(f"SELECT * FROM polls_poll WHERE id = {self.poll.pk}")[0]

        # questions = Question.objects.filter(poll=poll)
        questions = \
            Question.objects.raw(f'''SELECT * FROM "polls_question" WHERE "polls_question"."poll_id" = {poll.pk}''')
        questions_stat = []
        answers_stat = []
        for question in questions:
            questions_stat.append({'question': question,
                                   'percentage': self.__get_percentage(poll.participants, question.participants)})

            # answers = Answer.objects.filter(question=question.pk)
            answers = \
                Answer.objects.raw(f'''SELECT * FROM "polls_answer" WHERE "polls_answer"."question_id" = {question.pk}''')
            answer_list = []
            for answer in answers:
                answer_list.append({'answer': answer,
                                    'percentage': self.__get_percentage(poll.participants, answer.participants)})
            answers_stat.append(answer_list)

        return {'poll': poll,
                'questions_stat': questions_stat,
                'answers_stat': answers_stat}

    def get_questions_numbers(self):
        questions = Question.objects.filter(poll=self.poll).order_by('-participants')
        numbers = {}
        prev_question = None
        prev_number = 1
        for question in questions:
            if prev_question and question.participants == prev_question.participants:
                numbers[question.pk] = prev_number
            elif prev_question and question.participants != prev_question.participants:
                numbers[question.pk] = prev_number + 1
                prev_question = question
                prev_number += 1
            else:
                numbers[question.pk] = prev_number
                prev_question = question
        return numbers

    def __update_database(self):
        self.poll.participants = F('participants') + 1

        questions_to_update = [Question(pk=question_pk, participants=F('participants') + count)
                               for question_pk, count in self.questions.items()]

        answers_to_update = [Answer(pk=answer_pk, participants=F('participants') + count)
                             for answer_pk, count in self.answers.items()]

        poll_to_update = [self.poll]

        Poll.objects.bulk_update(poll_to_update, ['participants'])
        Question.objects.bulk_update(questions_to_update, ['participants'])
        Answer.objects.bulk_update(answers_to_update, ['participants'])

    @staticmethod
    def __get_percentage(poll_participants, item_participants):
        percentage = 0
        if poll_participants and item_participants:
            percentage = int((100 / poll_participants) * item_participants)
        return percentage


session = None
