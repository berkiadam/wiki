# Engine rebuild

* Van egy Range Rover Evoque 2016-om ezzel a motorral: 2.0 TD4 / AJ20D4 Ingenium
* A 4-es dugattyú picit lötyög, és erős kattogó hangot ad már alapjáraton is. Feltehetőleg a hajtókar csapágy oda lett. 
* a motoron túrbót cseréltek, és ez után az első autópálya menet után, kb 300 km után elkezdődött a kattogás, úgy hogy összefügghet. 
  * vagy a sérült túrbóból ment szennyeződés az olajba
  * vagy a turbó olaj éhezés miatt halt meg,  pl mert a puma elégtelen, és most a motor csapágyak is belehaltak. 
* Az az elsődleges terv, hogy kivesszük a motort, fejre fordítjuk, leszedjük az olaj teknőt és megnézzük milyen állapotban van a főtengely, a hajtókar, és a blokk. Ha a blokk nem sérült, akkor veszünk egy rebuild kit-et és kicseréljük a sérült hajtókart és a főtengelyt és a csapágyakat. 

* Ehhez keresünk szerszámokat és rebuild kit-eket. A rebuild kit csak megbízható angol boltból jöhet. 




## Rebuild kits: 

> **WARNING**: csak olyan főtengelyt szabad venni, aminek rajta van a végén a fogaskerék. 

> **WARNING**: Figyelni kell rá, hogy a single turbohoz legyen való, mert a biturbós változatban a hajtókar vastagabb. 


https://www.ebay.com/itm/406397216275

![](docs/image-2026-07-01-23-13-12.png)

- olajpuma
- főtengely with gear
- timing set


## Szerszámok: 


## Meghúzási nyomatékok és sorrendek (Torque Specifications & Sequences)

A 2.0 TD4 / 204DTD Ingenium motor újjáépítéséhez szükséges gyári nyomatékértékek és meghúzási sorrendek az alábbiak szerint érhetőek el a gyári kézikönyvekből (a helyi `/home/adam/Insync/lalilali96@gmail.com/Google Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE - INGENIUM I4 2.0L DIESEL/ENGINE/` könyvtárból):

### 1. Főtengely fekvőcsapágy csavarok (Crankshaft Main Bearing Cap Bolts)
*   **Nyomatékok:**
    *   Stage 1: **25 Nm**
    *   Stage 2: **58 Nm**
    *   Stage 3: **135°**
    *   Stage 4: **Lazítás** (Loosen retaining bolts - teljesen vissza kell lazítani)
    *   Stage 5: **25 Nm**
    *   Stage 6: **37 Nm**
    *   Stage 7: **135°**
    *(Megjegyzés: Mindig új csavarok beépítése kötelező!)*
*   **Sorrend:**
    *   A gyári manualok nem tartalmaznak külön bottom-end fűzési ábrát. A csapágyfedelek **1-től 5-ig számozottak**, és a rajtuk lévő nyilaknak a motor eleje felé kell mutatniuk a beépítéskor.
*   **Gyári forrásfájl:** [SPECIFICATIONS.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/SPECIFICATIONS.pdf) (és a mester [ENINGE-Joined.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/ENINGE-Joined.pdf)).

### 2. Hajtókarcsapágy csavarok (Connecting Rod Cap Bolts)
*   **Nyomatékok:**
    *   Stage 1: **20 Nm**
    *   Stage 2: **125°**
*   **Sorrend:**
    *   Nincs külön megadott sorrend (hajtókaronként 2 db csavar rögzíti a fedelet, ezeket egyenletesen kell lehúzni). A fedelek töréses illesztésűek (fracture split), nem felcserélhetőek.
*   **Gyári forrásfájl:** [SPECIFICATIONS.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/SPECIFICATIONS.pdf) (és a mester [ENINGE-Joined.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/ENINGE-Joined.pdf)).

### 3. Hengerfej csavarok (Cylinder Head Bolts)
*   **Nyomatékok (többlépcsős lehúzás és lazítás):**
    1.  **Kezdeti meghúzás:** Stage 1: **10 Nm** $\rightarrow$ Stage 2: **20 Nm** $\rightarrow$ Stage 3: **53 Nm**
    2.  **Lazítás és újra-lehúzás:** Stage 1: Lazítás **180°-kal** (fél fordulat) $\rightarrow$ Stage 2: Meghúzás **53 Nm-re**
    3.  **Végső szögrefeszítés:** Stage 1: **90°** $\rightarrow$ Stage 2: **120°**
    *(Megjegyzés: 10 db új csavar beépítése kötelező!)*
*   **Sorrend (ábra hivatkozás: E177227):**
    A csavarokat minden lépésben az alábbi középről kifelé haladó keresztmintában kell lehúzni/lazítani:
    *   Felső csavarsor: `8 - 6 - 1 - 3 - 9`
    *   Alsó csavarsor: `10 - 4 - 2 - 5 - 7`
*   **Gyári forrásfájl:** [CYLINDER HEAD GASKET REMOVAL AND INSTALLATION.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/CYLINDER%20HEAD%20GASKET%20REMOVAL%20AND%20INSTALLATION.pdf) (Installation rész, 6., 7. és 8. lépések) és a mester [ENINGE-Joined.pdf](file:///home/adam/Insync/lalilali96@gmail.com/Google%20Drive/Dokumentumok/auto/Evoque-F538/workshop-manual/POWERTRAIN/ENGINE%20-%20INGENIUM%20I4%202.0L%20DIESEL/ENGINE/ENINGE-Joined.pdf).