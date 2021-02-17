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
		winHeight = int(320)
		winWidth = int(250)
		client_id = str()
		details = str()
		state = str()
		small_image = str()
		big_image = str()
	def Stop():
		sys.exit(0)
		button_1.setText("Start")
		button_1.clicked.connect(Start)
		button_1.clicked.disconnect(Stop)
		print("rozłączono.") #disconnected
	
	def Start():
		pre.start()
		button_1.setText("Stop")
		button_1.clicked.disconnect(Start)
		button_1.clicked.connect(Stop)
	def Apply():
		if textbox_1.text() == "":
			error.show()
		if textbox_2.text() == "":
			textbox_2.setText(" ")
		if textbox_3.text() == "":
			textbox_3.setText(" ")
		if textbox_4.text() == "":
			textbox_4.setText(" ")
		if textbox_5.text() == "":
			textbox_5.setText(" ")
		else:
			error.hide()
			vars.client_id = textbox_1.text()
			vars.details = textbox_2.text()
			vars.state = textbox_3.text()
			vars.small_image = textbox_4.text()
			vars.big_image = textbox_5.text()
			
			client_id = vars.client_id
			rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
			print("połączono.") #connected
		
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
			                #"small_text": "",
			                "small_image": vars.small_image,
			                #"large_text": "",
			                "large_image": vars.big_image
			            }
			        }
			    rpc_obj.set_activity(activity)
			    time.sleep(900)
	pre = Thread(target=Apply)
	pre.daemon = True
	app = QApplication(sys.argv)
	
	win = QWidget()
	win.resize(vars.winHeight,vars.winWidth)
	win.setMinimumSize(vars.winHeight,vars.winWidth)
	win.setMaximumSize(vars.winHeight,vars.winWidth)
	win.setWindowTitle("DC Rich Presenceinator v1.0 PL")
	win.show()
	
	error = QLabel("Błąd:\nMusisz podać ID klienta.", win)
	error.move(10,180)
	
	label_1 = QLabel("ID klienta:", win) #client id
	label_1.move(10,15)
	label_1.show()
	
	label_2 = QLabel("Stan:", win) #state
	label_2.move(10,45)
	label_2.show()
	
	label_3 = QLabel("Detale:", win) #details
	label_3.move(10,77)
	label_3.show()
	
	label_4 = QLabel("Duże zdj.:", win) #large pic.
	label_4.move(10,110)
	label_4.show()
	
	label_5 = QLabel("Małe zdj.:", win) #small pic.
	label_5.move(10,144)
	label_5.show()
	
	textbox_1 = QLineEdit(win) #client id
	textbox_1.move(80,12)
	textbox_1.resize(220, 20) 
	textbox_1.show()
	
	textbox_2 = QLineEdit(win) #state
	textbox_2.move(80,42)
	textbox_2.resize(220, 20)
	textbox_2.show()
	
	textbox_3 = QLineEdit(win) #details
	textbox_3.move(80,75)
	textbox_3.resize(220, 20)
	textbox_3.show()
	
	textbox_4 = QLineEdit(win) #large pic.
	textbox_4.move(80,107)
	textbox_4.resize(220, 20)
	textbox_4.show()
	
	textbox_5 = QLineEdit(win) #small pic.
	textbox_5.move(80,139)
	textbox_5.resize(220, 20)
	textbox_5.show()
	
	button_1 = QPushButton("Start", win) #start button
	button_1.resize(120,20)
	button_1.move(100, 220)
	button_1.clicked.connect(Start)
	button_1.show()
	
	sys.exit(app.exec_())

main()
