# Piackutatási és ellenőrzési terv — 4- és 2-csatornás autódiagnosztikai USB-oszcilloszkópok

## Cél és leadandó eredmény

Két külön kategóriában készül linkgyűjtemény jelenleg megvásárolható oszcilloszkópokról, amelyek magyarországi webshopokban, az Allegro.hu-n vagy az eBay-en elérhetők:

- **4-csatornás kategória:** 4 valódi analóg csatorna; legfeljebb **200 000 Ft** vételár. A készüléknek vagy használható PC-s szoftverrel kell rendelkeznie, vagy a meglévő Launch X431 PRO3 APEX készülékkel dokumentáltan kompatibilisnek kell lennie.
- **2-csatornás kategória:** 2 valódi analóg csatorna; legfeljebb **150 000 Ft** vételár. A készüléknek vagy használható PC-s szoftverrel kell rendelkeznie, vagy a meglévő Launch X431 PRO3 APEX készülékkel dokumentáltan kompatibilisnek kell lennie.

A gyűjtés végső állapotában a `result.md` `Unverified` szakasza üres; minden megmaradó tétel a saját kategóriájának `Verified` szakaszában szerepel.

Minden tétel formátuma:

```md
* link: <közvetlen termékoldal>
* márka és típus: <gyártó és pontos típusszám>
* description: <kategória, csatornaszám, releváns műszaki adatok, csomag tartalma és fontos korlátozások>
* ár: <vételár, pénznem és átváltási alap; szállítás csak tájékoztató adat, ha látható>
```

## Kötelező és előnyös műszaki kritériumok

A kategóriánkénti árkerethez a feltételeket két szintre osztjuk. A `Verified` szakaszba csak olyan termék kerülhet, amely minden **kötelező** pontot bizonyíthatóan teljesít. Az **előnyös** funkciók nem kizáró okok, de tételenként fel kell tüntetni, hogy melyek hiányoznak.

| Követelmény | Szint | Elfogadási feltétel |
|---|---|---|
| Analóg csatornák | kötelező | a 4-csatornás kategóriában 4, a 2-csatornás kategóriában 2 valódi, egyidejűleg használható analóg bemenet |
| Analóg sávszélesség | kötelező | legalább 20 MHz |
| Mintavétel | kötelező | legalább 10 MS/s/csatorna az adott kategória összes aktív analóg csatornáján; 20 MS/s/csatorna előny |
| Memória | kötelező | legalább 5 MS/csatorna az adott kategória összes aktív analóg csatornáján |
| Vertikális felbontás | kötelező | legalább 8 bit; 12 bit előny |
| Bemeneti csatolás | kötelező | DC támogatott |
| Bemenetvédelem | kötelező | dokumentált bemeneti névleges érték és túlterhelés-védelem; autóipari nagyfeszültséghez megfelelő 10:1/100:1 vagy differenciális mérőfej használata szükséges |
| Tápellátás | kötelező | a szkóp hálózati adapter nélkül működjön: USB-táplálású, beépített akkumulátoros vagy dokumentáltan 12 V-os járműakkuról működtethető DC-bemenetű legyen |
| Rögzítés | előnyös | streaming / hosszú idejű rögzítés |
| Trigger | kötelező | éltrigger, állítható szint, normál/single mód és pre-trigger; pulse-width, dropout és runt pulse trigger előny |
| Buszdekódolás | előnyös | CAN, CAN FD és LIN; a hiányzó dekódolás külső buszanalizátorral pótolható |
| Feldolgozás | kötelező | matematikai csatornák, legalább A−B különbségképzés |
| Szoftver | kötelező | használható PC-s szoftver **vagy** a meglévő Launch X431 PRO3 APEX-en futó, dokumentáltan kompatibilis alkalmazás. Mindkét esetben mentés/visszatöltés, kurzorok és export igazolható |

A mintavételnél a gyártó által megadott teljes valós idejű mintavételi sebesség egyenletesen elosztható az adott kategória összes egyidejűleg aktív analóg csatornájára; az így kapott értéknek el kell érnie a 10 MS/s/csatorna minimumot. A memória esetében továbbra is csatornánkénti vagy egyértelműen megosztott adat szükséges, amelyből igazolható az 5 MS/csatorna minimum.

## Értelmezési szabályok

- Csak a saját kategóriájának megfelelő számú valódi analóg bemeneti csatornás eszköz jelölt. A „4 in 1”, digitális/multiméter-csatorna vagy szoftveres virtuális csatorna nem elég.
- Mindkét kategóriában PC-s eszköz vagy a meglévő Launch X431 PRO3 APEX-szel dokumentáltan kompatibilis Scopebox fogadható el. Önálló asztali modell nem jelölt.
- Hálózati adaptert igénylő szkóp nem jelölt. Külső DC-tápú modell csak akkor fogadható el, ha a gyártó dokumentálja a 12 V-os járműakkuról használható feszültségtartományt; USB-táplálású és beépített akkumulátoros modell elfogadható.
- A kategória szerinti 200 000, illetve 150 000 Ft-os plafon kizárólag a termék vételárára értendő. Más pénznemnél az ellenőrzés napján látható oldalár, illetve dokumentált árfolyam alapján számolt forintértéket kell feltüntetni. A szállítás, vám és importáfa nem kizáró feltétel, de ismert értékét a leírásban jelezni kell.
- A kategória szerinti felső ár mellett a kötelezőként jelölt táblázatsorok mindegyike kötelező. Az előnyös funkciók hiánya megengedett, de a `description` mezőben egyértelműen fel kell tüntetni.
- A CAN/CAN FD/LIN-dekódolást és a bemenetvédelmet nem szabad feltételezni: csak termékoldali vagy gyártói bizonyíték alapján szabad állítani.
- Kereskedőtől független műszaki adatokat lehetőleg a gyártó hivatalos adatlapjával is össze kell vetni. A kínálati oldal bizonyítja az árat és az elérhetőséget; a gyártói oldal azonosítja a pontos modellt és specifikációt.

## Piaci elérhetőség korlátja

Az Allegro- és eBay-hirdetések Magyarországra szállíthatóságát a kutatás nem tekinti ellenőrizhető vagy kizáró feltételnek. Ez fiók-, cím-, eladói és piactéri szabályfüggő lehet. A `description` mezőben minden ilyen találatnál szerepeljen: **„Magyarországi szállítás: vásárlás előtt ellenőrizendő.”**

## Nyitott döntések a kutatás előtt

Az alábbi döntéseket egyenként kell meghozni, és a választ a kutatás megkezdése előtt ebben a tervben kell rögzíteni:

1. **Döntés: mindkét kategóriában PC-s szkóp vagy a meglévő Launch X431 PRO3 APEX-szel dokumentáltan kompatibilis Scopebox fogadható el.** Önálló asztali modell nem jelölt.
2. **Döntés: csak új termék fogadható el.** A használt, felújított („refurbished”) és „open box” hirdetések nem jelöltek.
3. **Döntés: aukciós hirdetés is elfogadható.** Az ellenőrzéskor látható aktuális licitár alapján kell teljesítenie az árkorlátot; az aukció lezárásáig az ár változhat, ezt a leírásban jelezni kell.
4. **Döntés: a 4-csatornás kategóriában a 200 000 Ft-os, a 2-csatornás kategóriában a 150 000 Ft-os limit csak a vételárra vonatkozik.** A szállítás és egyéb járulékos költség nem kizáró feltétel; ha ismert, tájékoztató jelleggel rögzítendő.
5. **Döntés: magyar nyelvű, ismert és megbízható elektronikai forgalmazók közvetlen termékoldalait vizsgáljuk.** Kétes hátterű, nem ellenőrizhető vagy átverésgyanús webshop nem forrás; a keresők által indexelt találat csak kiindulópont.
6. **Döntés: a szkóp nem igényelhet hálózati adaptert.** USB-ről, beépített akkumulátorról vagy dokumentáltan 12 V-os járműakkuról kell működnie.

## Subagent-szerepkörök és adatkezelés

- A kutatás első körében külön subagent vizsgálja a magyar webshopokat, az Allegro.hu-t, az eBay-t, valamint a márka- és típusnév-alapú kiegészítő kereséseket.
- A gyűjtő subagent csak jelölteket keres és strukturált jelentésben ad át: URL, pontos modell, látható ár/szállítás, az állított műszaki adatok és a forrás megnyitásának ideje. Nem helyez át tételt `Verified`-be.
- A jelöltet felvevő és azt ellenőrző subagent nem lehet ugyanaz.
- Az ellenőrző subagent közvetlen oldalmegnyitással rögzíti az ellenőrzés időpontját, valamint az ár, rendelhetőség, 4 csatorna, 4 csatornás mintavétel és memória, illetve a többi kötelező adat bizonyítékát.
- Egy időben csak a koordinátor módosítja a `result.md`-t. A subagentek jelentést küldenek; a koordinátor írja be az új jelöltet `Unverified`-be, helyezi át a teljesen igazolt tételt `Verified`-be, vagy törli az elutasított tételt. Ez megakadályozza az egyidejű fájlmódosítások ütközését.
- Az Allegro- és eBay-hirdetések változékonysága miatt minden ellenőrzés időbélyeghez kötött; a `Verified` státusz az ellenőrzés pillanatában látható adatokra vonatkozik.

