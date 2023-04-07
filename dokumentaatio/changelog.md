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

### Testing
* More tests for user_service.py:
  * Registered accounts' passwords are hashed before storing
  * Service-Object's user-property is updated correctly before and after logging in
  * Logging in with invalid credentials throws an error
  * Trying to register with a taken username throws an error
  * Creating an account successfully updates the user-property correctly (as when logging in).
  * Logging out clears the user property
  * get_current_user returns the currently logged user

### Code
* user_service.py keeps track of the logged user
* Refactored code to follow PEP8-standard
* Refactored and modularized UI for clarity
* Set up new invoke tasks to help with linting and automatic formatting
* Refactored code for registration and logging in
* Separated application logic to user_service from user_repository (password hashing)
