# TRH-1


In English below.

**Suomeksi**

Tämän tietovaraston tarkoituksena on tarjota rakenteista tehtyjen lämpötilan (T) ja suhteellisen kosteuden (RH) mittausten tulosaineistoja vapaasti hyödynnettäväksi. Tietovarasto sisältää myös python-koodin, joka toimii esimerkkinä tulosdatan lukemisesta ja analysoimisesta.

***Kansiorakenne***

"database_read_only"-kansiossa oleva data on tarkoitettu vain lukemista varten, eikä kyseiseen kansioon lisätä laskentatuloksia tai tuloskuvaajia. Kansion rakenne on seuraava:
- Rakennus
    - Jokaisesta mittausten kohteena olleesta rakennuksesta tehdään kansioon uusi alakansio, johon kyseisen rakennuksen kaikki mittaustulokset tulevat.
    - Tässä kansiossa on myös kuvailutiedosto, jossa on annettu yksittäisen rakennuksen tasolle liittyviä lähtötietoja, kuten sijaintipaikka halutulla tarkkuudella, maastoluokka, alkuperäinen rakennusvuosi ja rakennuksen pääasiallinen käyttötarkoitus.
- Rakenne
    - Kustakin rakenteesta tehdyt mittaukset tulevat omiin alakansioihinsa. Jos mittauksia on tehty useasta rakenteesta, niin tällöin kunkin rakenteen mittaustulokset tulevat omiin kansioihinsa.
    - Kunkin rakenteen kansioon tulee myös kuvailutiedosto, jossa annetaan tietoja kyseisestä rakenteesta ja sen mittauksista, kuten mitatun rakenteen ilmansuunta, kuvaus rakenneratkaisusta materiaalikerroksineen ja kerrospaksuuksineen sekä rakenteen alkuperäinen rakennusvuosi ja mahdolliset korjausvuodet. Tässä tiedostossa annetaan myös mittalaitteisiin liittyvät tiedot, kuten mittalaitteen tyyppi sekä lämpötilan ja suhteellisen kosteuden standardiepävarmuudet.
- Mittauspisteet
    - Jokaiselta yksittäiseltä anturilta saatu T/RH-mittausdata tulee omiin csv-tiedostoihinsa. Jos/kun rakenteen olosuhteita on mitattu useasta mittauspisteetä, niin tällöin csv-tiedostoja on useita.
    - Jokaiseen rakennekansioon tulee myös omat csv-tiedostonsa mittausjaksolla vallinneista sisä- ja ulkoilman olosuhteista.
    - Kunkin mittauspisteen mittaustulokset sisältävien csv-tiedostojen ensimmäisessa sarakkeessa on aikaleima muodossa: "yyyy-mm-pp HH:MM:SS". Aikaleimasarakkeen otsikko on "t_UTC+2", jossa "+2" tarkoittaa Suomen normaaliaikaa (talviaikaa). Aikaleimasarakkeessa ilmoitetun UTC-ajan ja varsinaisten aikaleimojen tulee vastata toisiaan. Suhteellisen kosteuden sarakeotsikkona on "RH" ja lämpötilan "T". Mittauspisteen nimi on annettu csv-tiedoston nimenä.

Kansionimissä ja tiedostojen nimissä ei käytetä välilyöntejä, erikoismerkkejä tai ääkkösiä.

Tässä vielä esimerkki kansiorakenteesta:
```
database_read_only
- omakotitalo_1
  -- rakennuksen_tiedot.txt
  -- puurankaseina_1
     --- rakenteen_ja_mittauspisteiden_tiedot.txt
     --- sisailman_olosuhteet.csv
     --- ulkoilman_olosuhteet.csv OR fmi_1.csv
     --- runkotolpan_ja_tuulensuojalevyn_nurkka.csv
     --- tuulensuojan_sisapinta.csv
     --- alaohjauspuun_ylapinta.csv
  -- puurankaseina_2
     --- sisailma.csv
     --- ulkoilma.csv OR fmi_1.csv
     --- runkotolpan_ja_tuulensuojalevyn_nurkka.csv
     --- ylatukipuun_alapinta.csv
  -- betonisandwich_US_1
     --- rakenteen_ja_mittauspisteiden_tiedot.txt
     --- ...
     
- koulurakennus_1
  -- rakennuksen_tiedot.txt
  -- tiiliseina_1.csv
     --- ...
```

