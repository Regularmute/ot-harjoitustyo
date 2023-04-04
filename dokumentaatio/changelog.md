# Changelog

## Viikko 3

* User can switch between the login and registration screen
* User can create an account on the registration screen
* Set up an SQLite3 database initialization for the users
* Added class user_repository, which stores the User-objects into the local database
* Added class user_service, which handles the logic of creating an account
  * user_service also salts and hashes the user's password before storing it into the database
* Tested that the user_service stores the usernames