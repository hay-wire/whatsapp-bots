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

    #----------------------------------------------------------------
    def askBasicQuestions(self, usrMsg):
        botMsg = None
        if self.basicQuestionsAnswered == False:
            correctlyAnswered = False
            if self.basicQuestionState > -1:
                # he has answered last question. Evaluate and save this guy's answer.
                correctlyAnswered = self.validateAndSaveBasicAnswer(usrMsg)
            if correctlyAnswered == True or (self.basicQuestionState == -1 and correctlyAnswered == False):
                print "right basic answer."
                #check again if usrMsg completed the basic questions set?
                if self.basicQuestionsAnswered == False:
                    # some last basic question is still missing. ask next one
                    print "moving on to next basic question."
                    botMsg = self.getNextBasicQuestion()
                    print "OUTGOING: asking next question: ", botMsg
                    #self.respond(messageProtocolEntity, botMsg)
                    #return ret
                else:
                    # all basic questions answered. fall through to pickup questions
                    print "done with basic questions."
            else:
                #oops that was a wrong answer. shall we ask again?
                print "wrong basic answer. Asking same question again"
                botMsg = "Sorry! Invalid answer. Please try answering again. "+self.getNextBasicQuestion()
                print "OUTGOING: ", botMsg
                #self.respond(messageProtocolEntity, botMsg)
                #return
        # else self.basicQuestionsAnswered is True

        return {
            'botMsg': botMsg,
            'basicDone': self.basicQuestionsAnswered
        }



