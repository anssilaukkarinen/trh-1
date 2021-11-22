# TRH-1


In English below.

**Suomeksi**

Tämän tietovaraston tarkoituksena on tarjota rakenteista tehtyjen lämpötilan (T) ja suhteellisen kosteuden (RH) mittausten pitkäkestoisia ja jatkuvatoimisia tulosaineistoja vapaasti hyödynnettäväksi. Tietovarasto sisältää myös python-koodin, joka toimii esimerkkinä tulosdatan lukemisesta ja analysoimisesta.

***Kansiorakenne***

"database_read_only"-kansiossa oleva data on tarkoitettu vain lukemista varten, eikä kyseiseen kansioon lisätä laskentatuloksia tai tuloskuvaajia. Kansion rakenne on seuraava:
- Rakennus
    - Jokaisesta mittausten kohteena olleesta rakennuksesta tehdään kansioon uusi alakansio, johon kyseisen rakennuksen kaikki mittaustulokset tulevat.
    - Tässä kansiossa on myös kuvailutiedosto, jossa on annettu yksittäisen rakennuksen tasolle liittyviä lähtötietoja, kuten sijaintipaikka halutulla tarkkuudella, maastoluokka, alkuperäinen rakennusvuosi ja rakennuksen pääasiallinen käyttötarkoitus.
- Rakenne
    - Kustakin rakenteesta tehdyt mittaukset tulevat omiin alakansioihinsa. Jos mittauksia on tehty useasta rakenteesta, niin tällöin kunkin rakenteen mittaustulokset tulevat omiin kansioihinsa.
    - Kunkin rakenteen kansioon tulee myös kuvailutiedosto, jossa annetaan tietoja kyseisestä rakenteesta ja sen mittauksista, kuten:
        - rakenteeseen rajautuvan huonetilojen käyttötarkoitus ja sanallinen kuvaus tyypillisistä olosuhteista
        - kerrosnumero maanpinnan tasoon nähden
        - mitatun rakenteen ilmansuunta
        - kuvaus rakenneratkaisusta materiaalikerroksineen ja kerrospaksuuksineen
        - rakenteen alkuperäinen rakennusvuosi ja mahdolliset korjausvuodet
        - mittalaitteisiin liittyvät tiedot, kuten mittalaitteen tyyppi sekä lämpötilan ja suhteellisen kosteuden standardiepävarmuudet.
- Mittauspisteet
    - Jokaiselta yksittäiseltä anturilta saatu T/RH-mittausdata tulee omiin csv-tiedostoihinsa. Jos/kun rakenteen olosuhteita on mitattu useasta mittauspisteetä, niin tällöin csv-tiedostoja on useita.
    - Jokaiseen rakennekansioon tulee myös omat csv-tiedostonsa mittausjaksolla vallinneista sisä- ja ulkoilman olosuhteista.
    - csv-tiedostojen rakenne:
        - Ensimmäinen sarake sisältää hetkellisten T/RH-mittausarvojen aikaleiman muodossa: "yyyy-mm-pp HH:MM:SS". Aikaleimasarakkeen otsikko on "t_UTC+2", jossa "+2" tarkoittaa Suomen normaaliaikaa (talviaikaa). Aikaleimasarakkeessa ilmoitetun UTC-ajan ja varsinaisten aikaleimojen tulee vastata toisiaan, eli kesäajan aikaleimat korjataan talviaikaan.
        - Lämpötilan sarakeotsikkona on "T" ja suhteellisen kosteuden "RH".
        - Mittauspisteen nimi on annettu csv-tiedoston nimenä.
    - Mittauspisteiden kuvailutiedoissa voidaan hyödyntää mahdollisuuksien mukaan seuraavia termejä:
        - "Rajapinta" tarkoittaa kahden materiaalipinnan tasomaista kosketuspintaa.
        - "Kulma" tarkoittaa kahden materiaalin viivamaista kohtaamispaikkaa, jossa tasomaiset materiaalikerrokset ovat toisiinsa nähden 90 asteen kulmassa.
        - "Nurkka" tarkoittaa kolmen materiaalin pistemäistä kohtaamispaikkaa.

Kansionimissä ja tiedostojen nimissä ei käytetä välilyöntejä, erikoismerkkejä tai ääkkösiä.

