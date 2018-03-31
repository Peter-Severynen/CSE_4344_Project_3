# sources:
#https://stackoverflow.com/questions/35988/c-like-structures-in-python

class Packet():
    def __init__(self, sourceID, destID, seqNO, ackNO, headerLen, DRP, TER, URG, ACK, RST, SYN, FIN, recWin, chksum, urgent, data):
        self.sourceID = sourceID
        self.destID = destID
        self.seqNO = seqNO
        self.ackNO = ackNO
        self.headerLen = headerLen
        self.DRP = DRP
        self.TER = TER
        self.URG = URG
        self.ACK = ACK
        self.RST = RST
        self.SYN = SYN
        self.FIN = FIN
        self.recWin = recWin
        self.chksum = chksum
        self.urgent = urgent
        self.data = data
