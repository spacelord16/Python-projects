from http.client import responses


class AnonymousSurvey:
    """Collect anonymous answers to a survey questions"""

    def __init__(self, questions):
        """Store a question , and prepare store responses"""
        self.questions = question
        self.responses = []

    def show_question(self):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_result(self):
        print("Survey results:")
        for response in responses:
            print('-' + response)


question = "What language do you first learn to speak ?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q ' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!!!")
my_survey.show_results()
