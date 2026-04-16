Három nagy irány van:
1. HTML alapú konvertálás
   * wkhtmltopdf
   * pagedjs-cli
   * prince
2. LaTex alapú konvertálás
   * pdflatex
   * lualatex
   * xelatex
   * latexmk
   * Tectonic
   * ConTeXt
3. Vegyes
   * pdfroff: GNU unix alapú
   * Typst: egyedi 


weasyprint, wkhtmltopdf, pagedjs-cli, prince, pdflatex, lualatex, xelatex, latexmk, tectonic, pdfroff, typst, context


| Jellemző | XeLaTeX | WeasyPrint | PagedJS / Prince |
| :--- | :--- | :--- | :--- |
| **Minőség** | Nagyon stabil, nyomdai | Nem optimális PDF struktúra, CPU igényes | Modern, rugalmas |
| **Bázis technológia** | TeX / LaTeX | HTML / CSS (Python) | Modern HTML5 / CSS3 |
| **Formázás nehézsége** | Magas (LaTeX kód) | Közepes (CSS) | Alacsony (Standard CSS) |
| **Kód tördelése** | Komplex beállítást igényel | Natív CSS-sel könnyű | Nagyon egyszerű CSS-sel |
| **Képek / Mermaid** | Tökéletes SVG kezelés | Nagyon megterheli az SVG | Tökéletes SVG kezelés |
| **Mermaid támogatás** | Igen | Igen | Igen |


# COMMON:

A yaml header-be attól függetlenül hogy HTML vagy LaTex alapú a konvertáló, mindig meg lehet adni a dokumentum címét és alcímét és a tartalomjegyzék címét: 

```yaml
---
title: "Kafa használat a DSP-ben"
subtitle: "topic release, kafka beállítások és avro séma használat"
toc-title: "Tartalomjegyzék"
---
```

Ezekre mind LATEX-ben mind HTML css-ben lehet egyedi formázást adni. 



# WeasyPrint

Ha nincsenek benne SVG képek, akkor ezt használjuk !!! A css alapú PDF generátorokkal sokkal de sokkal könnyebb a formázás. A CSS-ben minden porcikája átállítható a PDF-nek. Latexben NEM. 

```
$ sudo dnf install weasyprint

$ pandoc README.md -o output.pdf --filter mermaid-filter --css docs/style.css --pdf-engine=weasyprint
```

```
/* docs/style.css */

@page {
    size: A4; /* Vagy 'letter', 'A3', vagy egyedi méret: 210mm 297mm */
    margin: 2cm; /* Margók beállítása */
}
```

~~~
```mermaid
%%{init: {"flowchart": {"htmlLabels": false}} }%%
graph LR
...
~~~

```
MERMAID_FILTER_FORMAT=svg pandoc README.md -o output.pdf --filter mermaid-filter --css docs/style.css --pdf-engine=weasyprint
```
vagy

```
MERMAID_FILTER_FORMAT=svg pandoc README.md -o output.pdf --filter mermaid-filter --css docs/style.css --pdf-engine=weasyprint --number-sections --toc 
```

---

# XeLaTeX

```
sudo dnf install librsvg2-tools
```

## Latex fájlformázó
VSCODE plugin: LaTeX Workshop

Ehhez fel kell telepítnei a **latexindent**-et. 

```
$ sudo dnf install texlive-latexindent "perl(Log::Log4perl)" "perl(YAML::Tiny)" "perl(File::HomeDir)"
```

```
$ which latexindent
/usr/bin/latexindent
```

Majd a settings.json-ba be kell rakni: 

```josn
    "[latex]": {
        "editor.defaultFormatter": "James-Yu.latex-workshop",
        "editor.formatOnSave": false
    },
    "latex-workshop.formatting.latex": "latexindent"
```

## Latex header

A latex motornak két helyen lehet átadni paramétereket: 
1. Latex yaml header 
2. latex include fájl. 


A latex yaml header mindig az md fájl elején van `---` blokkok között. 
Ebbe vagy teljes latex configurációt raknunk, vagy csak cím infókat: 

Minimum tartalom: 
```yaml
---
title: "Kafa használat a DSP-ben"
subtitle: "topic release, kafka beállítások és avro séma használat"
toc-title: "Tartalomjegyzék"
lang: hu
---

