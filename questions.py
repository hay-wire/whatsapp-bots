__author__ = 'haywire'


class Questions():

    questionsAnswered = False
    questionsState = -1

    def __init__(self, qstns, ansrHints, ansrs):
        self.questions = qstns
        self.answerHints = ansrHints
        self.answers = ansrs

    def getNextQuestion(self):
        if self.questionsState == -1:
            self.questionsState = 0
        return self.questions[self.questionsState]


    def validateAndSaveAnswer(self, ansr):
        # validate the answer for the question at current questionsState
        answer = (self.answerHints[self.questionsState])(ansr)
        if answer != None:
            # its a valid answer. save it. in answers
            self.answers[self.questionsState] = ansr
            if self.questionsState == len(self.questions) - 1:
                self.questionsAnswered = True
            else :
                self.questionsState += 1
        return answer != None


    def setQuestionsAnsweredState(self, state):
        self.questionsAnswered = state

    #----------------------------------------------------------------
    def askQuestions(self, usrMsg):
        botMsg = None
        if self.questionsAnswered == False:
            correctlyAnswered = False
            if self.questionsState > -1:
                # he has answered last question. Evaluate and save this guy's answer.
                correctlyAnswered = self.validateAndSaveAnswer(usrMsg)
            if correctlyAnswered == True or (self.questionsState == -1 and correctlyAnswered == False):
                print "right basic answer."
                #check again if usrMsg completed the basic questions set?
                if self.questionsAnswered == False:
                    # some last basic question is still missing. ask next one
                    print "moving on to next basic question."
                    botMsg = self.getNextQuestion()
                    print "OUTGOING: asking next question: ", botMsg
                    #self.respond(messageProtocolEntity, botMsg)
                    #return ret
                else:
                    # all basic questions answered. fall through to pickup questions
                    print "done with basic questions."
            else:
                #oops that was a wrong answer. shall we ask again?
                print "wrong basic answer. Asking same question again"
                botMsg = "Sorry! Invalid answer. Please try answering again. "+self.getNextQuestion()
                print "OUTGOING: ", botMsg
                #self.respond(messageProtocolEntity, botMsg)
                #return
        # else self.questionsAnswered is True
        return {
            'botMsg': botMsg,
            'basicDone': self.questionsAnswered
        }

