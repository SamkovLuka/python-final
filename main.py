from tkinter import*





press_return = True



def save():
    name = name_entry.get()
    surname = surname_entry.get()
    newlog = newlog_entry.get()
    newpass = newpass_entry.get()
    if not press_return:
        pass
    else:
       data = open("data.txt","w+")
       data.write(f"{name}")
       data.write(f"\n{surname}")
       data.write(f"\n{newlog}")
       data.write(f"\n{newpass}")
       pass
    if name == "":
        error1_label.pack()
        error1_label.after(1000,destroy)
    else:
       error1_label.destroy()
    if surname == "":
        error2_label.pack()
        error2_label.after(1000,destroy2)
    else:
       error2_label.destroy()
    if newlog == "":
        error3_label.pack()
        error3_label.after(1000,destroy3)
    else:
       error3_label.destroy()
    if newpass == "":
        error4_label.pack()
        error4_label.after(1000,destroy4)
    else:
       error4_label.destroy()
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    newlog_entry.delete(0, END)
    newpass_entry.delete(0, END)






def destroy():
   error1_label.config(root,text="")



def destroy2():
   error2_label.config(root,text="")


def destroy3():
   error3_label.config(root,text="")


def destroy4():
   error4_label.config(root,text="")





def check():
    login = login_entry.get()
    password = password_entry.get()
    try:
     data = open("data.txt","r")
     findlog = data.readline().strip()
     findpass = data.readline().strip()
     label_true = Label(root,text="Correct",font=14)
     if login == "":
        error3_label.pack()
        error3_label.after(1000,destroy3)
     if password == "":
        error4_label.pack()
        error4_label.after(1000,destroy3)
     if findpass == password:
        label_true.pack()
        return True
     elif findlog == login:
        label_true.pack()
        return True
     else:
         return False
    except:
        ValueError






root = Tk()
root.title("Register")
root.geometry("800x600")



#вхід
login_label = Label(root, text="Login: ", font=14)
login_label.pack()
login_entry = Entry(root, font=14)
login_entry.pack()

password_label = Label(root, text="Password: ", font=14)
password_label.pack()
password_entry = Entry(root, show="*", font=14)
password_entry.pack()

signin_button = Button(root, text="Sign in", font=20, command=check)
signin_button.pack()

register_label = Label(root, text="\nDon't have an account?", font=20)
register_label.pack()









#реєстрація
name_label = Label(root, text="Name:", font=14)
name_label.pack()
name_entry = Entry(root, font=14)
name_entry.pack()

surname_label = Label(root, text="Surname:", font=14)
surname_label.pack()
surname_entry = Entry(root, font=14)
surname_entry.pack()

newlog_label = Label(root, text="Create login: ", font=14)
newlog_label.pack()
newlog_entry = Entry(root, font=14)
newlog_entry.pack()

newpass_label = Label(root, text="Create password: ", font=14)
newpass_label.pack()
newpass_entry = Entry(root, show="*", font=14)
newpass_entry.pack()

register_button = Button(root, text="Sign up", font=20, command=save)
register_button.pack()







error1_label = Label(root,text="Enter your name",font=14)
error2_label = Label(root,text="Enter your surname",font=14)
error3_label = Label(root,text="Enter your login",font=14)
error4_label = Label(root,text="Enter your password",font=14)







root.bind(register_button,save)
root.bind(signin_button,check)
root.mainloop()