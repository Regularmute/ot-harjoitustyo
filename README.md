# Pathfinder 2E Character Generation Sheet

The application will allow users to create characters according to the ruleset used in the tabletop role-playing game, Pathfinder 2nd Edition.

## Current Features
---
  * The user can see the login and registration pages.
  * The user can create an account and store it into the database.
  * A registered user can login and logout.
  * A registered user is logged in automatically
  * A logged user is greeted with a personalized message

## Documentation
---
  * [Sovelluksen vaatimusmäärittely: Pathfinder 2e Hahmolomake](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

  * [Sovelluksen tuntikirjanpito](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

  * [Changelog](https://github.com/Regularmute/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Installation
---
1. Install the dependencies with the command:
  ```console
    poetry install
  ```

2. Initialize the user database with the command:
  ```console
    poetry run invoke create-database
  ```

3. Run the application with the command:
  ```console
    poetry run invoke start
  ```

## Console commands
---
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
