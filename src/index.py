from tkinter import Tk
from login_view import LoginView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        self._current_view = LoginView(
            self._root
        )

        self._current_view.pack()

window = Tk()
window.title("Pathdinder 2e Character Sheet")

ui = UI(window)
ui.start()

window.mainloop()