import tkinter
from tkinter import *
import sys
from pypresence import *
from time import time

def main():
	class vars():
		button1_label = str()
		button1_url = str()
		button2_lanel = str()
		button2_url = str()
		buttons_count = int(0)
		client_id = str()
		details = str()
		state = str()
		small_image = str()
		big_image = str()
		small_image_text = str()
		big_image_text = str()
	def buttons(count):
		vars.buttons_count=count
		if vars.buttons_count == 0:
			button_2.configure(bg="gray")
			button_3.configure(bg="lightgray")
			button_4.configure(bg="lightgray")
			textbox_8.configure(state="disabled")
			textbox_9.configure(state="disabled")
			textbox_10.configure(state="disabled")
			textbox_11.configure(state="disabled")
		elif vars.buttons_count == 1:
			button_2.configure(bg="lightgray")
			button_3.configure(bg="gray")
			button_4.configure(bg="lightgray")
			textbox_8.configure(state="normal")
			textbox_9.configure(state="normal")
			textbox_10.configure(state="disabled")
			textbox_11.configure(state="disabled")
		elif vars.buttons_count == 2:
			button_2.configure(bg="lightgray")
			button_3.configure(bg="lightgray")
			button_4.configure(bg="gray")
			textbox_8.configure(state="normal")
			textbox_9.configure(state="normal")
			textbox_10.configure(state="normal")
			textbox_11.configure(state="normal")
	def Stop():
		sys.exit(0)
		print("disconnected.") #disconnected
	def Start():
		Apply()
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
		
		timestamp = int(time())
		CLIENT_ID = vars.client_id
		RPC = Presence(CLIENT_ID)
		RPC.connect()
		if vars.buttons_count == 0:
			RPC.update(start=timestamp,
				large_image=vars.big_image,
				large_text=vars.big_image_text,
				small_image=vars.small_image,
				small_text=vars.small_image_text,
				details=vars.details,
				state=vars.state
           	)
		elif vars.buttons_count == 1:
			vars.button1_label = textbox_8.get()
			vars.button1_url = textbox_9.get()
			RPC.update(start=timestamp,
				large_image=vars.big_image,
				large_text=vars.big_image_text,
				small_image=vars.small_image,
				small_text=vars.small_image_text,
				details=vars.details,
				state=vars.state,
				buttons=[{"label": vars.button1_label, "url": vars.button1_url}]
				)
		elif vars.buttons_count == 2:
			vars.button1_label = textbox_8.get()
			vars.button1_url = textbox_9.get()
			vars.button2_label = textbox_10.get()
			vars.button2_url = textbox_11.get()
			RPC.update(start=timestamp,
				large_image=vars.big_image,
				large_text=vars.big_image_text,
				small_image=vars.small_image,
				small_text=vars.small_image_text,
				details=vars.details,
				state=vars.state,
				buttons=[{"label": vars.button1_label, "url": vars.button1_url}, {"label": vars.button2_label, "url": vars.button2_url}]
			)

	win = Tk()
	win.geometry("290x450")
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
	
	label_7 = Label(text="Buttons count:") #buttons count:
	label_7.place(x=10,y=235)
	
	label_8 = Label(text="Button1 label:") #Button1 label:
	label_8.place(x=10,y=273)
	
	label_9 = Label(text="Button1 URL:") #Button1 URL:
	label_9.place(x=10,y=301)
	
	label_10 = Label(text="Button2 label:") #Button2 label:
	label_10.place(x=10,y=341)
	
	label_11 = Label(text="Button2 URL:") #Button2 URL:
	label_11.place(x=10,y=369)
	
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
	
	textbox_8 = Entry(state="disabled") #button 1 label
	textbox_8.place(x=110,y=272)
	
	textbox_9 = Entry(state="disabled") #button 1 url
	textbox_9.place(x=110,y=300)
	
	textbox_10 = Entry(state="disabled") #button 2 label
	textbox_10.place(x=110,y=340)
	
	textbox_11 = Entry(state="disabled") #button 2 url
	textbox_11.place(x=110,y=368)
	
	button_1 = Button(text="Start", width=10, height=1, command=Start) #start button
	button_1.place(x=140,y=420, anchor=CENTER)
	
	button_2 = Button(text="0", width=1, height=1, bg="gray",command=lambda:buttons(0)) #change buttons count to 0
	button_2.place(x=160,y=230)
	
	button_3 = Button(text="1", width=1, height=1, bg="lightgray",command=lambda:buttons(1)) #change buttons count to 1
	button_3.place(x=200,y=230)
	
	button_4 = Button(text="2", width=1, height=1, bg="lightgray",command=lambda:buttons(2)) #change buttons count to 2
	button_4.place(x=240,y=230)
	
	win.mainloop()
main()
