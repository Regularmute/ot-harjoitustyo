# Testaus

Ohjelmaa on testattu automaattisilla yksikkötesteillä unittestillä sekä manuaalisesti järjestelmätasolla.

## Yksikkötestaus

### Repositorioluokat

Tietokantoja käsittelevät `UserRepository` sekä `CharacterRepository`-luokat testataan erillisen tietokantatiedoston avulla, joka on määritelty .env.test-tiedostossa. Nämä testiluokat ovat [TestUserRepository](https://github.com/Regularmute/ot-harjoitustyo/blob/main/src/tests/repositories/user_repository_test.py) sekä [TestCharacterRepository](https://github.com/Regularmute/ot-harjoitustyo/blob/main/src/tests/repositories/character_repository_test.py).

## Järjestelmätestaus

