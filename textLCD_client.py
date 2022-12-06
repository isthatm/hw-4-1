from time import sleep
import erpc
from text_lcd import *
import sys
from array import *

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python led_test_client.py COM5")
        exit()

    # Initialize all erpc infrastructure
    xport = erpc.transport.SerialTransport(sys.argv[1], 9600)
    client_mgr = erpc.client.ClientManager(xport, erpc.basic_codec.BasicCodec)
    client = client.TextLCDServiceClient(client_mgr)

    # Write character on the connected erpc server
    myNum = array('B',[49,50,51,52,53,54])
    
    client.location(3,0)
    for i1 in range(0,2):
       client.enterChar(myNum[i1])
       sleep(1)
    client.location(3,1)
    for i2 in range(2,6):
       client.enterChar(myNum[i2])
       sleep(1)

    
