import customtkinter
from CTkToolTip import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer
from invocation import Invocation
import all_invocations

app_width = 800
app_height = 600


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
            invocation_checkbox_tooltip = CTkToolTip(invocation_checkbox, message=invocation.get_description(), wraplength=app_width/2, justify="left", font=("Sans Serif", 20))
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
        self.geometry(f"{app_width}x{app_height}")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.raid_level = 0
        self.attempts_count = 0
        self.time_limit_count = 0
        self.helpful_spirit_count = 0
        self.path_level_count = 0

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

    def check_invocation_count(self, active_invocations, last_invocation_checkbox, category):
        attribute_count = self.get_attribute(category)
        if last_invocation_checkbox.get() == 1:
            self.set_attribute(category, attribute_count)
            if attribute_count > 1:
                self.set_attribute(attribute_count - 1)
                last_invocation_checkbox.deselect()
                if self.invocation_error_window is None or not self.invocation_error_window.winfo_exists():
                    self.invocation_error_window = InvocationErrorWindow(self)
                    self.invocation_error_window.after(10, self.focus_on_invocation_error_window)
                else:
                    self.invocation_error_window.focus()
                return True
        else:
            self.set_attribute(category, attribute_count - 1)
        return False


    def get_attribute(self, category):
        attribute = category.lower().replace(" ", "_") + "_count"
        return getattr(self, attribute)

    
    def set_attribute(self, category, new_value):
        attribute = category.lower().replace(" ", "_") + "_count"
        setattr(self, attribute, new_value)


    def invalid_invocation(self, last_invocation_checkbox, deselect_flag):
        if deselect_flag:
            last_invocation_checkbox.deselect()
        else:
            last_invocation_checkbox.select()
        if self.invocation_error_window is None or not self.invocation_error_window.winfo_exists():
            self.invocation_error_window = InvocationErrorWindow(self)
            self.invocation_error_window.geometry("%dx%d+%d+%d" % (480, 270, App.winfo_x(self) + app_width/4, App.winfo_y(self) + app_height/4))
            self.invocation_error_window.after(10, self.focus_on_invocation_error_window)
        else:
            self.invocation_error_window.destroy()
            self.invocation_error_window = InvocationErrorWindow(self)
            self.invocation_error_window.geometry("%dx%d+%d+%d" % (480, 270, App.winfo_x(self) + app_width/4, App.winfo_y(self) + app_height/4))
            self.invocation_error_window.after(10, self.focus_on_invocation_error_window)


    def update_raid_level(self, last_invocation_checkbox):
        active_invocations = self.invocation_frame.get()
        last_invocation = all_invocations.all_invocations[last_invocation_checkbox.cget("text")]


        # maybe create a list of the 4 categories and loop through it
        # requires a function which uses setattr and getattr

        if last_invocation.get_category() == "Attempts":
            if last_invocation_checkbox.get() == 1:
                self.attempts_count += 1
                if self.attempts_count > 1:
                    self.attempts_count -= 1
                    self.invalid_invocation(last_invocation_checkbox, True)
                    return
            else:
                self.attempts_count -= 1
        elif last_invocation.get_category() == "Time Limit":
            if last_invocation_checkbox.get() == 1:
                self.time_limit_count += 1
                if self.time_limit_count > 1:
                    self.time_limit_count -= 1
                    self.invalid_invocation(last_invocation_checkbox, True)
                    return
            else:
                self.time_limit_count -= 1
        elif last_invocation.get_category() == "Helpful Spirit":
            if last_invocation_checkbox.get() == 1:
                self.helpful_spirit_count += 1
                if self.helpful_spirit_count > 1:
                    self.helpful_spirit_count -= 1
                    self.invalid_invocation(last_invocation_checkbox, True)
                    return
            else:
                self.helpful_spirit_count -= 1
        elif last_invocation.get_category() == "Path Level":
            if last_invocation_checkbox.get() == 1:
                self.path_level_count += 1
                if self.path_level_count > 1:
                    self.path_level_count -= 1
                    self.invalid_invocation(last_invocation_checkbox, True)
                    return
            else:
                self.path_level_count -= 1

        zebak_check_1 = (last_invocation.get_name() == "Arterial Spray" or last_invocation.get_name() == "Blood Thinners") and "Not Just a Head" not in active_invocations
        zebak_check_2 = last_invocation.get_name() == "Not Just a Head" and ("Arterial Spray" in active_invocations or "Blood Thinners" in active_invocations)

        wardens_check_1 = last_invocation.get_name() == "Overclocked 2" and "Overclocked" not in active_invocations 
        wardens_check_2 = last_invocation.get_name() == "Insanity" and "Overclocked 2" not in active_invocations 
        wardens_check_3 = last_invocation.get_name() == "Overclocked" and "Overclocked 2" in active_invocations
        wardens_check_4 = last_invocation.get_name() == "Overclocked 2" and "Insanity" in active_invocations

        if zebak_check_1:
            self.invalid_invocation(last_invocation_checkbox, True)
            return
        elif zebak_check_2:
            self.invalid_invocation(last_invocation_checkbox, False)
            return
        elif wardens_check_1 or wardens_check_2:
            self.invalid_invocation(last_invocation_checkbox, True)
            return
        elif wardens_check_3 or wardens_check_4:
            self.invalid_invocation(last_invocation_checkbox, False)
            return

        pygame.mixer.init()

        active_invocations = self.invocation_frame.get()
        last_invocation_points = last_invocation.get_points()
        if last_invocation_checkbox.get() == 1:
            self.raid_level += last_invocation_points
            pygame.mixer.music.load("sfx/invocationon.mp3")
            pygame.mixer.music.play()
        else:
            self.raid_level -= last_invocation_points
            pygame.mixer.music.load("sfx/invocationoff.mp3")
            pygame.mixer.music.play()

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

        self.raid_level_progress_bar.set(self.raid_level/600)

try:
    app = App()
    app.mainloop()
except Exception as e:
    print(e)