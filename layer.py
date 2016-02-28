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

        # make sure basic questions have been answered.
        response = usr.askBasicQuestions(usrMsg)
        if response['basicDone'] != True:
            self.respond(messageProtocolEntity, response['botMsg'])
            return
        else:
            print "basic is done."
            self.respond(messageProtocolEntity, "basic is done")



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





