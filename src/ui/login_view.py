from tkinter import ttk, constants, StringVar
from user_service import user_service


class LoginView:
    def __init__(self, root, show_register_view, on_login):
        self._root = root
        self._frame = None
        self._show_register_view = show_register_view
        self._username_entry = None
        self._password_entry = None
        self._on_login = on_login
        self._error_label = None
        self._error_message = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        user = user_service.login(username, password)

        if user:
            self._on_login()

        else:
            self._show_error("Wrong credentials")

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,
                                      textvariable=self._error_message, foreground="red")
        heading_label = ttk.Label(
            master=self._frame, text="Pathfinder 2E Character Sheet")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler)

        register_button = ttk.Button(
            master=self._frame, text="Register",
            command=self._show_register_view)

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1,
                                  sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1,
                                  sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2,
                          sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(row=4, column=0, columnspan=2,
                             sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)
