# Code sourced from KFUPM COE 550 course - for term 241 - with modifications

import mqttclient
from time import *
from gpio import *
import random
import time

broker_add ='192.168.128.3'						#Broker Address
username= 'ambulence'								#Username
password = '1234'								#Password
sub = 'patient'									#Subscription topic

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
	# check received message and take action
	if status == "Success" or status == "Error":
		print(status + ": " + msg)
	
	elif status == "":
		print(msg)
	
def main():
	pinMode(0,IN)
	
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
 
	switchStatus=LOW

	while True:
		delay(6000);
		message = ""
		num = random.randint(0, 2)
		time_now = time.ctime()
		if num == 0:
			message = "Oxygen: Low, Pressure: Low, Time: " + time_now
		if num == 1:
			message = "Oxygen: Med, Pressure: Med, Time: " + time_now
		if num == 2:
			message = "Oxygen: High, Pressure: High, Time: " + time_now
		
		mqttclient.publish(sub, message, '1')

		
if __name__ == "__main__":
	main()