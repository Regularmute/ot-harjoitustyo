from tkinter import ttk, constants

class SheetView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Pathfinder 2E Sheet")

        username_label = ttk.Label(master=self._frame, text="You're logged in!")
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._show_login_view
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        logout_button.grid(
            row=3, column=0, columnspan=2,
            sticky=(constants.E, constants.W), padx=5, pady=5
        )
       
        self._root.grid_columnconfigure(1, weight=1, minsize=300)
