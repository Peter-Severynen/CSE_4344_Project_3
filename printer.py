import socket
import struct
import packet.py
#create a packet object for testing purposes
packet = Packet(80, 65535, '127.0.0.1', '192.168.1.17', 'Nothing')

def print_message_received():

    # TODO: Add file writing function at end
    print('Message Received is: ' + packet.data)
    print('Source Agent ID: ' + packet.tcp_src)
    print('Destination Agent ID: ' + packet.tcp_dst)
    print('Sequence Number: ' + packet.tcp_seq)
    print('Acknowledgement Number: ' + packet.tcp_ack_seq)
    print('Header Length: ' + packet.tcp_hdr_len)
    print('DRP: ' + packet.tcp_flags_drp)
    print('TER: ' + packet.tcp_flags_ter)
    print('URG: ' + packet.tcp_flags_urg)
    print('ACK: ' + packet.tcp_flags_ack)
    print('RST: ' + packet.tcp_flags_rst)
    print('SYN: ' + packet.tcp_flags_syn)
    print('FIN: ' + tcp_flags_fin)
    print('Receiver Window: ' + packet.tcp_wdw)
    print('Checksum: ' + packet.tcp_chksum)
    print('Urgent Pointer: ' + packet.tcp_urg_ptr)
    print('Data: ' + packet.tcp_data)


def print_message_sent():

    # TODO: Add file writing function at end
    print('Message sent is: ' + packet.data)
    print('Source Agent ID: ' + packet.tcp_src)
    print('Destination Agent ID: ' + packet.tcp_dst)
    print('Sequence Number: ' + packet.tcp_seq)
    print('Acknowledgement Number: ' + packet.tcp_ack_seq)
    print('Header Length: ' + packet.tcp_hdr_len)
    print('DRP: ' + packet.tcp_flags_drp)
    print('TER: ' + packet.tcp_flags_ter)
    print('URG: ' + packet.tcp_flags_urg)
    print('ACK: ' + packet.tcp_flags_ack)
    print('RST: ' + packet.tcp_flags_rst)
    print('SYN: ' + packet.tcp_flags_syn)
    print('FIN: ' + tcp_flags_fin)
    print('Receiver Window: ' + packet.tcp_wdw)
    print('Checksum: ' + packet.tcp_chksum)
    print('Urgent Pointer: ' + packet.tcp_urg_ptr)
    print('Data: ' + packet.tcp_data)


def file_writer():

    new_path = 'out.txt'
    new_file = open(new_path,'w')
    new_file.write(packet.data)
    new_file.close()