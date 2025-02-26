#!/bin/bash

# Bemeneti és kimeneti fájlok

FOLDER="range-rover"
WIKI_FILE="input.wiki"
MD_FILE="output_tmp.md"
MD_FINAL="index.md"
IMAGE_DIR="docs"

#--------------- dont edit below this line --------------------

FOLDER="range-rover"
WIKI_FILE="../$FOLDER/$WIKI_FILE"
MD_FILE="../$FOLDER/$MD_FILE"
MD_FINAL="../$FOLDER/$MD_FINAL"
IMAGE_DIR="../$FOLDER/$IMAGE_DIR"


rm $MD_FILE
touch $MD_FILE

# Ellenőrizzük, hogy létezik-e a bemeneti fájl
if [[ ! -f "$WIKI_FILE" ]]; then
    echo "Hiba: A $WIKI_FILE fájl nem található!"
    exit 1
fi

# Konverzió kezdete
echo "Konvertálás MediaWiki → Markdown..."



awk '
BEGIN { count = 1 }
/^# / { 
    print count ". " substr($0, 3); 
    count++; 
    next;
}
{ print }
' "$WIKI_FILE" > temp.md && mv temp.md "$MD_FILE"



# Csillagos listák (`*`) átalakítása tabulációs beljebb tolással
awk '
{
    gsub(/^\*\*\*\*/, "\t\t\t-");
    gsub(/^\*\*\*/, "\t\t-");
    gsub(/^\*\*/, "\t-");
    gsub(/^\*/, "-");
    print;
}' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"

sed -E '
# {{warning|...}} -> > **WARNING:** ... (plusz egy üres sor)
s/\{\{warning\|([^}]+)\}\}/> **WARNING:** \1\n/g

# {{note|...}} -> > **NOTE:** ... (plusz egy üres sor)
s/\{\{note\|([^}]+)\}\}/> **NOTE:** \1\n/g

# {{tip|...}} -> > **TIP:** ... (plusz egy üres sor)
s/\{\{tip\|([^}]+)\}\}/> **TIP:** \1\n/g
' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"



# <pre>...</pre> blokkokat ``` kódrészletekre cseréljük
awk '
{
    if ($0 ~ /<pre>/) {
        print "```";
        inside_code=1;
    } else if ($0 ~ /<\/pre>/) {
        print "```";
        inside_code=0;
    } else {
        print;
    }
}' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"

# Kép hivatkozások átalakítása Markdown formátumba, méretkezeléssel
awk -v imgdir="$IMAGE_DIR" '
{
    while (match($0, /\[\[File:([^|\]]+)\|?([^]]*)\]\]/, arr)) {
        filename = arr[1];
        size = "";
        sized_filename = filename;  # Alapértelmezés szerint a fájlnév változatlan

        if (match(arr[2], /([0-9]+)px/, sizearr)) {
            size = "{width=\"" sizearr[1] "\"}";
            sized_filename = sizearr[1] "px-" filename;  # Méret hozzáadása a fájlnév elé
        }

        gsub(/:?[\[File:[^|\]]+\|?[^]]*\]\]/, "![" imgdir "/" sized_filename "](" imgdir "/" sized_filename ") ");
    }
    print;
}' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"


# MediaWiki linkek Markdown formátumra konvertálása
awk '
{
    gsub(/\[\[([^|\]]+)\|([^]]+)\]\]/, "[\\2](\\1)");
    gsub(/\[\[([^|\]]+)\]\]/, "[\\1](\\1)");
    print;
}' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"


sed -E -i '
s/^ *====== *([^=]+) *====== *$/\n###### \1/
s/^ *===== *([^=]+) *===== *$/\n##### \1/
s/^ *==== *([^=]+) *==== *$/\n#### \1/
s/^ *=== *([^=]+) *=== *$/\n### \1/
s/^ *== *([^=]+) *== *$/\n## \1/
s/^ *= *([^=]+) *= *$/\n# \1/
' "$MD_FILE"

# döntöttt és kiemelt szövegetk 
sed -E "s/'''([^']+)'''/**\1**/g; s/''([^']+)''/*\1*/g" "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"

## a csillagok utáni és előtt space-ek törlése
sed -E 's/\*\* +([^*]+) +\*\*/**\1**/g' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"


# minden <br> után egy új sor
sed -E 's/<br>/&\n/g' "$MD_FILE" > temp.md && mv temp.md "$MD_FILE"



#------------több soros worning és note ------------------
# -------------------------------------------------------

# Bemeneti és kimeneti fájlok
WIKI_FILE=$MD_FILE
MD_FILE="$MD_FINAL"

# Ideiglenes fájl törlése, ha létezik
rm -f "$MD_FILE"
touch "$MD_FILE"




# Átmeneti változók
inside_warning=0
inside_note=0
inside_tip=0
content=""

# Fájl sorainak beolvasása
while IFS= read -r line; do
    # Ha új warning blokk kezdődik
    if [[ "$line" =~ \{\{warning\| ]]; then
        inside_warning=1
        #content="**WARNING:** "
        line=${line#*\{\{warning\|}  # Kezdő rész levágása
        line="**WARNING:** $line"
    fi

    # Ha új note blokk kezdődik
    if [[ "$line" =~ \{\{note\| ]]; then
        inside_note=1
        content="**NOTE:** "
        line=${line#*\{\{note\|}  # Kezdő rész levágása
    fi

    # Ha új tip blokk kezdődik
    if [[ "$line" =~ \{\{tip\| ]]; then
        inside_tip=1
        content="**TIP:** "
        line=${line#*\{\{tip\|}  # Kezdő rész levágása
    fi

    # Ha belül vagyunk egy warning, note, tip blokkban
    if [[ $inside_warning -eq 1 || $inside_note -eq 1 || $inside_tip -eq 1 ]]; then
        # Ha megtaláljuk a lezáró dupla kapcsos zárójelet
        if [[ "$line" =~ \}\} ]]; then
            line=${line%%\}\}*}  # Lezárás előtti rész levágása
            content+="> $line\n"    # Hozzáadjuk az utolsó sort
            echo -e "$content\n" >> "$MD_FILE"  # Kiírjuk a fájlba
            inside_warning=0
            inside_note=0
            inside_tip=0
            content=""
            continue
        else
            # Ha még nem záródott le, folytatjuk a gyűjtést
            content+="> $line\n"
            continue
        fi
    fi

    # Normál sorokat egyszerűen kiírunk a fájlba
    echo "$line" >> "$MD_FILE"

done < "$WIKI_FILE"







rm "$WIKI_FILE"


# Kész
echo "Konvertálás kész: $MD_FILE"
