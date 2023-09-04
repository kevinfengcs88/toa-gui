import customtkinter
from invocation import Invocation
import all_invocations

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


class RaidLevelFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x600")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.raid_level = 0

        self.invocation_frame = InvocationsFrame(self, all_invocations.all_invocations.values())
        self.invocation_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.raid_level_frame = RaidLevelFrame(self)
        self.raid_level_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.raid_level_frame.grid_columnconfigure(0, weight=1)

        self.raid_level_label = customtkinter.CTkLabel(self.raid_level_frame, text="0", fg_color="transparent", text_color="yellow", font=("Sans Serif", 20))
        self.raid_level_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.raid_level_progress_bar = customtkinter.CTkProgressBar(self.raid_level_frame, orientation="horizontal", border_color="black", border_width=1, progress_color="yellow")
        self.raid_level_progress_bar.set(0)
        self.raid_level_progress_bar.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")


    def update_raid_level(self):
        active_invocations = self.invocation_frame.get()
        print("Active invocations are:", active_invocations)
        self.raid_level = 0
        # this can be made more efficient by just adding or subtracting the one that was just checked
        # is that desirable with the invocation frame only having access to master though?
        for invocation in active_invocations:
            self.raid_level += all_invocations.all_invocations[invocation].get_points()
        self.raid_level_label.configure(text=str(self.raid_level))
        if self.raid_level < 150:
            self.raid_level_label.configure(text_color="yellow")
            self.raid_level_progress_bar.configure(progress_color="yellow")
        elif self.raid_level >= 150 and self.raid_level < 300:
            self.raid_level_label.configure(text_color="blue")
            self.raid_level_progress_bar.configure(progress_color="blue")
        elif self.raid_level >= 300:
            self.raid_level_label.configure(text_color="red")
            self.raid_level_progress_bar.configure(progress_color="red")

        # update the progress bar
        self.raid_level_progress_bar.set(self.raid_level/600)


app = App()
app.mainloop()