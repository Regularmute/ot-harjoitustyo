from tkinter import ttk, constants, StringVar
from user_service import user_service, UsernameExistsError


class RegisterView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._error_message = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) < 3:
            self._show_error("Username must be at least 3 characters long")
            return

        if len(password) < 6:
            self._show_error("Password must be at least 6 characters long")
            return
        try:
            user_service.create_user(username, password)
        except UsernameExistsError:
            self._show_error(f"Username {username} is already taken")

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(
            row=1, column=1, sticky=(constants.EW), padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=(constants.EW), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,
                                      textvariable=self._error_message,
                                      foreground="red")

        heading_label = ttk.Label(master=self._frame, text="Create an account")

        self._initialize_username_field()
        self._initialize_password_field()

        cancel_button = ttk.Button(master=self._frame, text="Cancel",
                                   command=self._show_login_view)
        register_button = ttk.Button(master=self._frame, text="Register",
                                     command=self._create_user_handler)

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        cancel_button.grid(row=3, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)
        register_button.grid(row=4, column=0, columnspan=2,
                             sticky=(constants.EW), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()
