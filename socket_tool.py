import socket,struct
class socketTool:
    def __init__(self, remote_ip ,local_port):
        self.remote_ip = remote_ip
        self.remote_port = 4822
        self.local_port = local_port
        self.local_ip = ''
        self.so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def connect(self):
        pass

    def setRemoteIp(self, ip):
        self.remote_ip = ip
    
    def setLocalPort(self, port):
        self.local_port = port

    def sendTestCmd(self, index, timeout_t):
        print("************************************************************************")
        print("send cmd index is " + str(hex(index)))
        self.so.sendto(struct.pack('>HB',0x1234,index),(self.remote_ip, self.remote_port))
        self.so.settimeout(timeout_t)

    def recvTestResult(self, index):   
        try:
            ret,address= self.so.recvfrom(1024)    
        except socket.timeout:
            ret = b''
        try:
            head, item_index, result = struct.unpack('>H2B',ret)
            print("recv cmd index is " + str(hex(item_index)) + " result is " + str(hex(result)))
        except:
            head = 0xFFFF   
        if head == 0x5678:
            if item_index == index and result == 0xFF:
                return True
            else:
                return False
        else:
            return False