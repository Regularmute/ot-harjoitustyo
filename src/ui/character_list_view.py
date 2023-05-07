"""Moduuli joka vastaa käyttäjän hahmojen listanäkymästä.

Sisältää kaksi luokkaa.
"""

from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.character_service import character_service

class CharacterListView:
    """Alustaa näkymän sisältämän listan hahmoista.

    Args:
        - root: tkinter.Tk, tämän näkymän juurikomponentti.
        - characters: lista käyttäjälle näytettävistä hahmoista.
        - show_character_view: funktio, joka näyttää tietyn hahmon lomakenäkymän.
    """
    def __init__(self, root, characters, show_character_view):
        self._root = root
        self._characters = characters
        self._show_character = show_character_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_character_item(self, character):
        character_frame = ttk.Frame(master=self._frame)
        character_name_label = ttk.Label(
            master=character_frame, text=character.name
        )
        character_view_btn = ttk.Button(
            master=character_frame,
            text="View",
            command=lambda: self._show_character(character.character_id)
        )

        character_name_label.grid(
            row=0, column=0, sticky=constants.W, padx=5, pady=5
        )
        character_view_btn.grid(
            row=0, column=1, sticky=constants.W, padx=5, pady=5
        )


        character_frame.grid_columnconfigure(0, weight=1)
        character_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for character in self._characters:
            self._initialize_character_item(character)

class CharactersView:
    def __init__(self, root, show_login_view, show_character):
        """Alustaa hahmolistanäkymän.

        Args:
            - root: tkinter.Tk, tämän näkymän juurikomponentti.
            - show_login_view: funktio, joka näyttää kirjautumisnäkymän.
            - show_character: funktio, joka näyttää tietyn hahmon lomakenäkymän.
        """
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._show_character_view = show_character
        self._user = user_service.get_current_user()
        self._character_list_view = None
        self._character_list_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        """Kirjaa käyttäjän ulos ja ohjaa hänet kirjautumisnäkymään."""
        user_service.logout
        self._show_login_view()

    def _create_character_handler(self):
        """Kutsuu sovelluslogiikkaa uuden hahmon luomiselle.

        Jos hahmon nimessä ei ole yhtään merkkejä (lukuunottamatta
        välilyöntejä), logiikkaa ei kutsuta ja näkymä näyttää virheviestin.
        """
        character_name = self._new_character_entry.get().strip()

        if len(character_name) < 1:
            self._show_error("Character must have a name")
            return

        character_service.create_character(self._user.user_id, character_name)
        self._initialize_character_list()

    def _view_character_handler(self, character_id):
        self._show_character_view(character_id)

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_character_list(self):
        if self._character_list_view:
            self._character_list_view.destroy()

        characters = character_service.get_all_by_creator_id(self._user.user_id)

        self._character_list_view = CharacterListView(
            self._character_list_frame,
            characters,
            self._view_character_handler
        )

        self._character_list_view.pack()

    def _initialize_character_creation_field(self):
        self._creation_label = ttk.Label(
            master=self._frame, text="Create a new character:"
        )
        self._new_character_entry = ttk.Entry(master=self._frame)
        self._create_character_btn = ttk.Button(
            master=self._frame, text="Create", command=self._create_character_handler)

        self._creation_label.grid(
            row=3, column=0, sticky=constants.W, padx=5, pady=5)
        self._new_character_entry.grid(
            row=3, column=1, padx=5, pady=5
        )
        self._create_character_btn.grid(
            row=3, column=2, padx=5, pady=5
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._character_list_frame = ttk.Frame(master=self._frame)

        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,
                                      textvariable=self._error_message,
                                      foreground="red")

        heading_label = ttk.Label(master=self._frame, text=f"{self._user.username}'s Characters")
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)


        self._initialize_character_list()
        self._initialize_character_creation_field()

        self._character_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        logout_button.grid(row=4, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()
