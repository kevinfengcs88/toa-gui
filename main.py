import customtkinter
from invocation import Invocation
from components.App import App

app_width = 800
app_height = 600

try:
    app = App(app_width, app_height)
    app.mainloop()
except Exception as e:
    print(e)