In English below.

***Käyttöoikeustietoja***

Tietokanta sisältää kolmen tyyppistä dataa:
- Rakenteista tehtyjä T/RH-mittauksia sekä näiden metadataa. Tämä data on koottu useiden eri rakennusalan toimijoiden toimesta.
- Ilmatieteen laitoksen sääasemien havaintodataa.
- Yksi tai useampia ohjelmakoodiesimerkkejä datan lukemisesta ja analysoimisesta.

Rakenteisiin liittyvä mittausdata on vapaasti saatavilla CC-BY 4.0 -lisenssin mukaisesti. Linkki lisenssiin:

https://creativecommons.org/licenses/by/4.0/deed.fi

Voit käyttää rakenteiden mittausaineistoja vapaasti kaupallisiin ja ei-kaupallisiin tarkoituksiin, mutta muista nimetä lähde ("TRH-tietokanta"). Minkäänlaista takuuta datan oikeellisuudesta tai soveltuvuudesta ei anneta. TRH-tietokanta ja siihen kontribuoineet tahot eivät myöskään ole millään lailla vastuussa mahdollisista menetyksistä, oikeudenkäynneistä, vaateista, kanteista, vaatimuksista, tai kustannuksista taikka vahingosta, olivat ne mitä tahansa tai aiheutuneet miten tahansa, johtuen joko suoraan tai välillisesti yhteydestä tietokannassa esitettyihin aineistoihin.

Jos haluat luovuttaa mittausaineistoja tietokannan osaksi (mikä on sangen tervetullutta!), niin tällöin tietokantaan lisättäville aineistoille tulee hyväksyä nämä samat käyttöehdot.

Ilmatieteen laitoksen data on saatavilla Ilmatieteen laitoksen Avoin data -palvelusta ja on vapaasti käytettävissä CC-BY 4.0 -lisenssin mukaisesti:

https://www.ilmatieteenlaitos.fi/avoin-data-lisenssi

Ilmatieteen laitoksen havaintoasemien mittausdata on eriytetty muusta datasta käyttämällä kyseisen datan sisältävän csv-tiedoston nimessä "fmi"-tunnusta. Kyseiset tiedostot voivat sisältää T/RH-tietojen lisäksi myös muita havaintosuureita omissa sarakkeissaan. Jos Ilmatieteen laitoksen avointa dataa on käytetty mainitaan tämä structure.txt -tiedostossa, sisältäen viittauksen Ilmatieteen laitoksen Avoin data -palveluun datan hakuajankohdan ja ilmoituksen, jos dataa on muokattu.

TRH-tietokannan yhteydessä esitetyt ohjelmakoodiesimerkit ovat käytettävissä MIT-lisenssin mukaisesti. MIT-lisenssin lisenssiteksti on tämän tiedoston lopussa.

---

***License***

The repository contains three types of data:
- Temperature and relative humidity measurement data from building envelope structures and the related metadata. This data has been collected as a joint effort of multiple stakeholders in the building sector.
- Meteorological observation data collected by The Finnish Meteorological Institute (FMI) or other similar organisation. The main time series here are for outdoor air temperature and relative humidity, but other data can be also included.
- One or multiple code examples on how to read and analyse the data.

The data related to structures is available according to the Creative Commons CC-BY 4.0 license. Here is a link to the license:

https://creativecommons.org/licenses/by/4.0/

You may use the T/RH data from structures freely for commercial and non-commercial use, but attribution to the original data source ("TRH-database") must be given. Guarantees of any kind for correctedness, suitability or other is not given. The database or its contributors shall not also be held liable in any way for any kind of losses or consequences that might have have either directly or indirectly from the use of the material in the TRH-database. If you want to submit data to be added to the repository (primarily cold climate data is most welcome!), then the same license conditions must be given to them.

The Finnish Meteorological Institute (FMI) provides access to observation data through their open data service and the data is freely available according to the CC-BY 4.0 license:

https://en.ilmatieteenlaitos.fi/open-data-licence

The data from the FMI must be placed into separate csv-files, where the file name contains the "fmi" identifier. These csv-files may contain also other data besides outdoor air T and RH, such as solar and longwave radiation, wind and precipitation. The format of these csv files is otherwise the same as described previously, i.e. a time stamp column as the left-most column and climatic variables as comma-separated values to the right of it. If data from FMI is used, then this is mentioned in the structure description file, along with a link to the open data service, date of retrieval and a notice, if the data has been modified.

The code example(s) are avaiable under the MIT license (see below).


"""

MIT License

Copyright (c) 2021 Anssi Laukkarinen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
