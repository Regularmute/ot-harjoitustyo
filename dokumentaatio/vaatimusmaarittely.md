# Vaatimusmäärittely - Pathfinder2E hahmogeneraattori

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi luoda Pathfinder2E-pöytäroolipeliin sopivan pelihahmon lomakkeen, tallentaa sen ja muokata sitä myöhemmin. Usea rekisteröitynyt käyttäjä voi käyttää sovellusta, joista jokaisella on oma hahmolomakkeensa.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli _pelaaja_. Sovelluksen kehityksen edetessä saatetaan lisätä rooli _Pelinjohtaja_, jolla on suuremmat oikeudet (esimerkiksi mahdollisuus nähdä kaikkien pelaajien hahmot ja muokata niitä).

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

* Käyttäjä näkee oman hahmolomakkeensa
  * Hahmolomake säilyttää monen tyyppistä tietoa:
    * Merkkijonoja: esim. hahmon nimi, pelaajan nimi, kykyjen (featien) nimet ja selitykset, kosmeettiset tiedot
    * Kokonaislukuja: esim. hahmon attribuuttipisteet, hahmon taso
* Käyttäjä voi muokata hahmolomakettaan ja tallentaa muutokset
* Käyttäjä voi kirjautua ulos järjestelmästä (tehty)

### Jatkokehitysmahdollisuuksia

Sovelluksen alkuversion valmistuttua on mahdollista laajentaa sovelluksen toimintaa mm. seuraavilla ominaisuuksilla:

* Käyttäjä voi ylläpitää ja luoda useita hahmolomakkeita.
* Sovellukseen voidaan lisätä käyttäjärooli _Pelinjohtaja_, jolla on enemmän oikeuksia kuin normaalilla käyttäjällä.
* Osat hahmolomakkeesta voidaan täyttää automaattisesti, esimerkiksi kentät jotka pystytään laskemaan matemaattisesti muista kentistä.
* Käyttäjäjoukot, joiden jäsenet näkevät toistensa hahmolomakkeet.
* Lomake voi avustaa käyttäjää täyttämään lomakkeen esim. ehdotuksilla tai viitteillä Pathfinder 2E - sääntöihin
