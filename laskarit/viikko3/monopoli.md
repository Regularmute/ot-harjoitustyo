```mermaid
  classDiagram
    Monopoli "1"--"2..8" Pelaaja
    Monopoli "1"--"2" Noppa
    Monopoli "1"--"1" Pelilauta
    Pelaaja "1" -- "1" Pelinappula
    Pelilauta "1" -- "40" Ruutu
    Pelinappula "1" -- "1" Ruutu
    class Ruutu{
      getNextRuutu()
    }
```
