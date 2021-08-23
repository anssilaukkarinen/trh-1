# TRH-1


In English below.

**Suomeksi**

Tämän tietovaraston tarkoituksena on tarjota rakenteista tehtyjen lämpötilan (T) ja suhteellisen kosteuden (RH) mittausten tulosaineistoja vapaasti hyödynnettäväksi. Tietovarasto sisältää myös python-koodin, joka toimii esimerkkinä tulosdatan lukemisesta ja analysoimisesta.

"database_read_only"-kansio sisältää dataa kahdesta lähteestä:
- Rakenteista tehtyjä T/RH-mittauksia sekä näiden metadataa. Tämä data on koottu useiden eri rakennusalan toimijoiden toimesta.
- Ilmatieteen laitoksen sääasemien havaintodataa.

Rakenteisiin liittyvä mittausdata on vapaasti saatavilla CC-BY 4.0 -lisenssin mukaisesti. Linkki lisenssiin:
https://creativecommons.org/licenses/by/4.0/deed.fi

Voit käyttää materiaaleja vapaasti kaupallisiin ja ei-kaupallisiin tarkoituksiin, mutta muista nimetä lähde ("TRH-tietokanta"). Minkäänlaista takuuta datan oikeellisuudesta tai soveltuvuudesta ei anneta. Jos haluat luovuttaa mittausaineistoja tietokannan osaksi (mikä on sangen tervetullutta!), niin tällöin tietokantaan lisättäville aineistoille tulee hyväksyä nämä samat käyttöehdot. Tämä data on "trh"-kansioissa.

Ilmatieteen laitoksen data on sijoitettu "fmi"-kansioihin ja se on vapaasti käytettävissä CC-BY 4.0 -lisenssin mukaisesti:
https://www.ilmatieteenlaitos.fi/avoin-data-lisenssi

Suureet ja yksiköt
- Lämpötila ("T"), degC, hetkellinen arvo
- Suhteellinen kosteus ("RH") nestemäisen veden suhteen , 0-100 %, hetkellinen arvo
- Diffuusi auringonsäteily vaakapinnalle ("Rdif"), W/m2, edellisen tunnin keskimääräinen vuo
- Globaali auringonsäteily vaakapinnalle ("Rglob"), W/m2, edellisen tunnin keskimääräinen vuo
- Sateen kokonaismäärä vaakapinnalle ("precip"), mm/h, edellisen tunnin keskiarvo
- Tuulen nopeus ("ws"), m/s, hetkellinen arvo
- Tuulen suunta ("wd"), deg, pohjoisesta myötäpäivään lukien, 90 = idastä, 180 = etelästä.

Lisätietoja (mukaan lukien datojen luovutus tietopankkiin): Anssi Laukkarinen, anssi.laukkarinen@tuni.fi




**In  English**

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


