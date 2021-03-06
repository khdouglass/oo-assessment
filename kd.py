class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return '(Student {} {} at {}.)'.format(self.first_name, 
                 self.last_name, self.address)


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return '({} {})'.format(self.question, self.correct_answer)

    def ask_and_evaluate(self):
        user_anwer = raw_input(self.question)
        if user_anwer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    questions = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '(Exam {})'.format(self.name)

    def add_question(self, question, correct_answer):
        self.questions.append(question)
        self.questions.append(correct_answer)

    def administer(self):
        correct_counter = 0
        for i in range(0, len(self.questions), 2):
            user_anwer = raw_input(self.questions[i])
            if user_anwer == self.questions[i + 1]:
                correct_counter += 1
        return (float(correct_counter) / (len(self.questions) / 2)) * 100       

class StudentExam(Exam):
    student_score = None

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def __repr__(self):
        return '(StudentExam {})'.format(self.name)

    def take_test(self):
        self.student_score = self.administer()
        print "Your score is {}".format(self.student_score)

# this is an outline/general idea of how I would set up the Quiz function
# inheriting from the Exam class and returning 1 or 0 based on the scores.
# Right now I am receiving an error that 'return' is outside the function,
# unfortunately I do not have time (before 9pm) to debug.
class Quiz(Exam):
    student_score = None

    def __init__(self, student):
        self.student = student

    def __repr__(self):
        return '(Quiz {})'.format(self.name)

    self.take_test()
    if self.student_score >= 50:
        return 1
    else:
        return 0


def example(exam_name, first_name, last_name, student_address):
    exam_name = Exam(exam_name)
    exam_name.add_question("What is the color of the sky? ", "blue")
    exam_name.add_question("How many days are in a year? ", 365)
    exam_name.add_question("Do dolphins live in the ocean? ", "yes")
    
    student_name = Student(first_name, last_name, student_address)

    student_exam = StudentExam(student_name, exam_name)

    student_exam.take_test()

example("midterm", "katy", "douglass", "1335 bay st")