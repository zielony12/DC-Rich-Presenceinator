import tkinter
from tkinter import *
import sys
import rpc
import time
from time import mktime
from threading import Thread

def main():
	class vars():
		client_id = str()
		details = str()
		state = str()
		small_image = str()
		big_image = str()
		small_image_text = str()
		big_image_text = str()
	def Stop():
		sys.exit(0)
		print("disconnected.") #disconnected
	
	def Start():
		presence.start()
		button_1.configure(text="Stop", command=Stop)
	def Apply():
		vars.client_id = textbox_1.get()
		vars.details = textbox_2.get()
		vars.state = textbox_3.get()
		vars.big_image = textbox_4.get()
		vars.small_image = textbox_5.get()
		vars.big_image_text = textbox_6.get()
		vars.small_image_text = textbox_7.get()
		
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

	win = Tk()
	win.geometry("290x270")
	win.resizable(False, False)
	win.title("DC Rich Presenceinator v1.3 EN")
	
	label_1 = Label(text="Client ID:") #client id
	label_1.place(x=10,y=15)
	
	label_2 = Label(text="State:") #state
	label_2.place(x=10,y=45)
	
	label_3 = Label(text="Details:") #details
	label_3.place(x=10,y=77)
	
	label_4 = Label(text="Large picture:") #large picture
	label_4.place(x=10,y=107)
	
	label_5 = Label(text="Small picture:") #small picture
	label_5.place(x=10,y=140)
	
	label_6 = Label(text="Large pic. text:") #large pic. text:
	label_6.place(x=10,y=170)
	
	label_7 = Label(text="Small pic. text:") #small pic. text:
	label_7.place(x=10,y=200)
	
	textbox_1 = Entry() #client id
	textbox_1.place(x=110,y=12)
	
	textbox_2 = Entry() #state
	textbox_2.place(x=110,y=42)
	
	textbox_3 = Entry() #details
	textbox_3.place(x=110,y=75)
	
	textbox_4 = Entry() #large picture
	textbox_4.place(x=110,y=107)
	
	textbox_5 = Entry() #small picture
	textbox_5.place(x=110,y=139)
	
	textbox_6 = Entry() #large picture text
	textbox_6.place(x=110,y=169)
	
	textbox_7 = Entry() #small picture text
	textbox_7.place(x=110,y=199)
	
	button_1 = Button(text="Start", width=10, height=1, command=Start) #start button
	button_1.place(x=140, y=240, anchor=CENTER)
	
	win.mainloop()
main()
