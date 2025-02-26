#!/bin/bash

# Cél URL
URL="https://wiki.berki.org/index.php/Land_Rover#Felf.C3.BCggeszt.C3.A9s"

# Célkönyvtár létrehozása
mkdir -p docs

# HTML letöltése
HTML=$(curl -s -k "$URL")

# Ellenőrizzük, hogy van-e tartalom
if [[ -z "$HTML" ]]; then
    echo "Hiba: Nem sikerült letölteni a HTML forrást."
    exit 1
fi

# Képek URL-jeinek kinyerése
IMAGE_URLS=$(echo "$HTML" | grep -oE '<img[^>]+src="([^"]+)' | sed -E 's/<img[^>]+src="([^"]+)/\1/' | sed 's|^/|https://wiki.berki.org/|')

# Ha nincs kép, jelezzük a hibát
if [[ -z "$IMAGE_URLS" ]]; then
    echo "Nem találtunk képeket az oldalon."
    exit 1
fi

# Képek letöltése megfelelő formátumban
for IMG in $IMAGE_URLS; do
    FILENAME=$(basename "$IMG")

    # A képek letöltése bináris módon
    curl -s -k -o "docs/$FILENAME" --referer "$URL" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "$IMG"
    
    # Ellenőrizzük, hogy sikerült-e letölteni
    if [[ $? -eq 0 ]]; then
        echo "Letöltve: $FILENAME"
    else
        echo "Hiba történt: $FILENAME nem sikerült letölteni!"
    fi
done

echo "Képek letöltése kész. Fájlok a docs mappában."
