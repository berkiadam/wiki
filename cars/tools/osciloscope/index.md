# Követelménylista egy jó, 4 csatornás autódiagnosztikai USB-oszcilloszkóphoz

Ez a specifikáció általános személyautó-diagnosztikai használatra készült, különös tekintettel az alábbi mérésekre:

- főtengely- és vezérműtengely-jeladók vizsgálata;
- CKP–CMP korreláció és vezérlés-időzítés;
- VVT-rendszerek diagnosztikája;
- injektor- és gyújtásjelek vizsgálata;
- PWM-vezérelt aktuátorok mérése;
- analóg szenzorjelek vizsgálata;
- CAN, CAN FD és LIN kommunikáció ellenőrzése;
- relatív kompresszió és áramfelvétel-mérés;
- hosszabb ideig fennálló vagy időszakos hibák rögzítése.

## Alapkövetelmények

| Paraméter | Minimális követelmény | Ajánlott érték |
|---|---:|---:|
| Analóg csatornák száma | 4 | 4 |
| Valós mintavételi sebesség 4 aktív csatornán | legalább 10 MS/s/csatorna | legalább 20 MS/s/csatorna |
| Maximális mintavételi sebesség 1 aktív csatornán | legalább 50 MS/s | legalább 100 MS/s |
| Analóg sávszélesség | legalább 20 MHz | 20–50 MHz |
| Memóriamélység 4 aktív csatornán | legalább 5 MS/csatorna | 10–25 MS/csatorna |
| Összes memóriamélység | legalább 20 MS | 40–100 MS |
| Vertikális felbontás | legalább 8 bit | 12 bit |
| Bemeneti csatolás | DC | AC és DC |
| Bemeneti feszültségtartomány | legalább ±20 V | legalább ±50 V |
| Túlterhelés-védelem | legalább ±100 V | ±200 V vagy megfelelő külső csillapító használata |
| Hosszú idejű streaming rögzítés | ajánlott | kötelezően előnyös |
| PC-csatlakozás | USB | galvanikusan leválasztott USB előny |
| Tápellátás | USB-ről vagy külső tápról | stabil USB-s működés |

## Triggerfunkciók

A szkóp legalább az alábbi triggerfunkciókat támogassa:

- emelkedő és lefutó éltrigger;
- állítható triggerszint;
- pre-trigger;
- triggerkésleltetés;
- pulse-width trigger;
- dropout trigger;
- runt pulse trigger előny;
- single-shot rögzítés;
- automatikus és normál trigger mód.

A stabil trigger különösen fontos CKP–CMP korreláció, injektor- és gyújtásjelek, illetve időszakos hibák vizsgálatakor.

## Szoftveres funkciók

A hozzá tartozó szoftver legalább az alábbi funkciókat biztosítsa:

- vízszintes és függőleges kurzorok;
- pontos időmérés;
- frekvencia- és kitöltési tényező mérés;
- nagyítás mély memóriába;
- referencia-hullámforma mentése;
- több hullámforma egymásra helyezése;
- matematikai csatornák;
- legalább A−B differenciálképzés;
- FFT előny;
- mérési adatok exportálása;
- CSV-export;
- képernyőkép vagy képformátumú export;
- mérési fájl mentése és visszatöltése;
- hosszú idejű rögzítés;
- soros busz dekódolás.

## Kommunikációs buszok támogatása

Ajánlott támogatás:

- CAN;
- CAN FD;
- LIN.

Előny lehet még:

- FlexRay;
- SENT;
- PSI5;
- K-Line.

A buszdekódolás nem helyettesíti a gyári diagnosztikai műszert, de sokat segíthet a fizikai jelszint, jelalak, szakadás, zárlat, zaj és kommunikációs hibák vizsgálatában.

## Bemeneti kialakítás

Különösen fontos ellenőrizni:

- a csatornák közös vagy különálló földelését;
- az USB és a mérőcsatornák közötti galvanikus kapcsolatot;
- a differenciális mérés lehetőségét;
- a lebegő jelek biztonságos mérhetőségét;
- a bemeneti impedanciát;
- a mérővezetékek és csatlakozók minőségét.

Sok olcsó USB-oszcilloszkóp összes csatornájának földpontja közös, és az USB-n keresztül a laptop földjéhez is kapcsolódhat. Emiatt két különböző potenciálon lévő pontra nem szabad a csatornák földcsipeszeit külön-külön rákötni.

Lebegő vagy differenciális jelekhez szükség lehet:

- differenciális mérőfejre;
- két csatorna különbségképzésére;
- galvanikusan leválasztott szkópra;
- megfelelő leválasztó adapterre.

## Szükséges tartozékok

Egy jó autódiagnosztikai készlethez legalább az alábbi tartozékok ajánlottak:

- 4 darab jó minőségű mérővezeték;
- tűszondák;
- back-probe tüskék;
- krokodilcsipeszek;
- akkumulátorcsatlakozók;
- biztosítékkal védett mérővezeték;
- 10:1 feszültségosztó;
- legalább 100–200 V-os csillapító;
- kisáramú áramfogó;
- nagyáramú áramfogó;
- differenciális mérőfej;
- induktív gyújtásjel-mérő;
- BNC-adapterek;
- univerzális breakout vezetékek.

## Reális, költséghatékony célkonfiguráció

Egy jó ár-érték arányú, általános autódiagnosztikai USB-oszcilloszkóp célkonfigurációja:

- 4 analóg csatorna;
- 20–50 MHz analóg sávszélesség;
- legalább 100 MS/s maximális mintavétel;
- legalább 20 MS/s/csatorna 4 aktív csatornán;
- legalább 10 MS memória csatornánként 4 aktív csatornán;
- legalább 40 MS összes memória;
- 12 bites vertikális felbontás;
- AC és DC bemeneti csatolás;
- legalább ±50 V bemeneti tartomány;
- legalább ±100 V túlterhelés-védelem;
- streaming mód;
- fejlett triggerfunkciók;
- CAN, CAN FD és LIN dekódolás;
- matematikai csatornák;
- referencia-hullámforma kezelés;
- CSV-export;
- stabil és jól használható Windows-szoftver.

## Ami nem feltétlenül szükséges

Költségcsökkentés miatt nem kötelező:

- 8 analóg csatorna;
- 100 MHz-nél nagyobb sávszélesség;
- 500 MS/s vagy 1 GS/s mintavétel;
- beépített jelgenerátor;
- érintőkijelző;
- önálló, laptop nélküli működés;
- nagyon nagy felbontású kijelző;
- Wi-Fi kapcsolat.

Ezek hasznos extrák lehetnek, de általános személyautó-diagnosztikában kisebb előnyt jelentenek, mint a jó bemenetvédelem, a memóriamélység, a 12 bites felbontás és a használható szoftver.

## Végső ajánlás

A legfontosabb minimumkövetelmények:

1. 4 analóg csatorna;
2. legalább 20 MHz sávszélesség;
3. legalább 20 MS/s/csatorna 4 aktív csatornán;
4. legalább 5 MS memória csatornánként;
5. 12 bites vertikális felbontás;
6. DC bemeneti csatolás;
7. legalább ±100 V túlterhelés-védelem;
8. streaming rögzítés;
9. fejlett triggerfunkciók;
10. CAN, CAN FD és LIN dekódolás;
11. matematikai csatornák;
12. stabil, jól használható diagnosztikai szoftver.

A kiválasztásnál nem elég a maximális mintavételi sebességet vagy sávszélességet nézni. Külön ellenőrizni kell, hogy a megadott mintavétel és memóriamélység mennyi 4 egyidejűleg aktív csatorna használatakor.