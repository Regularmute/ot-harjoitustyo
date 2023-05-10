from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.character_service import (
    character_service,
    ValueTypeError,
    NegativeValueError,
    MissingParamError)


class SheetView:
    def __init__(self, root, show_login_view, show_char_list_view, character_id):
        """Alustaa lomakenäkymä-olion.

        Args:
            - root: tkinter.Tk, tämän näkymän juurikomponentti.
            - show_login_view: funktio, joka näyttää kirjautumisnäkymän.
            - show_char_list_view: funktio, joka näyttää hahmolistanäkymän.
            - character_id(int): näytettävän lomakkeen hahmon tunnisteluku.
        """
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._on_return = show_char_list_view
        self._user = user_service.get_current_user()

        self._error_label = None
        self._error_message = None

        self._character = character_service.get_character_by_character_id(character_id)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid(columnspan=3)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _logout_handler(self):
        user_service.logout
        self._show_login_view()

    def _handle_return(self):
        self._on_return()

    def _edit_name_handler(self):
        """Piilottaa hahmon nimen ja näyttää käyttäjälle muokkauskentän."""
        self._edit_name_btn.grid_remove()
        self._name_entry.insert(0, self._character.name)
        self._name_entry.grid(
            row=3, column=1, padx=5, pady=5)
        self._confirm_name_btn.grid(
            row=3, column=2, padx=5, pady=5)

    def _edit_name_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon nimen muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän.
        """
        new_name = self._name_entry.get()
        try:
            character_service.set_character_attribute_string(
                self._character.character_id, "name", new_name)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except MissingParamError as e:
            self._show_error(e.args[0])

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

    def _edit_ancestry_handler(self):
        """Piilottaa hahmon syntyperän ja näyttää käyttäjälle muokkauskentän."""
        self._edit_ancestry_btn.grid_remove()
        self._ancestry_entry.insert(0, self._character.ancestry)
        self._ancestry_entry.grid(
            row=4, column=1, padx=5, pady=5)
        self._confirm_ancestry_btn.grid(
            row=4, column=2, padx=5, pady=5)

    def _edit_ancestry_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon syntyperän muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän.
        """
        new_ancestry = self._ancestry_entry.get()
        try:
            character_service.set_character_attribute_string(
                self._character.character_id, "ancestry", new_ancestry)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except MissingParamError as e:
            self._show_error(e.args[0])

        self._ancestry_label.grid_remove()
        self._character_ancestry_label.grid_remove()
        self._ancestry_entry.grid_remove()
        self._confirm_ancestry_btn.grid_remove()

        self._initialize_ancestry_field()

    def _initialize_ancestry_field(self):
        self._ancestry_label = ttk.Label(
            master=self._frame, text="Ancestry:")
        self._character_ancestry_label = ttk.Label(
            master=self._frame, text=f"{self._character.ancestry}"
        )
        self._ancestry_entry = ttk.Entry(master=self._frame)
        self._edit_ancestry_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_ancestry_handler)
        self._confirm_ancestry_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_ancestry_confirm_handler)

        self._ancestry_label.grid(
            row=4, column=0, sticky=constants.W, padx=5, pady=5)
        self._character_ancestry_label.grid(
            row=4, column=1, sticky=constants.W, padx=5, pady=5)
        self._edit_ancestry_btn.grid(
            row=4, column=2, padx=5, pady=5)

    def _edit_heritage_handler(self):
        """Piilottaa hahmon perimän ja näyttää käyttäjälle muokkauskentän."""
        self._edit_heritage_btn.grid_remove()
        self._heritage_entry.insert(0, self._character.heritage)
        self._heritage_entry.grid(
            row=4, column=4, padx=5, pady=5)
        self._confirm_heritage_btn.grid(
            row=4, column=5, padx=5, pady=5)

    def _edit_heritage_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon perimän muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän.
        """
        new_heritage = self._heritage_entry.get()
        try:
            character_service.set_character_attribute_string(
                self._character.character_id, "heritage", new_heritage)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except MissingParamError as e:
            self._show_error(e.args[0])

        self._heritage_label.grid_remove()
        self._character_heritage_label.grid_remove()
        self._heritage_entry.grid_remove()
        self._confirm_heritage_btn.grid_remove()

        self._initialize_heritage_field()

    def _initialize_heritage_field(self):
        self._heritage_label = ttk.Label(
            master=self._frame, text="Heritage:")
        self._character_heritage_label = ttk.Label(
            master=self._frame, text=f"{self._character.heritage}"
        )
        self._heritage_entry = ttk.Entry(master=self._frame)
        self._edit_heritage_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_heritage_handler)
        self._confirm_heritage_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_heritage_confirm_handler)

        self._heritage_label.grid(
            row=4, column=3, sticky=constants.W, padx=5, pady=5)
        self._character_heritage_label.grid(
            row=4, column=4, sticky=constants.W, padx=5, pady=5)
        self._edit_heritage_btn.grid(
            row=4, column=5, padx=5, pady=5)

    def _edit_level_handler(self):
        """Piilottaa hahmon tason ja näyttää käyttäjälle muokkauskentän."""
        self._edit_level_btn.grid_remove()
        self._level_entry.insert(0,self._character.level)
        self._level_entry.grid(
            row=3, column=4, padx=5, pady=5)
        self._confirm_level_btn.grid(
            row=3, column=5, padx=5, pady=5)

    def _edit_level_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon tason muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän. Funktio heittää virheen, jos tallennettava arvo
        ei ole nolla tai positiivinen numero.
        """
        new_level = self._level_entry.get()
        try:
            character_service.set_character_attribute_float(
                self._character.character_id, "level", new_level)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except NegativeValueError as e:
            self._show_error(e.args[0])
        except ValueTypeError as e:
            self._show_error(e.args[0])

        self._level_label.grid_remove()
        self._character_level_label.grid_remove()
        self._level_entry.grid_remove()
        self._confirm_level_btn.grid_remove()

        self._initialize_level_field()

    def _initialize_level_field(self):
        self._level_label = ttk.Label(
            master=self._frame, text="Level:")
        self._character_level_label = ttk.Label(
            master=self._frame, text=f"{self._character.level}"
        )
        self._level_entry = ttk.Entry(master=self._frame)
        self._edit_level_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_level_handler)
        self._confirm_level_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_level_confirm_handler)

        self._level_label.grid(
            row=3, column=3, sticky=constants.W, padx=5, pady=5)
        self._character_level_label.grid(
            row=3, column=4, sticky=constants.W, padx=5, pady=5)
        self._edit_level_btn.grid(
            row=3, column=5, padx=5, pady=5)

    def _edit_experience_handler(self):
        """Piilottaa hahmon XP:n ja näyttää käyttäjälle muokkauskentän."""
        self._edit_experience_btn.grid_remove()
        self._experience_entry.insert(0,self._character.experience)
        self._experience_entry.grid(
            row=5, column=1, padx=5, pady=5)
        self._confirm_experience_btn.grid(
            row=5, column=2, padx=5, pady=5)

    def _edit_experience_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon XP:n muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän. Funktio heittää virheen, jos tallennettava arvo
        ei ole nolla tai positiivinen numero.
        """
        new_experience = self._experience_entry.get()
        try:
            character_service.set_character_attribute_float(
                self._character.character_id, "experience", new_experience)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except NegativeValueError as e:
            self._show_error(e.args[0])
        except ValueTypeError as e:
            self._show_error(e.args[0])

        self._experience_label.grid_remove()
        self._character_experience_label.grid_remove()
        self._experience_entry.grid_remove()
        self._confirm_experience_btn.grid_remove()

        self._initialize_experience_field()

    def _initialize_experience_field(self):
        self._experience_label = ttk.Label(
            master=self._frame, text="Experience:")
        self._character_experience_label = ttk.Label(
            master=self._frame, text=f"{self._character.experience}"
        )
        self._experience_entry = ttk.Entry(master=self._frame)
        self._edit_experience_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_experience_handler)
        self._confirm_experience_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_experience_confirm_handler)

        self._experience_label.grid(
            row=5, column=0, sticky=constants.W, padx=5, pady=5)
        self._character_experience_label.grid(
            row=5, column=1, sticky=constants.W, padx=5, pady=5)
        self._edit_experience_btn.grid(
            row=5, column=2, padx=5, pady=5)

    def _edit_hit_points_handler(self):
        """Piilottaa hahmon HP:n ja näyttää käyttäjälle muokkauskentän."""
        self._edit_hit_points_btn.grid_remove()
        self._hit_points_entry.insert(0, self._character.hit_points)
        self._hit_points_entry.grid(
            row=5, column=4, padx=5, pady=5)
        self._confirm_hit_points_btn.grid(
            row=5, column=5, padx=5, pady=5)

    def _edit_hit_points_confirm_handler(self):
        """Kutsuu sovelluslogiikkaa tallentamaan hahmon HP:n muutoksen.

        Muutoksen jälkeen funktio piilottaa muokkauskentän ja palauttaa
        normaalinäkymän. Funktio heittää virheen, jos tallennettava arvo
        ei ole nolla tai positiivinen numero.
        """
        new_hit_points = self._hit_points_entry.get()
        try:
            character_service.set_character_attribute_float(
                self._character.character_id, "hit_points", new_hit_points)
            self._character = character_service.get_character_by_character_id(
                self._character.character_id)
            self._hide_error()
        except NegativeValueError as e:
            self._show_error(e.args[0])
        except ValueTypeError as e:
            self._show_error(e.args[0])

        self._hit_points_label.grid_remove()
        self._character_hit_points_label.grid_remove()
        self._hit_points_entry.grid_remove()
        self._confirm_hit_points_btn.grid_remove()

        self._initialize_hit_points_field()

    def _initialize_hit_points_field(self):
        self._hit_points_label = ttk.Label(
            master=self._frame, text="Hit points:")
        self._character_hit_points_label = ttk.Label(
            master=self._frame, text=f"{self._character.hit_points}"
        )
        self._hit_points_entry = ttk.Entry(master=self._frame)
        self._edit_hit_points_btn = ttk.Button(
            master=self._frame, text="Edit", command=self._edit_hit_points_handler)
        self._confirm_hit_points_btn = ttk.Button(
            master=self._frame, text="Confirm", command=self._edit_hit_points_confirm_handler)

        self._hit_points_label.grid(
            row=5, column=3, sticky=constants.W, padx=5, pady=5)
        self._character_hit_points_label.grid(
            row=5, column=4, sticky=constants.W, padx=5, pady=5)
        self._edit_hit_points_btn.grid(
            row=5, column=5, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text="Pathfinder 2E Sheet")
        username_label = ttk.Label(
            master=self._frame, text=f"You're logged in as {self._user.username}!")
        return_button = ttk.Button(
            master=self._frame, text="Back to Characters", command=self._handle_return)
        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,
                                      textvariable=self._error_message,
                                      foreground="red")

        self._initialize_name_field()
        self._initialize_level_field()
        self._initialize_ancestry_field()
        self._initialize_heritage_field()
        self._initialize_experience_field()
        self._initialize_hit_points_field()

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        return_button.grid(row=6, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)
