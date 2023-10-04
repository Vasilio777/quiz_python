from question_model import Question
import random 

class QuizController():
    def __init__(self, questions):
        self.questions = self.init_questions(questions)
        self.curr_q = 0
        self.score = 0
        self.questions_amount = 2

    def init_questions(self, data):
        """[{"text", "answer"}]"""

        questions = data.data["results"]
        q_arr = []
        for i in questions:
            q_text = self.html_decode(i["question"])
            q = Question(q_text, i["correct_answer"])
            q_arr.append(q)
        
        return q_arr

    def html_decode(self, s):
        """
        Returns the ASCII decoded version of the given HTML string. This does
        NOT remove normal HTML tags like <p>.
        """
        htmlCodes = (
                ("'", '&#039;'),
                ('"', '&quot;'),
                ('>', '&gt;'),
                ('<', '&lt;'),
                ('&', '&amp;')
            )
        for code in htmlCodes:
            s = s.replace(code[1], code[0])
        return s

    def begin(self):
        print("Hello there. Let's get started.", end='\n\n')

    def ask_question(self):
        """ask_question"""
        self.curr_q += 1

        q = random.choice(self.questions)
        self.questions.remove(q)
        inp = input(f'Q{self.curr_q}. {q.text} (True or False?): \n')
        self.check_answer(inp, q.answer)

    def check_answer(self, inp, answer):
        if inp.lower() == answer.lower():
            self.score += 1
            print('Correct.')
        else:
            print('Wrong. Ha-ha.')
        print(f'The correct answer was: {answer}')
        print(f'Your current score is: {self.score}/{self.curr_q}', end='\n\n')

    def has_more_questions(self) -> bool:
        return self.curr_q < self.questions_amount

    def end_play(self):
        print('Therefore, it was no so bad.')
        print(f'You have {self.score} points in total. Live with it. Bye. Beep-boop.')
