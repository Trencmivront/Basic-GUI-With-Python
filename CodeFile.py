import customtkinter

customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("500x350")


def login():
    frame.destroy()

    new_frame = customtkinter.CTkFrame(master = root)
    new_frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    
    label = customtkinter.CTkLabel(master = new_frame, text = "Succesfuly logged in! What now?", font = ("Roboto", 24))
    label.pack(pady = 20, padx = 60)


frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Login System", font = ("Roboto", 24))
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text = "Username")
entry1.pack(pady = 12, padx = 10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "Login", command = login)
button.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "Rememer Me", command = login)
checkbox.pack(pady = 12, padx =10)

slider = customtkinter.CTkSlider(master = frame)
slider.pack(pady = 2, padx = 5)

root.mainloop()
