# Changelog

## Viikko 3

* User can switch between the login and registration screen
* User can create an account on the registration screen
* Set up an SQLite3 database initialization for the users
* Added class user_repository, which stores the User-objects into the local database
* Added class user_service, which handles the logic of creating an account
  * user_service also salts and hashes the user's password before storing it into the database
* Tested that the user_service stores the usernames
* A registered user can login and logout

## Viikko 4

### User experience
* User is automatically logged in after registering succesfully
* User cannot register with a username used by another account
  * Doing so will display an error message
* Logging in with invalid credentials displays an error message

* A logged user without an existing character is prompted to create one
* Created character is stored into a database, and its name is displayed to its creator.
* A user can currently have one character at a time.

### Testing
* More tests for user_service.py:
  * Registered accounts' passwords are hashed before storing
  * Service-Object's user-property is updated correctly before and after logging in
  * Logging in with invalid credentials throws an error
  * Trying to register with a taken username throws an error
  * Creating an account successfully updates the user-property correctly (as when logging in).
  * Logging out clears the user property
  * get_current_user returns the currently logged user
* Set up test database
* Finish testing user_repository.py:
  * create() stores an User object correctly to the database
  * get_all() retrieves Users correctly from the database
  * get_one_by_username() retrieves correct User from the database
  * delete_all() clears the contents of the Users database
* Add tests to character_service.py:
  * create_character() stores a Character object correctly
  * get_characters() fetches Character objects correctly
  * characters can be fetched by their creator_id or own id
  * characters' names can be edited
  * characters' other properties can be edited
* Add tests to character_repository.py:
  * characters can be created and fetched correctly
  * characters' names and properties can be edited correctly

### Code
* user_service.py keeps track of the logged user
* Refactored code to follow PEP8-standard
* Refactored and modularized UI for clarity
* Set up new invoke tasks to help with linting and automatic formatting
* Refactored code for registration and logging in
* Separated application logic to user_service from user_repository (password hashing)
* Create and initialize a table for characters
* Set up files to interact with the character table
* Begin working on application logic for characters

## Viikko 5

### User experience
* User can now create multiple characters
* User can now edit characters' names
* User can now switch between viewing characters and a specific sheet
* Ui has been adjusted for clarity
* Character creation has been assigned to character-list view

### Testing
* Tests have been added and modified to character_repository and character_service

### Code
* Characters are tracked by a unique id set in SQLite

## Viikko 6

### User Experience
* User can now edit characters' level, experience and hit points.

### Code
* Some lines have been split into under 79 long lines to follow PEP8.
* Docstring has been written for all non-UI related code.
* Added ancestry and heritage attributes to character entity and refactored code to adapt.

### Documentation
* Architecture document has been expanded to cover the basic information of the app.
* User guide has been written for the app.

### Tests
* More tests for character service and repository.
* Tests adjusted for the change in character entity.

## Viikko 7

### User Experience
* User now sees the previous value of a field when editing.
* User can only enter positive numbers to certain fields.

### Documentation
* Docstring added to UI files.
