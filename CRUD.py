from tkinter import*

from tkinter import messagebox

from tkinter import filedialog

import sqlite3

root=Tk()

frame=Frame(root, bg="#d7e7e3", width=300, height=400)

root.resizable(0,0)

root.iconbitmap("icon.ico")

root.title("BBDD")

frame.pack()

items=StringVar()

names=StringVar()

lastnames=StringVar()

passwords=StringVar()

adresss=StringVar()

def exit():
	value=messagebox.askquestion("Exit", "Are you shure about exit?")

	if value=="yes":
		root.destroy()
 
def sublime():
	messagebox.showinfo("SUBLIME 3.0.2", "Sublime Text\n UNREGISTRED \ncopyrigth 2020")

def clean():
	names.set("")
	lastnames.set("")
	items.set("")
	passwords.set("")
	adresss.set("")
	remarks.delete(1.0, END)

def toconnect():
	try:
		conexion=sqlite3.connect("User")
		cursor=conexion.cursor()
		cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR (20), LAST_NAME VARCHAR (20), PASSWORD VARCHAR (8), ADRESS VARCHAR (20), REMARK VARCHAR(250))")
		conexion.commit()
		messagebox.showinfo("Connect", "BBDD has conceted correctly")
		conexion.close()
	except:
		messagebox.showwarning("ERROR", "Table USER already exists")

def tocreate():
	global names
	global lastnames
	global adresss
	global passwords
	global remarks

	conexion=sqlite3.connect("User")
	cursor=conexion.cursor()
	cursor.execute("INSERT INTO USER VALUES(NULL, '"+ names.get()+"','"+ lastnames.get()+"','"+passwords.get()+"','"+adresss.get()+"','"+remarks.get(1.0, END)+"')")
	conexion.commit()
	messagebox.showinfo("Create", "One (1) row has been created correctly")
	conexion.close()

def todelete():
	value=messagebox.askquestion("Delete", "Are you shure about delete one (1) row?")
	if value=="yes":
			conexion=sqlite3.connect("User")
			cursor=conexion.cursor()
			cursor.execute("DELETE FROM USER WHERE ID='"+items.get()+"'")
			conexion.commit()
			messagebox.showinfo("Delete", "One (1) row has been deleted")
			conexion.close()
	
def toupdate():
	value=messagebox.askquestion("Update", "Are you sure about update one (1) row?")
	if value=="yes":
		try:
			conexion=sqlite3.connect("User")
			cursor=conexion.cursor()
			cursor.execute("UPDATE USER SET NAME='"+names.get()+"', LAST_NAME='"+lastnames.get()+"', PASSWORD='"+passwords.get()+"', ADRESS='"+adresss.get()+"', REMARK='"+remarks.get(1.0, END)+"' WHERE ID='"+items.get()+"'")
			conexion.commit()
			messagebox.showinfo("Update", "One (1) row has been updated")
			conexion.close()
		except:
			messagebox.showwarning("ERROR", "Invalid ID")

def toread():
	remarks.delete(1.0, END)
	try:
		conexion=sqlite3.connect("User")
		cursor=conexion.cursor()
		cursor.execute("SELECT * FROM USER WHERE ID='"+items.get()+"'")
		product=cursor.fetchall()
		for i in product:
			items.set(i[0])
			names.set(i[1])
			lastnames.set(i[2])
			passwords.set(i[3])
			adresss.set(i[4])
			remarks.insert(1.0, i[5])
		conexion.commit()
		conexion.close()
	except:
		messagebox.showwarning("ERROR", "Invalid ID")

bar=Menu(root)
root.config(bg="#d7e7e3", menu=bar, width=300, height=400)

bbdd=Menu(bar, tearoff=0)

bbdd.add_command(label="Connect", font=("Helvetica", 10), command=toconnect)

bbdd.add_separator()

bbdd.add_command(label="Exit", font=("Helvetica", 10), command=exit)

delete=Menu(bar, tearoff=0)

delete.add_command(label="Delete All", font=("Helvetica", 10), command=clean)

crud=Menu(bar, tearoff=0)

crud.add_command(label="Create", font=("Helvetica", 10), command=tocreate)

crud.add_command(label="Read", font=("Helvetica", 10), command=toread)

crud.add_command(label="Update", font=("Helvetica", 10), command=toupdate)

crud.add_command(label="Delete", font=("Helvetica", 10), command=todelete)

helps=Menu(bar, tearoff=0)

helps.add_command(label="License", font=("Helvetica", 10), command=sublime)

helps.add_command(label="About Us", font=("Helcetica", 10), command=sublime)

bar.add_cascade(label="BBDD", menu=bbdd, font=("Helvetica", 10))

bar.add_cascade(label="Delete", menu=delete, font=("Helvetica", 10))

bar.add_cascade(label="CRUD", menu=crud, font=("Helvetica", 10))

bar.add_cascade(label="Help", menu=helps, font=("Helvetica", 10))

name=Entry(frame, bg="white", font="Consolas", fg="Black", textvariable=names)
name.grid(row=2, column=2, pady=5, padx=5, columnspan=3)

name=Label(frame, text="Name: ", bg="#d7e7e3")
name.grid(row=2, column=1, pady=5, padx=5)

lastname=Entry(frame, bg="white", fg="black", font="Consolas", textvariable=lastnames)
lastname.grid(row=3, column=2, pady=5, padx=5, columnspan=3)

lastname=Label(frame, text="Last Name:", bg="#d7e7e3")
lastname.grid(row=3, column=1, padx=5)

password=Entry(frame, show="*", font="Consolas", bg="white", textvariable=passwords)
password.grid(row=4, column=2, padx=5, columnspan=3)

password=Label(frame, text="Password:", bg="#d7e7e3")
password.grid(row=4, column=1, padx=5)

adress=Entry(frame, bg="white", font="Consolas",  textvariable=adresss)
adress.grid(row=5, column=2, pady=5, padx=5, columnspan=3)

adress=Label(frame, text="Adress: ", bg="#d7e7e3")
adress.grid(row=5, column=1, pady=5, padx=5)

remarks=Text(frame, bg="white", font="Consolas", width=20, height=8)
remarks.grid(row=6, column=2, pady=5, padx=5, columnspan=3)

scroll=Scrollbar(frame, command=remarks.yview)
scroll.grid(row=6, column=5, sticky="nsew")
remarks.config(yscrollcommand=scroll.set)

remark=Label(frame, text="Insert a\n commentary:", bg="#d7e7e3")
remark.grid(row=6, column=1, padx=5, pady=5)

item=Entry(frame, bg="white", font="Consolas", textvariable=items)
item.grid(row=1, column=2, padx=5, pady=5, columnspan=3)

item=Label(frame, text="ID:", bg="#d7e7e3")
item.grid(row=1, column=1, padx=5, pady=5)

create=Button(frame, text="Create", bg="#baeee1", activebackground="#76f2d4", command=tocreate)
create.grid(row=7, column=1, padx=5, pady=5)

read=Button(frame, text="Read", bg="#baeee1", activebackground="#76f2d4", command=toread)
read.grid(row=7, column=2, padx=5, pady=5)

update=Button(frame, text="Update", bg="#baeee1", activebackground="#76f2d4", command=toupdate)
update.grid(row=7, column=3, padx=5, pady=5)

delete=Button(frame, text="Delete", bg="#baeee1", activebackground="#76f2d4", command=todelete)
delete.grid(row=7, column=4, padx=5, pady=5)

root.mainloop()