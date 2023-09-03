import customtkinter
from invocation import Invocation

class InvocationsFrame(customtkinter.CTkFrame):
    def __init__(self, master, invocations):
        super().__init__(master)
        self.invocation_checkboxes = []

        for index, invocation in enumerate(invocations):
            invocation_checkbox = customtkinter.CTkCheckBox(self, text=invocation.get_name())
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
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        invocations = [
            Invocation("Need Some Help?", "The quantity of items offered by the Helpful Spirit will be reduced to 66%, with a minimum of one supply of that type.", 15, "Helpful Spirit"),
            Invocation("On a Diet", "Players can no longer eat food within the raid, though potions that restore health (such as Saradomin brews) can still be used.", 15, "Restoration"),
            Invocation("Mind the Gap!", "When Ba-Ba knocks back the player to the bottom of the room at 66% and 33% health, players will fall into the pit and die, unless they stand at the northern/southern sides of the room.", 10, "Ba-Ba")
        ]

        self.invocation_frame = InvocationsFrame(self, invocations)
        self.invocation_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=1)

    def button_callback(self):
        print("Active invocations are:", self.invocation_frame.get())

app = App()
app.mainloop()