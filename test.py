# from zeroconf import ServiceBrowser, Zeroconf


# from zeroconf import ServiceBrowser, Zeroconf


# class MyListener:

#     def remove_service(self, zeroconf, type, name):
#         print("Service %s removed" % (name,))

#     def add_service(self, zeroconf, type, name):
#         info = zeroconf.get_service_info(type, name)
#         print("Service %s added, service info: %s" % (name, info))


# zeroconf = Zeroconf()
# listener = MyListener()
# browser = ServiceBrowser(zeroconf, "_arduino._tcp.local.", listener)
# print(browser)
# try:
#     input("Press enter to exit...\n\n")
# finally:
#     zeroconf.close()

# import socket
# import struct
# import dpkt, dpkt.dns
# UDP_IP="0.0.0.0"
# UDP_PORT=5353
# MCAST_GRP = '224.0.0.251'
# sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind( (UDP_IP,UDP_PORT) )
# #join the multicast group
# mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
# for host in ['esp01','microknoppix','pvknoppix','hprinter'][::-1]:
# #    the string in the following statement is an empty query packet
#     dns = dpkt.dns.DNS('\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01')
#     dns.qd[0].name=host+'.local'
#     sock.sendto(dns.pack(),(MCAST_GRP,UDP_PORT))
# sock.settimeout(5)
# while True:
#     try:
#         m=sock.recvfrom( 1024 );#print '%r'%m[0],m[1]
#         dns = dpkt.dns.DNS(m[0])
#         if len(dns.qd)>0:
#             print(dns.__repr__()+dns.qd[0].name)
#         if len(dns.an)>0 and dns.an[0].type == dpkt.dns.DNS_A:
#             print(dns.__repr__()+dns.an[0].name,socket.inet_ntoa(dns.an[0].rdata))
#     except socket.timeout:
#         break