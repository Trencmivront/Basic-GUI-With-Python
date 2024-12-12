import customtkinter

customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("green")

def login():
    if entry1.get() == "username":
        if entry2.get() == "password":

            frame.destroy()

            frame_2.destroy()

            new_frame = customtkinter.CTkFrame(master = root)
            new_frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    
            label = customtkinter.CTkLabel(master = new_frame, text = "Succesfuly logged in! What now?", font = ("Roboto", 24))
            label.pack(pady = 20, padx = 60)
        else:
            print("Incorrect Password!")
    else:
        print("Incorrect Username!")

    


def sign_up():
    pass


def check_state():
    if checkbox_var.get() =="on":
        print("check box checked")
    elif checkbox_var.get() =="off":
        print("Check box unchecked")

root = customtkinter.CTk()

root.geometry("500x350")

checkbox_var = customtkinter.StringVar(value = "off")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

frame_2 = customtkinter.CTkFrame(master = frame, width = 200, height = 200)
frame_2.pack(pady = 20, padx = 60, fill = "x", expand = False)

label = customtkinter.CTkLabel(master = frame_2, text = "Login System", font = ("Roboto", 24))
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame_2, placeholder_text = "Username")
entry1.pack(pady = 12, padx = 10)

entry2 = customtkinter.CTkEntry(master = frame_2, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12, padx = 10)

button_log_in = customtkinter.CTkButton(master = frame_2, text = "Login", command = login)
button_log_in.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame_2, variable = checkbox_var, onvalue = "on", offvalue = "off", text = "Rememer Me", command = check_state)
checkbox.pack(pady = 12, padx =10)

button_sign_up = customtkinter.CTkButton(master = frame_2, width = 12, height = 10, text = "Sing Up", command = sign_up)
button_sign_up.pack(side = "bottom", pady = 50, padx = 20)

root.mainloop()
