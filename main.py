from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import rpc
import time
from time import mktime
from threading import Thread

def main():
	class vars():
		winHeight = int(270)
		winWidth = int(340)
		client_id = str()
		details = str()
		state = str()
		small_image = str()
		big_image = str()
		small_image_text = str()
		big_image_text = str()
	def Stop():
		sys.exit(0)
		button_1.setText("Start")
		button_1.clicked.connect(Start)
		button_1.clicked.disconnect(Stop)
		print("disconnected.") #disconnected
	
	def Start():
		presence.start()
		button_1.setText("Stop")
		button_1.clicked.disconnect(Start)
		button_1.clicked.connect(Stop)
	def Apply():
		error.hide()
	
		vars.client_id = textbox_1.text()
		vars.details = textbox_2.text()
		vars.state = textbox_3.text()
		vars.big_image = textbox_4.text()
		vars.small_image = textbox_5.text()
		vars.big_image_text = textbox_6.text()
		vars.small_image_text = textbox_7.text()
		
		if vars.small_image == str():
			vars.small_image = " "
		if vars.small_image_text == str():
			vars.small_image_text = "   "
		if vars.big_image_text == str():
			vars.big_image_text = "   "
		
		client_id = vars.client_id
		rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
		print("connected.") #connected
	
		time.sleep(5)
		start_time = mktime(time.localtime())
		while True:
		    activity = {
		    		"details": vars.details,
		    		"state": vars.state,
		            "timestamps": {
		                "start": start_time
		            },
		            "assets": {
		                "small_text": vars.small_image_text,
		                "small_image": vars.small_image,
		                "large_text": vars.big_image_text,
		                "large_image": vars.big_image
		            }
		        }
		    rpc_obj.set_activity(activity)
		    time.sleep(900)
	presence = Thread(target=Apply)
	presence.daemon = True
	app = QApplication(sys.argv)
	
	win = QWidget()
	win.resize(vars.winWidth,vars.winHeight)
	win.setMinimumSize(vars.winWidth,vars.winHeight)
	win.setMaximumSize(vars.winWidth,vars.winHeight)
	win.setWindowTitle("DC Rich Presenceinator v1.2 EN")
	win.show()
	
	error = QLabel("Error:\nYou must specify Client ID", win)
	error.move(10,180)
	
	label_1 = QLabel("Client ID:", win) #client id
	label_1.move(10,15)
	label_1.show()
	
	label_2 = QLabel("State:", win) #state
	label_2.move(10,45)
	label_2.show()
	
	label_3 = QLabel("Details:", win) #details
	label_3.move(10,77)
	label_3.show()
	
	label_4 = QLabel("Large picture:", win) #large picture
	label_4.move(10,107)
	label_4.show()
	
	label_5 = QLabel("Small picture:", win) #small picture
	label_5.move(10,140)
	label_5.show()
	
	label_6 = QLabel("Large pic. text:", win) #large pic. text:
	label_6.move(10,170)
	label_6.show()
	
	label_7 = QLabel("Small pic. text:", win) #small pic. text:
	label_7.move(10,200)
	label_7.show()
	
	textbox_1 = QLineEdit(win) #client id
	textbox_1.move(110,12)
	textbox_1.resize(220, 20) 
	textbox_1.show()
	
	textbox_2 = QLineEdit(win) #state
	textbox_2.move(110,42)
	textbox_2.resize(220, 20)
	textbox_2.show()
	
	textbox_3 = QLineEdit(win) #details
	textbox_3.move(110,75)
	textbox_3.resize(220, 20)
	textbox_3.show()
	
	textbox_4 = QLineEdit(win) #large picture
	textbox_4.move(110,107)
	textbox_4.resize(220, 20)
	textbox_4.show()
	
	textbox_5 = QLineEdit(win) #small picture
	textbox_5.move(110,139)
	textbox_5.resize(220, 20)
	textbox_5.show()
	
	textbox_6 = QLineEdit(win) #large picture text
	textbox_6.move(110,169)
	textbox_6.resize(220, 20)
	textbox_6.show()
	
	textbox_7 = QLineEdit(win) #small picture text
	textbox_7.move(110,199)
	textbox_7.resize(220, 20)
	textbox_7.show()
	
	button_1 = QPushButton("Start", win) #start button
	button_1.resize(120,20)
	button_1.move(100, 230)
	button_1.clicked.connect(Start)
	button_1.show()
	
	sys.exit(app.exec_())

main()
