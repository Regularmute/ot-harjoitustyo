from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Pathfinder 2E Character Sheet")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)


        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="Login")
        register_button = ttk.Button(master=self._root, text="Register")

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

window = Tk()
window.title("Pathdinder 2e Character Sheet")

ui = UI(window)
ui.start()

window.mainloop()