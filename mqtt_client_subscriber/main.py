# Code sourced from KFUPM COE 550 course - for term 241 - with modifications

import mqttclient
from time import *
from gpio import *

broker_add ='192.168.128.3'						#Broker Address
username= 'pscreen'								#Username
password = '1234'								#Password
sub1 = 'patient'									#Subscription topic
lcdMessageList = ["", ""]

def on_connect(status, msg, packet):			#show connection status
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	elif status == "":
		print(msg)
	
def on_disconnect(status, msg, packet):			#show disconnection status
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	elif status == "":
		print(msg)
	

def on_subscribe(status, msg, packet):			#show subscription status
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	elif status == "":
		print(msg)
	

def on_unsubscribe(status, msg, packet):		#show unsubscription status
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	elif status == "":
		print(msg)
	

def on_publish(status, msg, packet):			#show publishing status
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	elif status == "":
		print(msg)
	
def on_message_received(status, msg, packet):  #Invoked when new message received
	display_message = packet["payload"].split(", ")
	
	customWrite(0, display_message[0] + "\n" + display_message[1])
	print(packet["topic"])
	print(packet["payload"])
	
	# check received message and take action
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	
	elif status == "":
		print(msg)
	
def main():
	pinMode(0, OUT)

	mqttclient.init()

	mqttclient.onConnect(on_connect)
	mqttclient.onDisconnect(on_disconnect)
	mqttclient.onSubscribe(on_subscribe)
	mqttclient.onUnsubscribe(on_unsubscribe)
	mqttclient.onPublish(on_publish)
	mqttclient.onMessageReceived(on_message_received)
	print('Client Initialized')

	mqttclient.connect(broker_add,username,password)
	while not mqttclient.state()["connected"]:		#wait until connected
 		pass											#do nothing
 
	mqttclient.subscribe(sub1)

	while True:
		delay(6000);
		
if __name__ == "__main__":
	main()