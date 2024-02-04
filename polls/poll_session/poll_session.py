class PollSession:
    def __init__(self, poll):
        self.poll = poll
        self.questions = {}
        self.answers = {}

    def update_statistic(self, question_pk, answer_pk):
        if question_pk:
            self.questions[question_pk] = self.questions.get(question_pk, 0) + 1
            print('questions: ', self.questions)
        if answer_pk:
            self.answers[answer_pk] = self.answers.get(answer_pk, 0) + 1
            print('answers: ', self.answers)


session = None
