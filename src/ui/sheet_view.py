from tkinter import ttk, constants
from services.user_service import user_service
from services.character_service import character_service


class SheetView:
    def __init__(self, root, show_login_view, show_char_list_view, character_id):
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._on_return = show_char_list_view
        self._user = user_service.get_current_user()

        # Hahmon tiedot
        self._character = character_service.get_character_by_character_id(character_id)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout
        self._show_login_view()

    def _handle_return(self):
        self._on_return()

    def _edit_name_handler(self):
        self._edit_name_btn.grid_remove()
        self._name_entry.grid(
            row=3, column=1, padx=5, pady=5)
        self._confirm_name_btn.grid(
            row=3, column=2, padx=5, pady=5)

    def _edit_name_confirm_handler(self):
        new_name = self._name_entry.get()
        character_service.set_character_name(
            self._character.character_id, new_name)
        self._character = character_service.get_character_by_character_id(
            self._character.character_id)

        self._name_label.grid_remove()
        self._character_name_label.grid_remove()
        self._name_entry.grid_remove()
        self._confirm_name_btn.grid_remove()

        self._initialize_name_field()

    def _initialize_name_field(self):
        self._name_label = ttk.Label(
            master=self._frame, text="Name:")
        self._character_name_label = ttk.Label(
            master=self._frame, text=f"{self._character.name}"
        )
        self._name_entry = ttk.Entry(master=self._frame)
        self._edit_name_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_name_handler)
        self._confirm_name_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_name_confirm_handler)

        self._name_label.grid(
            row=3, column=0, sticky=constants.W, padx=5, pady=5)
        self._character_name_label.grid(
            row=3, column=1, sticky=constants.W, padx=5, pady=5)
        self._edit_name_btn.grid(
            row=3, column=2, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text="Pathfinder 2E Sheet")
        username_label = ttk.Label(
            master=self._frame, text=f"You're logged in as {self._user.username}!")
        return_button = ttk.Button(
            master=self._frame, text="Back to Characters", command=self._handle_return)

        self._initialize_name_field()

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        return_button.grid(row=4, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)
