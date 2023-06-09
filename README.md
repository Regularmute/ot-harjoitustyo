# Pathfinder 2E Character Generation Sheet

The application will allow users to create characters according to the ruleset used in the tabletop role-playing game, Pathfinder 2nd Edition.

Latest release's download page can be accessed by clicking [HERE](https://github.com/Regularmute/ot-harjoitustyo/releases/tag/loppupalautus).

List of all releases can be found [HERE](https://github.com/Regularmute/ot-harjoitustyo/releases)

## Current Features
---
  * The user can see the login and registration pages.
  * The user can create an account and store it into the database.
  * A registered user can login and logout.
  * A registered user is logged in automatically.
  * A logged user sees a list of their characters and can create new ones.
  * The created character is stored in a sqlite database.
  * A logged user can view their characters' details and edit them.
  * A logged user can delete characters.

## Documentation
---
Note: Some of the documentation has been written in Finnish. These are marked with [FI].

  * [Application's requirement specifications: Pathfinder 2e Character Sheet [FI]](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

  * [Logged hours spent on the application [FI]](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

  * [Changelog](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

  * [Architecture description [FI]](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

  * [User instructions [FI]](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

  * [Testing document [FI]](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)

## Installation
---
1. Install the dependencies with the command:
  ```console
    poetry install
  ```

2. Initialize the user and character databases with the command:
  ```console
    poetry run invoke create-database
  ```

3. Run the application with the command:
  ```console
    poetry run invoke start
  ```

## Console commands
---
### Initializing databases

You can initialize the User and Character databases with the command:
  ```console
    poetry run invoke create-database
  ```

### Running the application

You can run the application with the command:
  ```console
    poetry run invoke start
  ```

### Testing

You can run the tests with the command:
  ```console
    poetry run invoke test
  ```

### Linting

You can run pylint on src/ files with the command:
  ```console
    poetry run invoke lint
  ```

### Formatting

You can automatically format code files in src/ directory according to PEP8-standard with the following command:
  ```console
    poetry run invoke format
  ```

### Coverage report

You can check the test coverage and generate a .html form coverage report with the command:
  ```console
    poetry run invoke coverage-report
  ```
