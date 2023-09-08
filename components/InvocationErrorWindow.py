import customtkinter

class InvocationErrorWindow(customtkinter.CTkToplevel):
    def __init__(self, master, error_message, app_width, app_height):
        super().__init__(master)
        self.title("Invocation error")
        self.geometry("69x69") # default geometry, although it's manually set

        self.label = customtkinter.CTkLabel(self)
        self.label.pack(padx=20, pady=20)

        self.change_error_message(error_message)
        self.geometry("%dx%d+%d+%d" % (600, 100, self.winfo_x() + app_width/4, self.winfo_y() + app_height/4))
        self.after(10, master.focus_on_invocation_error_window)

    def change_error_message(self, message):
        self.label.configure(text=message)