import socket
import binascii
import struct

def parse_ethernet_header(data):
    dest_mac, src_mac, eth_type = struct.unpack('!6s6sH', data[:14])
    return {
        'dest_mac' : binascii.hexlify(dest_mac).decode(),
        'src_mac' : binascii.hexlify(src_mac).decode(),
        'type' : eth_type
    }, data[14:]

def parse_ip_header(data):
    ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    version_ihl = ip_header[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0xF) * 4
    protocol = ip_header[6]
    src_ip = socket.inet_ntoa(ip_header[8])
    dest_ip = socket.inet_ntoa(ip_header[9])
    return {
        'version' : version,
        'ihl' : ihl,
        'protocol' : protocol,
        'src_ip' : src_ip,
        'dest_ip' : dest_ip
    }, data[ihl:]

def parse_tcp_header(data):
    tcp_header = struct.unpack('!HHLLBBHHH', data[:20])
    src_port = tcp_header[0]
    dest_port = tcp_header[1]
    return {
        'src_port' : src_port,
        'dest_port' : dest_port
    }, data[20:]

def main():
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(socket.ETH_P_ALL))
    sock.bind(('labnet-br2', 0))
    
    print("Sniffing packets....")
    with open("capture.log", 'a') as log_file:
        while True:
            packet, _ = sock.recvfrom(65535)
            eth_header, eth_data = parse_ethernet_header(packet)
            if eth_header['type'] != 0x0800: #IPv4
                continue
            ip_header, ip_data = parse_ip_header(eth_data)
            if ip_header['protocol'] != 6: #TCP
                continue
            tcp_header, tcp_data = parse_tcp_header(ip_data)
            if tcp_header['dest_port'] in [80, 21] or tcp_header['src_port'] in [80, 21]:
                print(f"TCP Packet: {ip_header['src_ip']}:{tcp_header['src_port']} -> {ip_header['dest_ip']}:{tcp_header['dest_port']}")
                if tcp_data:
                    try:
                        payload = tcp_data.decode('utf-8', errors='ignore')
                        if 'GET' in payload or 'POST' in payload or 'USER' in payload:
                            print(f"Payload: {payload[:100]}...")
                            log_file.write(f"{ip_header['src_ip']}:{tcp_header['src_port']} -> " 
                                           f"{ip_header['dest_ip']}:{tcp_header['dest_port']}\n"
                                           f"Payload: {payload}\n\n")
                    except UnicodeDecodeError:
                        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped sniffing.")
