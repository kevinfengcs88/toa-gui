import customtkinter
from CTkToolTip import *

class InvocationsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, invocations, app_width, app_height):
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

