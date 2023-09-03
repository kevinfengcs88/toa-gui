import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.checkboxes = []

        for index, value in enumerate(values):
            c = customtkinter.CTkCheckBox(self, text=value)
            c.grid(row=index, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(c)

    def get(self):
        checked_checkboxes = []
        for _, checkbox in enumerate(self.checkboxes):
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame_1 = MyCheckboxFrame(self, values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.checkbox_frame_2 = MyCheckboxFrame(self, values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checked checkboxes are:",  self.checkbox_frame_1.get(), self.checkbox_frame_2.get())

app = App()
app.mainloop()