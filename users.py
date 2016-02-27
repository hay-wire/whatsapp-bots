__author__ = 'haywire'
import re

stringRegexp = re.compile(r'\w+')
anythingRegexp = re.compile(r'.+')

def validateString(s):
    return stringRegexp.match(s)

def validateAddress(s):
    if len(s) > 10:
        return anythingRegexp.match(s)
    return None

# def validateDate(dateStr):
#     if dateStr == 'today'

class User():
    name = 'Honey'
    email = ''
    address = ''

    basicQuestions = [
        'What shall I call you honey? (Your sweet name please :)',
        'Ok {name}! What\'s your internet address? (Email Id!)',
        'And where do you live on the earth? (Your address! Please type in one line only)'
    ]
    basicAnswerHints = [
        validateString,
        validateString,
        validateString
    ]
    basicAnswers = [
        'Honey',
        '',
        ''
    ]
    basicQuestionsAnswered = False
    basicQuestionState = -1

    # def getNextBasicQuestion(self):
    #     # if not at the last question, increment the state
    #     print "1. basic question state: ", self.basicQuestionState
    #     if self.basicQuestionState < len(self.basicQuestions):
    #         self.basicQuestionState += 1
    #     print "2. basic question state: ", self.basicQuestionState
    #     qstn = self.basicQuestions[self.basicQuestionState]
    #     return qstn

    def getNextBasicQuestion(self):
        if self.basicQuestionState == -1:
            self.basicQuestionState = 0
        return self.basicQuestions[self.basicQuestionState]

    def validateAndSaveBasicAnswer(self, ansr):
        # validate the answer for the question at current basicQuestionState
        answer = (self.basicAnswerHints[self.basicQuestionState])(ansr)
        if answer != None:
            # its a valid answer. save it. in basicAnswers
            self.basicAnswers[self.basicQuestionState] = ansr
            if self.basicQuestionState == len(self.basicQuestions) - 1:
                self.basicQuestionsAnswered = True
            else :
                self.basicQuestionState += 1
        return answer != None


    def setBasicQuestionsAnswered(self, state):
        self.basicQuestionsAnswered = state






