import customtkinter
from invocation import Invocation
import all_invocations

class InvocationErrorWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Invocation error")
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="That combination of invocations is not allowed.")
        self.label.pack(padx=20, pady=20)

class InvocationsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, invocations):
        super().__init__(master)
        self.invocation_checkboxes = []

        for index, invocation in enumerate(invocations):
            invocation_checkbox = customtkinter.CTkCheckBox(self, text=invocation.get_name())
            invocation_checkbox.configure(command=lambda checkbox=invocation_checkbox: master.update_raid_level(checkbox))
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

        self.invocation_error_window = None


    def focus_on_invocation_error_window(self):
        self.invocation_error_window.focus()


    def update_raid_level(self, last_invocation):
        print(last_invocation.cget("text"))
        if last_invocation.get() == 1:
            print("just turned on")
        elif last_invocation.get() == 0:
            print("just turned OFF")
        active_invocations = self.invocation_frame.get()
        # here check if last_invocation is in violation with the active_invocations
        # if so, then disable it and open the error window

        last_invocation_points = all_invocations.all_invocations[last_invocation.cget("text")].get_points()
        if last_invocation.get() == 1:
            self.raid_level += last_invocation_points
        else:
            self.raid_level -= last_invocation_points

        self.raid_level_label.configure(text=str(self.raid_level))
        if self.raid_level < 150:
            #####
            # if self.invocation_error_window is None or not self.invocation_error_window.winfo_exists():
            #     self.invocation_error_window = InvocationErrorWindow(self)
            #     self.invocation_error_window.after(10, self.focus_on_invocation_error_window)
            # else:
            #     self.invocation_error_window.focus()
            #####
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