"example.py" -tiedosto sisältää esimerkin mittausdatojen käyttämisestä. Esimerkki kutsuu "trh.py"-luokkaa, jossa on toteutettuna peruspaketti yksittäisen mittauspisteen T/RH-olosuhteiden analysoinnista suhteessa sisä- ja ulkoilman olosuhteisiin.

***Käyttöoikeustietoja***

Tietokanta sisältää dataa kahdesta lähteestä:
- Rakenteista tehtyjä T/RH-mittauksia sekä näiden metadataa. Tämä data on koottu useiden eri rakennusalan toimijoiden toimesta.
- Ilmatieteen laitoksen sääasemien havaintodataa.

Rakenteisiin liittyvä mittausdata on vapaasti saatavilla CC-BY 4.0 -lisenssin mukaisesti. Linkki lisenssiin:
https://creativecommons.org/licenses/by/4.0/deed.fi

Voit käyttää materiaaleja vapaasti kaupallisiin ja ei-kaupallisiin tarkoituksiin, mutta muista nimetä lähde ("TRH-tietokanta"). Minkäänlaista takuuta datan oikeellisuudesta tai soveltuvuudesta ei anneta. Jos haluat luovuttaa mittausaineistoja tietokannan osaksi (mikä on sangen tervetullutta!), niin tällöin tietokantaan lisättäville aineistoille tulee hyväksyä nämä samat käyttöehdot.

Ilmatieteen laitoksen data on saatavilla Ilmatieteen laitoksen Avoin data -palvelusta ja on vapaasti käytettävissä CC-BY 4.0 -lisenssin mukaisesti:
https://www.ilmatieteenlaitos.fi/avoin-data-lisenssi

Ilmatieteen laitoksen havaintoasemien mittausdata on eriytetty muusta datasta käyttämällä kyseisen datan sisältävän csv-tiedoston nimessä "fmi"-tunnusta. Kyseiset tiedostot voivat sisältää T/RH-tietojen lisäksi myös muita havaintosuureita omissa sarakkeissaan. Jos Ilmatieteen laitoksen avointa dataa on käytetty mainitaan tämä structure.txt -tiedostossa, sisältäen viittauksen Ilmatieteen laitoksen Avoin data -palveluun datan hakuajankohdan ja ilmoituksen, jos dataa on muokattu.

Suureet ja yksiköt
- Lämpötila ("T"), degC, hetkellinen arvo
- Suhteellinen kosteus ("RH") nestemäisen veden suhteen , 0-100 %, hetkellinen arvo

Lisätietoja (mukaan lukien datojen luovutus tietopankkiin): Anssi Laukkarinen, anssi.laukkarinen@tuni.fi




**In  English, to be updated**

The primary purpose of this repository is to provide temperature (T) and relative humidity (RH) measurement data from building envelope structures. The repository gives also an example python code that reads in part of the data and makes figures and calculates performance indicators from it. The general goal is to develop the database and the analysis methods forward to create a better understanding on the heat and moisture behaviour of building envelope structures.

The folder: "database_read_only" includes data from two main sources:
- Measurement data from building structures, gathered by various stakeholders in the Finnish building sector
- Climatic data from the Finnish Meteorological Institute, gathered at various weather stations.

The measurement data from structures is available freely for commercial and non-commercial use according to the CC BY 4.0 licence:
https://creativecommons.org/licenses/by/4.0/

The acknowledgement of the data source ("TRH database") is required. No quanrantees whatsoever is given for the accuracy, correctness or suitability of the data for any purposes. Any person or organization committing data to the database must accept the use of these conditions.

This data is in the "trh" folders.

The data from the Finnish Meteorological Institute is subjected to the open data licence "Create Commons Attribution 4.0 International licence", i.e. CC-BY 4.0. See more:
https://en.ilmatieteenlaitos.fi/open-data-licence

This data is in the "fmi" folders.


Units:
- Temperature ("T"), degC, instantaneous value
- Relative humidity ("RH"), 0-100 %, instantaneous value, given with respect to liquid water
- Diffuse solar radiation on a horizontal surface ("Rdif"), W/m2, mean flux for the previous hour
- Global horizontal solar radiation ("Rglob"), W/m2, mean flux for the previous hour
- The amount of rain on a horizontal surface ("precip"), mm/h, mean value for the previous hour
- Wind speed, m/s, instantaneous value
- Wind direction, deg, 90 = from east, 180 = from south, instantaneous value.

For more information contact: Anssi Laukkarinen, anssi.laukkarinen@tuni.fi


