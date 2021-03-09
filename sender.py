from common import *


class sender:
    RTT = 20
    seqNum = 0
    ackNum = 0
    checkSum = None
    payload = ''

    
    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum. 
        '''

        return

    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side
        '''

        return
 
    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''
        seqNum = 0 if self.seqNum == 0 else 1

        return seqNum

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None
        '''
        print('this is sender-init')
        self.packet = None

        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.
        '''
        print('this is sender-timerInterupt')

        
        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        ''' 
        print('this is sender-output')
        self.seqNum = self.getNextSeqNum()
        self.ackNum = 0
        self.checkSum = checksumCalc(message.data) + self.seqNum + self.ackNum
        self.packet = Packet(self.seqNum, self.ackNum, self.checkSum, message.data)
        
        # call udtSend function with new packet
        self.networkSimulator.udtSend(self.entity, self.packet)

        # start the timer
        self.networkSimulator.startTimer(self.entity, self.RTT)

        return
 
    def input(self, packet):

        '''If the acknowlegement packet isn't corrupted or duplicate, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.

        In the case of duplicate or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.
        '''
        print('this is sender-input')
        self.seqNum = self.getNextSeqNum()

        checkSum = checksumCalc(packet.payload) + packet.ackNum + packet.seqNum

        if checkSum == packet.checksum:
            self.networkSimulator.stopTimer(self.entity)

        return 
