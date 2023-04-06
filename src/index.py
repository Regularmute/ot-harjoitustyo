from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Pathfinder 2e Character Sheet")

ui = UI(window)
ui.start()

window.mainloop()
