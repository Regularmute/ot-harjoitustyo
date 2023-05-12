# Vaatimusmäärittely - Pathfinder2E hahmogeneraattori

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi luoda Pathfinder2E-pöytäroolipeliin sopivan pelihahmon lomakkeen, tallentaa sen ja muokata sitä myöhemmin. Usea rekisteröitynyt käyttäjä voi käyttää sovellusta, joista jokaisella on omat hahmolomakkeensa.

## Käyttäjät

Sovelluksella on tällä hetkellä ainoastaan yksi käyttäjärooli _pelaaja_. Sovelluksen kehityksen edetessä saatetaan lisätä rooli _Pelinjohtaja_, jolla on suuremmat oikeudet (esimerkiksi mahdollisuus nähdä kaikkien pelaajien hahmot ja muokata niitä).

## Sovelluksen perustoiminnallisuudet

### Ennen kirjautumista

* Käyttäjä voi luoda järjestelmään oman tunnuksen. (tehty)
  * Käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä pitkä. (tehty)
  * Salasanan tulee olla vähintään 6 merkkiä pitkä (tehty)
  * Käyttäjä kirjautuu automaattisesti sisään onnistuneen rekisteröitymisen jälkeen (tehty)
* Käyttäjä voi kirjautua sisään järjestelmään omalla tunnuksellaan. (tehty)
  * Käyttäjän tulee kirjautua omalla käyttäjätunnuksellaan sekä oikealla salasanalla. (tehty)
    * Virheellisellä syötteellä sovellus palauttaa virheilmoituksen. (tehty)

### Kirjautumisen jälkeen

* Käyttäjä näkee listan hahmoistaan (tehty)
* Käyttäjä näkee oman hahmolomakkeensa (tehty)
  * Hahmolomake säilyttää monen tyyppistä tietoa:
    * Nimi (tehty)
    * Syntyperä (tehty)
    * Perimä (tehty)
    * Taso (tehty)
    * Kokemuspisteet (tehty)
    * Vahinkopisteet (tehty)
    * Muuta mahdollista (mahdollisesti tulevaisuudessa)
* Käyttäjä voi muokata hahmolomakettaan ja tallentaa muutokset (tehty)
* Käyttäjä voi kirjautua ulos järjestelmästä (tehty)
* Käyttäjä pystyy poistamaan hahmolomakkeita (tehty)

### Jatkokehitysmahdollisuuksia

Sovelluksen alkuversion valmistuttua on mahdollista laajentaa sovelluksen toimintaa mm. seuraavilla ominaisuuksilla:

* Käyttäjä voi ylläpitää ja luoda useita hahmolomakkeita. (tehty)
* Sovellukseen voidaan lisätä käyttäjärooli _Pelinjohtaja_, jolla on enemmän oikeuksia kuin normaalilla käyttäjällä.
* Osat hahmolomakkeesta voidaan täyttää automaattisesti, esimerkiksi kentät jotka pystytään laskemaan matemaattisesti muista kentistä.
* Käyttäjäjoukot, joiden jäsenet näkevät toistensa hahmolomakkeet.
* Lomake voi avustaa käyttäjää täyttämään lomakkeen esim. ehdotuksilla tai viitteillä Pathfinder 2E - sääntöihin