Tässä vielä esimerkki kansiorakenteesta:
```
database_read_only
- omakotitalo_1
  -- rakennuksen_tiedot.txt
  -- puurankaseina_1
     --- rakenteen_ja_mittauspisteiden_tiedot.txt
     --- sisailman_olosuhteet.csv
     --- ulkoilman_olosuhteet.csv TAI fmi_1.csv
     --- kulma_runkotolppa_ja_tuulensuojalevy.csv
     --- rajapinta_tuulensuojalevy_lammoneriste.csv
     --- kulma_alaohjauspuun_ylapinta_tuulensuojalevy.csv
  -- puurankaseina_2
     --- sisailma.csv
     --- ulkoilma.csv TAI fmi_1.csv
     --- kulma_runkotolppa_tuulensuojalevy.csv
     --- nurkka_ylatukipuun_alapinta_tuulensuojalevy_runkotolppa.csv
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

Tietokanta sisältää kahden tyyppistä dataa:
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
- Diffuusi auringonsäteily vaakapinnalle ("Rdif"), W/m2, edeltävän tunnin keskiarvo
- Globaali säteily vaakapinnalle ("Rglob"), W/m2, edeltävän tunnin keskiarvo
- Sateen määrä vaakapinnalle ("precip"), mm/h, edeltävän tunnin keskiarvo
- Tuulen nopeus ("ws"), m/s, hetkellinen arvo
- Tuulen suunta ("wd"), deg, hetkellinen arvo, 90 deg = tuuli idästä, 180 deg = tuuli etelästä

Lisätietoja (mukaan lukien datojen luovutus tietopankkiin): Anssi Laukkarinen, anssi.laukkarinen@tuni.fi



**In  English**

The purpose of this repository is to provide open data access to temperature (T) and relative humidity (RH) measurement data from building envelope structures. The repository contains an example code on the different possibilities on how the T/RH conditions in a single measurement point could be analysed.

***Folder structure***

The folder "database_read_only" is meant to be read-only. No analysis data or figures are intended to be put here. The structure of the folder is as follows:
- Building
    - New folder is created for every new building where measurements have been made.
    - The building-level folder contains also a text file, that contains metadata on the building, such as location, terrain category, year of construction and the main purpose of use.
- Structure
    - Data from each measured structure is put into separate folders. If measurements have been conducted from multiple structures within a building, then new folder is created for each structure.
    - Each structure-level folder contain also a metadata text file, that contains information on that specific structure and the factors related to that structure and its measurements. The structure-level metadata file contains:
        - a short description of the purpose and typical conditions of the room/zones to which the structure is adjacent to
        - floor number of the structure above the ground level
        - facade orientation
        - list of material layers in the structure, i.e. at least material names and layer thicknesssess
        - the original construction year of the structure and possible retrofitting years
        - information related to the measurement equipemtn, such as equipment manufacturer and model and standard uncertainties.
- Measurement points
    - Measurement dat from each sensor is put into separate csv files. If there were multiple sensors/probes, then multiple csv files are put into the folder.
    - CSV files are also put to the structure-level folder on the indoor and outdoor conditions during the measurements (two files)
    - The formatting of the csv files:
        - The first column contains the time stamps for the instantaneous T/RH readings. The time stamps are formatted as: "yyyy-mm-dd HH:MM:SS". The column header for the time stamps is of the format: "t_UTC+x", where "+x" means the different to UTC time (for Finnish normal time this would be: "t_UTC+2", without the quotes. The UTC-time in the column header and the actual time stamps must match.
        - The column header for temperature is "T" and for relative humidity "RH".
        - A unique name of the measurement point is given as the name of the csv file.
    - The following terminology can be utilised when describing and placement of the measurement points:
        - "Interface" for the plane-like surface between two adjacent materials.
        - "Line" for the linear line-like contact point of two material surfaces, where the materials meet each other at 90 degree angle
        - "Corner" for the point-like contact point of three material surfaces.

Do not use scandinavian alphabets, special characters or white space in folder or file names.

Here is an example of the folder structure:
```
database_read_only
- single_family_house_1
  -- information_building.txt
  -- timber_frame_wall
     --- information_on_the_structure_and_measurements.txt
     --- indoor_conditions.csv
     --- outdoor_conditions.csv OR fmi_1.csv
     --- line_timber_stud_windbarrier.csv
     --- interface_windbarrier_thermal_insulation.csv
  -- timber_frame_wall_2
     --- indoors.csv
     --- outdoors.csv OR fmi_1.csv
     --- line_bottom_plate_windbarrier.csv
  -- betonisandwich_1
     --- information_structure_measurement_points.txt
     --- ...
     
- school_1
  -- info_building.txt
  -- brick_wall_1.csv
     --- ...
```

The script: "example.py" shows a simple example on how to analyse the measurement results. The example uses the class "trh-py", in which a basic set of performance indicators and plots. The class requires also data on the indoor and outdoor air conditions.

***License***

The repository contains two types of data:
- Temperature and relative humidity measurement data from building envelope structures and the related metadata. This data has been collected as a joint effort of multiple stakeholders in the building sector.
- Meteorological observation data collected by The Finnish Meteorological Institute (FMI) or other similar organisation. The main time series here are for outdoor air temperature and relative humidity, but other data can be also included.

The data related to structures is available according to the Creative Commons CC-BY 4.0 license. Here is a link to the license:

https://creativecommons.org/licenses/by/4.0/

You may use the materials freely for commercial and non-commercial use, but attribution to the original data source ("TRH-database") must be given. Guarantees of any kind for correctedness, suitability or other is not given. If you want to submit data to be added to the repository (primarily cold climate data is most welcome!), then the same license conditions must be given to them.

The Finnish Meteorological Institute (FMI) provides access to observation data through their open data service and the data is freely available according to the CC-BY 4.0 license:

https://en.ilmatieteenlaitos.fi/open-data-licence

The data from the FMI must be placed into separate csv-files, where the file name contains the "fmi" identifier. These csv-files may contain also other data besides outdoor air T and RH, such as solar and longwave radiation, wind and precipitation. The format of these csv files is otherwise the same as described previously, i.e. a time stamp column as the left-most column and climatic variables as comma-separated values to the right of it. If data from FMI is used, then this is mentioned in the structure description file, along with a link to the open data service, date of retrieval and a notice, if the data has been modified.


Units:
- Temperature ("T"), degC, instantaneous value
- Relative humidity ("RH"), 0-100 %, instantaneous value, given with respect to liquid water
- Diffuse solar radiation on a horizontal surface ("Rdif"), W/m2, mean flux for the previous hour
- Global horizontal solar radiation ("Rglob"), W/m2, mean flux for the previous hour
- The amount of rain on a horizontal surface ("precip"), mm/h, mean value for the previous hour
- Wind speed, m/s, instantaneous value
- Wind direction, deg, 90 = from east, 180 = from south, instantaneous value.

For more information contact: Anssi Laukkarinen, anssi.laukkarinen@tuni.fi