... md fájl további része
```


Teljes config: 
```yaml
---
title: "Cross-Client Authorization Handoff"
header-includes:
  - |
    \usepackage{titling}
    \setlength{\droptitle}{-2cm}
    \pretitle{\begin{center}\LARGE\bfseries\color{blue}}
    \posttitle{\par\vskip 0.5em{\color{black}\hrule}\end{center}}
    \usepackage{xurl}
    \urlstyle{same}
    \lstset{
      breaklines=true,
      breakatwhitespace=false,
      basicstyle=\ttfamily\small,
      columns=flexible,
      extendedchars=true,
      literate={„}{{\textquotedblleft}}1 {”}{{\textquotedblright}}1 {á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ö}{{\"o}}1 {ő}{{\H{o}}}1 {ú}{{\'u}}1 {ü}{{\"u}}1 {ű}{{\H{u}}}1
    }
---
```


## Latex include fájl

Hozzunk létre egy **header.tex** fájlt. Ebbe fogunk minden latex konfigurációt megadni a cím adatokon kívül: 

```latex
\usepackage{xcolor}
\usepackage{titling}
\usepackage{xurl}
\usepackage{colortbl}
\usepackage[many]{tcolorbox}
\usepackage{etoolbox}
\usepackage{fvextra}
\usepackage{hyperref}

% Színek definíciója
\definecolor{codebg}{gray}{0.95}
\definecolor{lightgray}{gray}{0.9}

% Cím stílus beállítása
\setlength{\droptitle}{-2cm}
\pretitle{\begin{center}\LARGE\bfseries\color{blue}}
    \posttitle{\par\vskip 0.5em{\color{black}\hrule}\end{center}}

% Linkek aláhúzása (kékkel)
\hypersetup{
  colorlinks=false,
  pdfborderstyle={/S/U/W 1},
  urlbordercolor=blue,
  linkbordercolor=blue
}

% Kód tördelése és speciális karakterek (pl. _) védelme
\fvset{
  breaklines=true,
  breakanywhere=true,
  commandchars=none % Ez kulcsfontosságú a YAML kódblokkokhoz
}

% Pandoc belső Shaded környezetének kiürítése az ütközések elkerülésére
\renewenvironment{Shaded}{}{}

% Kódblokkok dobozolása tcolorbox-szal
\makeatletter
\BeforeBeginEnvironment{Highlighting}{
  \begin{tcolorbox}[
      breakable,
      size=small,
      colback=codebg,
      colframe=lightgray,
      arc=0mm
    ]
    }
    \AfterEndEnvironment{Highlighting}{\end{tcolorbox}}
\makeatother

\urlstyle{same}
```

A pandoc parancsban így kell megadni: 
```
--include-in-header=header.tex
```




## Pandoc futtatás


Itt nincs css megadás

pandoc README.md -o output.pdf --filter mermaid-filter --pdf-engine=xelatex


Egységes 3 cm-es margó minden oldalon:
pandoc README.md -o output.pdf --filter mermaid-filter --pdf-engine=xelatex -V geometry:margin=2cm

Különböző margók (pl. felül/alul 2cm, oldalt 3cm):
pandoc README.md -o output.pdf --filter mermaid-filter --pdf-engine=xelatex -V geometry:"top=2cm, bottom=2cm, left=3cm, right=3cm"

```
$ pandoc README.md -o output.pdf --filter mermaid-filter --pdf-engine=xelatex --listings -V geometry:margin=2cm --number-sections
```



- nincs külső css
- a felsorolások előtt kell egy üres sor 


MERMAID_FILTER_FORMAT=svg pandoc README.md -o output.pdf --filter mermaid-filter --pdf-engine=xelatex --listings -V geometry:margin=2cm --number-sections


```
MERMAID_FILTER_FORMAT=svg pandoc README.md -o output.pdf   --filter mermaid-filter   --pdf-engine=xelatex   --number-sections   --toc   --highlight-style pygments   -V geometry:margin=2cm
```

```
$ pandoc README-kiserlet.md -o output.pdf   --filter mermaid-filter   --pdf-engine=xelatex   --number-sections --include-in-header=header.tex   --toc --pdf-engine-opt=-interaction=nonstopmode  --highlight-style pygments -V geometry:a3paper    -V geometry:margin=2cm
```



## Latex Math-ot tartalmazó md konvertálása

```bash
pandoc berki-joist.md -o berki-joist.pdf \
--pdf-engine=xelatex \
-V geometry:margin=2cm \
-V mainfont="DejaVu Serif"
```


# PagedJS

```
$ npm install -g pagedjs-cli
```


MERMAID_FILTER_FORMAT=svg pandoc README.md -o output.pdf \
  --pdf-engine=pagedjs \
  --number-sections \
  --toc \
  --highlight-style pygments \
  --css docs/style.css