## Munkafolyamat

1. **Keresési térkép és időbélyeg rögzítése.** A keresés napját, az alkalmazott kulcsszavakat és az átvilágított forrásokat röviden dokumentálni kell. Forráscsoportok: magyar szaküzletek és műszaki webshopok, ár-összehasonlítók által mutatott hazai termékoldalak, Allegro.hu és eBay. Keresésekben a típusnév mellett a `4 channel`, `4 csatornás`, `USB oscilloscope`, `automotive`, `PicoScope`, `Hantek`, `OWON`, `Rigol`, `Siglent` kifejezések is szerepeljenek.
2. **Párhuzamos jelöltgyűjtés subagentekkel.** Az egyes subagentek egymástól elkülönített forráscsoportot vagy márkacsoportot kapnak. Minden hihető találatot strukturált jelentésben küldenek a koordinátornak; a koordinátor azokat a `result.md` `Unverified` szakaszába írja a fenti, négymezős formátumban. A jelöltgyűjtő nem helyez át tételt a `Verified` szakaszba.
3. **Duplikátumok és nyilvánvaló hibák szűrése.** Azonos típus több eladónál külön tétel lehet, ha külön termékoldal és ár tartozik hozzá. Az azonos URL-eket össze kell vonni. Azonnal törlendő a hibás kategóriájú, a saját árplafonja fölötti, kifutott/nem megvásárolható, hibás URL-re mutató vagy félreazonosított tétel.
4. **Független ellenőrzés subagentekkel.** Minden `Unverified` tételt egy másik subagent nyit meg, mint aki felvette. Az ellenőr közvetlenül a termékoldalon és a gyártói dokumentációban igazolja: (a) az oldal tényleg a megadott pontos modellt kínálja, (b) a kötelező műszaki táblázat minden sora teljesül — különösen az adott kategória összes aktív csatornájára érvényes mintavétel és memória —, (c) a termék vételára nem haladja meg a saját kategóriájának plafonját, (d) megvásárolható vagy egyértelműen rendelhető, (e) a leírás nem tulajdonít neki nem igazolt képességet. Az előnyös funkciókat és az esetleg látható szállítási költséget külön rögzíti.
5. **Döntés és naplózás.** Az ellenőr csak akkor teszi át a tételt a `Verified` szakaszba, ha a fenti pontok és minden kötelező specifikáció közvetlen oldalbeli bizonyítékkal alátámasztható. A termékoldalak állapota gyorsan változhat, ezért a „100%” itt az ellenőrzés időpontjában, elsődleges oldalakon ellenőrizhető bizonyítékot jelent. Bármely kétség, eltérés, hiányzó szállítási információ vagy nem igazolható **kötelező** specifikáció esetén a tételt törölni kell, nem maradhat `Unverified`-ben.
6. **Iteráció a lista kiürüléséig.** Újabb jelölteket addig lehet felvenni, amíg a forráscsoportokban marad ellenőrizetlen találat; minden kör végén az összes `Unverified` elemet kiosztjuk ellenőrzésre. A munka csak akkor zárható le, amikor az `Unverified` szakasz üres.
7. **Végső audit.** Egy utolsó olvasás ellenőrzi, hogy minden `Verified` bejegyzésnél van élő, közvetlen link, pontos típus, tárgyszerű leírás és egyértelmű ár; a `result.md` nem tartalmaz nem megfelelő vagy bizonytalan tételt.

## Ellenőrzési ellenőrzőlista

- [ ] A link közvetlen termékoldal, és az oldal megnyílik.
- [ ] Az oldal és a gyártói adatlap ugyanazt a márkát és típust azonosítja.
- [ ] A saját kategóriának megfelelő számú analóg csatorna igazolt.
- [ ] A dokumentáció igazolja az USB-s, akkumulátoros vagy 12 V-os járműakkuról történő működést; a szkóp nem igényel hálózati adaptert.
- [ ] A kötelező műszaki megfelelési táblázat minden kötelező sora igazolt, a mintavétel és memória az adott kategória összes aktív csatornájára is.
- [ ] A termék vételára legfeljebb a saját kategóriájának megfelelő 200 000 vagy 150 000 Ft, vagy ez a külföldi piactéren egyértelműen kiszámítható.
- [ ] Allegro/eBay esetén a leírás tartalmazza: „Magyarországi szállítás: vásárlás előtt ellenőrizendő.”
- [ ] A rögzített leírás csak bizonyított adatokat tartalmaz, és megnevezi a célok szempontjából fontos kompromisszumokat.
- [ ] A tételt nem ugyanaz a subagent ellenőrizte, aki felvette.
