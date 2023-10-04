import data
from quiz_brain import QuizController

game = QuizController(data)
game.begin()

while game.has_more_questions():
    game.ask_question()

game.end_play()
