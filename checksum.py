# -*- coding: utf-8 -*-
"""
Source: http://www.bitforestinfo.com/2017/12/code-to-create-tcp-packet-header-with-python-socket-module.html
"""

def calculate_chksum(self):
  src_addr     = socket.inet_aton( self.src_ip )
  dest_addr    = socket.inet_aton( self.dst_ip )
  placeholder  = 0
  protocol     = socket.IPPROTO_TCP
  tcp_len      = len(self.raw) + len(self.data)
 
  psh = struct.pack('!4s4sBBH' , 
   src_addr ,    # Source Address  
   dest_addr ,   # Destination Address 
   placeholder , # Placeholder
   protocol ,    # Protocol 
   tcp_len       # Length of pseudo + Demo TCP header + Data 
   )

  psh = psh + self.raw + self.data

  self.tcp_chksum = self.chksum(psh) # call CheckSum calculation function
  
  self.reassemble_tcp_feilds()       # finally, reassemble all peice of information
  
  return 
