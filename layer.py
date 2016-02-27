__author__ = 'haywire'

from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from users import User

usersList = {}

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        phone = (messageProtocolEntity.getFrom().split("@"))[0]
        usrMsg = messageProtocolEntity.getBody()
        print "INCOMING: ", phone ,": ", usrMsg

        # get this user's details
        usr = self.getUser(phone)
        if usr.basicQuestionsAnswered == False:
            correctlyAnswered = False
            if usr.basicQuestionState > -1:
                # he has answered last question. Evaluate and save this guy's answer.
                correctlyAnswered = usr.validateAndSaveBasicAnswer(usrMsg)
            if correctlyAnswered == True or (usr.basicQuestionState == -1 and correctlyAnswered == False):
                print "right basic answer."
                if usr.basicQuestionsAnswered == False:
                    # some last basic question is still missing. ask next one
                    print "moving on to next basic question."
                    botMsg = usr.getNextBasicQuestion()
                    print "OUTGOING: asking next question: ", botMsg
                    self.respond(messageProtocolEntity, botMsg)
                    return
                else:
                    # all basic questions answered. fall through to pickup questions
                    print "done with basic questions."
            else:
                #oops that was a wrong answer. shall we ask again?
                print "wrong basic answer. Asking same question again"
                botMsg = "Sorry! Invalid answer. Please try answering again. "+usr.getNextBasicQuestion()
                print "OUTGOING: ", botMsg
                self.respond(messageProtocolEntity, botMsg)
                return

        print "user has answered basic questions!"
        botMsg = "Congrats! You have answered all basic questions correctly!"
        print "OUTGOING: ", botMsg
        self.respond(messageProtocolEntity, botMsg)



        # usr.validateAndSaveAnswer()
        # # self.solveMsg(phone, msg)
        #
        # self.respond(messageProtocolEntity, msg)
        # # outgoingMessageProtocolEntity = TextMessageProtocolEntity(
        #     messageProtocolEntity.getBody(),
        #     to = messageProtocolEntity.getFrom())
        #
        # self.toLower(receipt)
        # self.toLower(outgoingMessageProtocolEntity)


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

    def getUser(self, phone):
        if phone in usersList:
            usr = usersList[phone]
        else :
            usr = usersList[phone] = User()
        return usr

    def respond(self, messageProtocolEntity, msg):
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())

        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            msg,
            to = messageProtocolEntity.getFrom())

        self.toLower(receipt)
        self.toLower(outgoingMessageProtocolEntity)





