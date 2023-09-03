import customtkinter
from invocation import Invocation
import all_invocations

global_raid_level = 0

class InvocationsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, invocations):
        super().__init__(master)
        self.invocation_checkboxes = []

        for index, invocation in enumerate(invocations):
            invocation_checkbox = customtkinter.CTkCheckBox(self, text=invocation.get_name(), command=master.update_raid_level)
            invocation_checkbox.grid(row=index, column=0, padx=10, pady=(10, 0), sticky="w")
            self.invocation_checkboxes.append(invocation_checkbox)

    def get(self):
        active_invocations = []
        for _, invocation_checkbox in enumerate(self.invocation_checkboxes):
            if invocation_checkbox.get() == 1:
                active_invocations.append(invocation_checkbox.cget("text"))
        return active_invocations


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x600")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.invocation_frame = InvocationsFrame(self, all_invocations.all_invocations.values())
        self.invocation_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.raid_level_label = customtkinter.CTkLabel(self, text="0", fg_color="transparent", font=("Sans Serif", 20))
        self.raid_level_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")


    def update_raid_level(self):
        active_invocations = self.invocation_frame.get()
        print("Active invocations are:", active_invocations)
        global_raid_level = 0
        for invocation in active_invocations:
            global_raid_level += all_invocations.all_invocations[invocation].get_points()
        self.raid_level_label.configure(text=str(global_raid_level))


app = App()
app.mainloop()