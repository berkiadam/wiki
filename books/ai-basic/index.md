
---
# Mesterséges "Intelligencia"?
 
> A „mesterséges intelligencia” kifejezés félrevezető — nem intelligenciával állunk szemben, hanem hatalmas statisztikai alapon működő modellekkel. 

A modern AI, amit ma használunk — a ChatGPT-től a képfelismerőkön át az önvezető autókig — valójában nem gondolkodik, nem rendelkezik fogalmi tudással, nem értelmez és nem következtet emberi módon.

A modern AI rendszerek matematikai modellek, amelyek:
- bemeneti adatokat fogadnak,
- azokat numerikus vektorokká alakítják,
- majd többrétegű, paraméterezett függvényeken vezetik át őket,
- ahol a függvény paraméterei (a súlyok) egy tanítási folyamat során optimalizálódnak.

```
AI = optimalizált, statisztikai függvények, rengeteg paraméterrel.
``` 
Sokszor "Macine Learing"-ként (Gépi Tanulás) vagy deep learning models-ként (mély tanuló modellek) hivatkozunk rá, nem „intelligenciaként”.

<br>

---
# Machine Learning -> Deep Learing

A fogalmak pontos hierarchiája:

AI (Artificial Intelligence)
 └─ ML (Machine Learning)
      └─ Deep Learning (Neural Networks)


AI: minden módszer, ami emberihez hasonló kompetenciákat próbál megvalósítani (szabályalapú rendszerek is).

ML: olyan módszerek, amelyek adatból tanulnak.
(Lineáris regresszió, SVM, döntési fák, boosting, stb.)

Deep Learning (DL): gépi tanulási módszer, amely mély neurális hálókat használ.

A videóban innentől kimondhatod:

„Ebben a sorozatban, amikor AI-t mondok, deep learning alapú neurális hálókról beszélek.”

Mert ez az ipari valóság — minden modern AI megoldás alapja deep learning.

## Machine Learning 

Gépi Tanulás: a program nem szabályokat követ, hanem szabályokat tanul

A klasszikus szoftverfejlesztésben:
Mi írjuk le a logikát.

```java
if input > threshold:
    return X
else:
    return Y
```

Az ML ezzel szemben azt mondja:

> „A Gépi Tanulás lehetővé teszi a számítógépek számára, hogy adatokból tanuljanak és anélkül hozzanak döntéseket, hogy erre kifejezetten programozták volna őket. Algoritmusok segítségével mintázatokat azonosít nagy adatállományokban, így a rendszer előrejelzéseket vagy besorolásokat tud készíteni új, korábban nem látott adatokon. Ez a folyamat segíti a feladatok automatizálását, és képessé teszi a rendszereket arra, hogy teljesítményüket idővel javítsák, ahogy egyre több adatot kapnak..”

Ez formálisan azt jelenti:

- Van egy bemenet: 𝑥
- és egy várt kimenet: 𝑦
- és mi keresünk egy függvényt:

$$
f_{\theta}(x) \approx y
$$

ahol 𝜃 a modell paraméterei, amiket súlyoknak is nevezünk.

> A "gépi tanulás" célja tehát:
> Megtalálni azt a paraméterkészletet, amely a bemenet → kimenet leképezést a > lehető legpontosabban approximálja.

Az ML modellek egyszerűbb példái:
- lineáris regresszió,
- logisztikus regresszió,
- döntési fák,
- SVM,
- random forest,
- XGBoost.

Ezek mind paraméteres vagy szabályalapú modellek, amelyek adatból tanulnak.


## Deep Learning

A "Deep Learing" a gépi tanulás egy speciális alfaja

> A Deep Learning nem külön diszciplína — ez machine learning, csak egy nagyon > erős, mély hálózatokra épülő formája.

A Deep Learning lényege: többrétegű **neurális hálókkal** (deep neural networks) tanulunk függvényeket.

Deep Learning képes megtanulni egy:
- sokdimenziós,
- nemlineáris,
- nagyon komplex,
- rétegekbe bújtatott,
- függvényrendszert.







# Deep learing részletesen

### A DL egy univerzális függvény-approximátor


Egy neurális háló — mégpedig már egyetlen rejtett réteggel is — képes arra, hogy:
- bármilyen folytonos függvényt
- egy kompakt tartományon
- tetszőlegesen jól

megközelítsen, ha elegendő számú neuron van a rejtett rétegben.

Tehát egy egyszerű háló:

$$
y = \sum_{i=1}^{N} \alpha_i \, \sigma(w_i^T x + b_i)
$$





Ezért működnek olyan jól a DL modellek:

képfelismerésben,

beszédfelismerésben,

nyelvfeldolgozásban (LLM-ek),

generatív feladatokban (Stable Diffusion),

robotikában,

időbeli és multimodális adatoknál.

1. Mi teszi "deep"-pé a Deep Learninget?

A „deep” szó rétegmélységet jelent.

A modell sokszor egymás után alkalmaz:

egy súlymátrixszorzást,

egy bias hozzáadását,

és egy nemlineáris aktivációt.

Formailag egy L rétegű háló: