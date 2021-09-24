- [Applications of machine learning in drug discovery and development yleiskatsaus ja nosteita](#applications-of-machine-learning-in-drug-discovery-and-development-yleiskatsaus-ja-nosteita)
  - [käyttökohteet](#käyttökohteet)
  - [hidasteet/puutteet](#hidasteetpuutteet)
  - [tärkeitä nosteita](#tärkeitä-nosteita)
  - [koneoppimisesta](#koneoppimisesta)
  - [Neuroverkoista](#neuroverkoista)
    - [Eri neurtoverkkoja ja niiden toiminnalliset erot](#eri-neurtoverkkoja-ja-niiden-toiminnalliset-erot)
  - [Datan laadusta ja määrästä](#datan-laadusta-ja-määrästä)
  - [Käytännön kohteet lääkkeiden löytmisessä/kehityksessä](#käytännön-kohteet-lääkkeiden-löytmisessäkehityksessä)
  - [Yleiskatsaus](#yleiskatsaus)
  - [Selvitettäviä asioita](#selvitettäviä-asioita)

# Applications of machine learning in drug discovery and development yleiskatsaus ja nosteita

## käyttökohteet
*  kohteen varmentaminen
*  Biomerkin tunnistaminen
*  kliinisistä testeistä kerätyn patologisen datan analyysia

## hidasteet/puutteet
*  tulosten tulkitsemisen heikkous
*  tulosten toistettavuus

## tärkeitä nosteita
*  Korkea laatuisen datan tarve
*  Koneoppimismallien validointi

## koneoppimisesta

* Käytetään ohjattuja ja ohjaamattomia malleja
   *  ohjattuja, kun halutaan luokitella näytteitä ja ennustaa tulevia näytteitä
   *  ohjaamattomia, kun etsitään ryppäitä datasta
* Käyttettävä malli on valittava käyttökohteen mukaan
Eri malleja vertaillaan usean eri metriikan perusteella, esim. ryhmittely tarkkuus, kappa -arvo, logaritminen ero...
* CPU -> GPU -> TPU

## Neuroverkoista
### Eri neurtoverkkoja ja niiden toiminnalliset erot
*  Convolutional neural networks (CNN)
*  Recurrent neural network (RNN)
*  feedforward network
*  Deep autoencoder network (DAEN)

## Datan laadusta ja määrästä
*  Tulee olla tarkistettua, tarkkaa ja tarpeeksi kuvaavaa
*  Mallia suunniteltaessa mietittävä, mikä on tarpeeksi dataa
*  Useat käytännön koneet eivät suoriudukkaan tehtävästään hyvin, koska
niiden koulutukseen tai niiden käsittelemä data vaihtelee laadultaan

## Käytännön kohteet lääkkeiden löytmisessä/kehityksessä
*  Koneoppimista on jo käytetty useassa tutkimuksessa tunnistamaan ja luokittelemaan
dataa näytteistä
*  NLP -mementelmiä hyödynnetään aineiston etsinnässä. Aineistoa voidaan etsitä
lääke-sairaus, geeni-sairaus ja kohde-lääke konteksteissa
*  Voidaan käyttää syöpäkohtaisten lääkkeiden etsinnässä. Koulutetaan malli hyödyntäen
kerättyä dataa ja ennustetaan eri lääkkeiden vaikutusta
*  Yksi suurimmista tavoitteista koneoppimisen hyödyntämisessä on ennustaa, mitkä lääkkeet tulevat
menestymään kliinisissä kokeissa
*  Koneoppimista on myös hyödynnetty pienten kemiallisten yhdisteiden suunnittelussa.
   * Multitask -mallit ovat osoittautuneet tehokkaammiksi kuin singletask -mallit, mutta ne ovat hyvin datan laadusta riippuvaisia
   * Neuroverkkoja ja nykyisiä hakupuualgoritmeja voidaan käyttää kemiallisen aineen syntesoinnin välivaiheiden suunnittelussa
   * De novo yhdisteiden suunnittelussa
   * Suuri kysymys on, kuinka pieniä molekyylejä/yhdisteitä kuvataan, esim. circular fingerprint, symmetry functions
*  Biologisten indikaattoreiden tunnistaminen
   * menetelmiä on käytetty indikaattoreiden tunnistamiseen
   * Useita ei ole kuitenkaan otettu käyttöö
   * mallien tulosten heikko tulkittavuus ja mallien validointi useiden instituutioiden kontekstissa ovat hidasteita suurempaan käyttöönottoon

## Yleiskatsaus
* Voi johtaa kehitykseen henkilökohtaisten räätälöityjen lääkkeiden osalta
  * Käytetty elektronisissa potilasasiakirjoissa, joka on mahdollistanut kliinisten kokeiden parantamisen ja kliinisen kokeen kelpaavuuden todentamisen
  * Terveydellistä dataa keräävien laitteiden yleistyminen (Wearables)
* Tärkeitä tunnettuja ongelmia
  * Mallien tulosten tulkittavuus
    * Miten/mitä reittiä kone päätyi tulokseensa?
    * Luottaako potilas tässä tilanteessa ennemmin koneen vai lääkärin antamaa diagnoosia? / Luottaako yritys koneen antamaan ennusteeseen lääkkeestä ja sen tominnasta?
    * Lisenssi ongelmat. Kuka omistaa koneen kehittämän lääkkeen?
  * Koneiden tulosten toistettavuus
    * Koneiden tulokset ovat hyvin riippuvaisia verkon alkuparametreista ja jopa siitä, missä järjestyksessä data syötetään koneelle
    * Antaako sama kone aina saman tulosteen samalle datalle?
  * Paikoittainen hyvän datan puute
    * Koneet ovat riippuvaisia datasta
    * Tarvittava datan määrä riippuu käyttökohteesta/tutkittavasta asiasta -> Voi olla kallista tuottaa tarvittava määrä dataa
  * Osaavan henkilöstön puute

## Selvitettäviä asioita 
* Biomarkers
* machine learning evaluation methods
* kappa metric
* de novo molecular design
* ex vivo and in vivo models