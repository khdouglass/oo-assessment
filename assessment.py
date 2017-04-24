"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The first is encapsulation, meaning the data lives close to it's funcationality.
   The variables (attributes) and functions (methods) are assigned to a class and 
   can only be accessed through instances of that class. 

   The second is abstraction. This means the user does not need to know how a method 
   functions internally. Larger programs can be broken up into smaller pieces and
   organized to improve design and functionality. 

   The third is polymorphism. This refers to the interchangeability of components.
   For example, inherited class attributes can be changed for instances of that class. 


2. What is a class?

    A class is a type of thing in Python. There are many built in classes, such as
    lists and strings. It is also possible to build your own class with assigned 
    attributes (variables) and methods (functions in the class).

3. What is an instance attribute?
    
    A variable specifically assigned to an instance of a class. 

4. What is a method?

    A function defined inside of a class.

5. What is an instance in object orientation?

    An individual occurance of a class. It inherits attributes and methods from 
    it's parent class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is defined in a class and inherited by all instances of 
   that class. For example if there is a motorcyle class, we might create a
   class attibute "number_of_wheels" and assign the value to 2 because all instances of that class will
   have two wheels.

   An instance attribute is an attribute of a specific instance. For example, 
   creating a color attribute for a motorcyle instance and setting it to 'red'.


"""


# Parts 2 through 5:
# Create your classes and class methods

"""Part 2"""

class Student(object):
    """Student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return '(Student {} {} at {}.)'.format(self.first_name, 
                 self.last_name, self.address)


class Question(object):
    """ Question in an exam."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return '({} {})'.format(self.question, self.correct_answer)

    def ask_and_evaluate(self):
        """Show question to user and evaulate user answer"""

        user_anwer = raw_input(self.question + ">")
        return user_anwer == self.correct_answer


class Exam(object):
    """A test comprised of zero or more questions."""

    def __init__(self, name):
        self.name = name
        self.question_list = []

    def __repr__(self):
        return '(Exam {})'.format(self.name)

    def add_question(self, question, correct_answer):
        """Create question instance. Add to exam."""

        new_question = Question(question, correct_answer)
        self.question_list.append(new_question)

    def administer(self):
        """Administer exam's questions and returns user's score"""

        correct_counter = 0
        for question in self.question_list:
            if question.ask_and_evaluate():
                correct_counter += 1
        return float(correct_counter) / len(self.question_list) * 100       

class StudentExam(object):
    """An exam belonging to a particular student. Contains student's score."""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.student_score = None

    def __repr__(self):
        return '(StudentExam for {}, test: {}, score: {}.)'.format(self.student, 
                                                            self.exam, 
                                                            self.student_score)

    def take_test(self):
        """Administer exam and assign score"""

        self.student_score = self.exam.administer()

        print "Your score is {:.2f} percent".format(self.student_score)

class Quiz(Exam):
        """Quizzes for students.

    A quiz is like an exam, except that it is pass/fail.
    A quiz passes if more than 50% of the answers are correct.
    """
  
    def __repr__(self):
      return '(Quiz {})'.format(self.name)
    
    def administer(self):
        """Administer exam questions and return 1 or 0"""
        
        score = super(Quiz, self).administer()

        if score >= 0.5:
            return 1
        else:
            return 0

            
class StudentQuiz(object):
    """A quiz belonging to a particular student. Contains score for quiz."""

    def __init__(self, student, quiz):
        self.quiz = quiz
        self.student = student
        self.score = None

        def __repr__(self):

        template = "<StudentQuiz student: {}, exam: {}, score: {}>"

        return template.format(self.student.first_name + " " + self.student.last_name,
                               self.quiz.name,
                               self.score)
                                                            )

    def take_test(self):
        """Administer exam and return score"""

        self.student_score = self.quiz.administer()

        if self.student_score:
            print "You passed!"
        else:
            print "You failed."


def example():
    """Show usage of exam, questions, and student."""

    exam_name = Exam('midterm')

    exam_name.add_question("What is the color of the sky? ", "blue")

    exam_name.add_question("How many days are in a year? ", 365)

    exam_name.add_question("Do dolphins live in the ocean? ", "yes")
    
    student_name = Student("Joe", "Computer", "555 California Street")

    joe_midterm = StudentExam(student, exam)

    joe_midterm.take_test()
    








