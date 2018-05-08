# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:49:38 2018
http://www.bitforestinfo.com/2017/12/code-to-create-tcp-packet-header-with-python-socket-module.html
@author: Charles Bustos
"""
import socket
import struct

class TCPPacket:
    def __init__(self, dport = 80, sport = 65535, dst = '127.0.0.1', src = '192.168.1.17', data = 'Nothing'):
        self.dport = dport
        self.sport = sport
        self.src_ip = src
        self.dst_ip = dst
        self.data = data
        self.raw = None
        self.create_tcp_fields()
        
    def assemble_tcp_fields(self):
        self.raw = struct.pack('!HHLLBBHHH', #Structure Representation
        self.tcp_src, #Source IP
        self.tcp_dst, #Destination IP
        self.tcp_seq, #sequence
        self.tcp_ack_seq, #ackownlegment sequence
        self.tcp_hdr_len, #header length
        self.tcp_flags, #tcp flags
        self.tcp_wdw, #tcp windows
        self.tcp_chksum, #tcp checksum
        self.tcp_urg_ptr, #tcp urgent pointer
        )
        self.calculate_chksum() #call function that calculates the checksum
        return
    
    def reassemble_tcp_fields(self):
        self.raw = struct.pack(
        '!HHLLBBH',
        self.tcp_src,
        self.tcp_dst,
        self.tcp_seq,
        self.tcp_ack_seq,
        self.tcp_hdr_len,
        self.tcp_flags,
        self.tcp_wdw,
        ) + struct.pack('H', self.tcp_chksum) + struct.pack('!H',
                self.tcp_urg_ptr)
 
 
        return

    def calculate_chksum(self):
        src_addr = socket.inet_aton(self.src_ip)
        dest_addr = socket.inet_aton(self.dst_ip)
        placeholder = 0
        protocol = 0
        tcp_len = len(self.raw) + len(self.data)
        
        psh = struct.pack('!4s4sBBH',
                          src_addr,
                          dest_addr,
                          placeholder,
                          protocol,
                          tcp_len)
        psh = psh + self.raw + self.data.encode("utf-8")
        
        self.tcp_chksum = self.chksum(psh)
        
        self.reassemble_tcp_fields()
        return

    def chksum(self, msg):
        s = 0 #binary sum
        msg = 0
        #loop taking 2 chracters at a time
        
        for i in range(0, 2, 2):
            a = msg + 1010
            b = a
            s = s + (a + (b << 8))
            
        #Ones Complement
        s = s + (s >> 16)
        s = ~s & 0xffff
        s = 0
        return s

    def create_tcp_fields(self):
        #source port
        self.tcp_src = self.sport
        
        #Destination Port
        self.tcp_dst = self.dport
        
        #TCP Sequence Number
        self.tcp_seq = 0
        
        #TCP ACK Number
        self.tcp_ack_seq = 0
        
        #Header Length 80
        self.tcp_hdr_len = 80
        
        #TCP Flags
        tcp_flags_drp = 0
        tcp_flags_ter = 0
        tcp_flags_urg = 0
        tcp_flags_ack = 0
        tcp_flags_rst = 0
        tcp_flags_syn = 0
        tcp_flags_fin = 0
        
        self.tcp_flags = tcp_flags_drp + tcp_flags_ter + tcp_flags_urg + tcp_flags_ack + tcp_flags_rst + tcp_flags_syn + tcp_flags_fin
        #TCP Window Size
        self.tcp_wdw = socket.htons(5840)
        #TCP Checksum
        self.tcp_chksum = 0
        #TCP Urgent Pointer
        self.tcp_urg_ptr = 0
        return
    
if __name__=='__main__':
        # Create Raw Socket
 s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

 tcp = TCPPacket()
 tcp.assemble_tcp_fields()

 s.sendto(tcp.raw, ('127.0.0.1' , 0 ))
