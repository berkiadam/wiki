#!/bin/bash
set -euo pipefail

URL="http://wiki.berki.org/index.php/Apache_Avro_with_Kafka"
BASE="http://wiki.berki.org"
mkdir -p docs

HTML=$(curl -sS "$URL")

if [[ -z "$HTML" ]]; then
  echo "Hiba: Nem sikerült letölteni a HTML forrást."
  exit 1
fi

# src kinyerés (egyszerűen)
mapfile -t IMAGE_URLS < <(echo "$HTML" \
  | grep -oE '<img[^>]+src="[^"]+"' \
  | sed -E 's/.*src="([^"]+)".*/\1/' \
  | sed -E "s|^/|$BASE/|")

if [[ ${#IMAGE_URLS[@]} -eq 0 ]]; then
  echo "Nem találtunk képeket az oldalon."
  exit 1
fi

UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

for IMG in "${IMAGE_URLS[@]}"; do
  FILENAME=$(basename "${IMG%%\?*}")  # querystring levágása

  # Ha valamiért //-val kezd (protocol-relative)
  if [[ "$IMG" == //* ]]; then
    IMG="http:$IMG"
  fi

  # Letöltés (redirect követés, hibára ne csináljon HTML mentést)
  if curl -sS -L --fail -o "docs/$FILENAME" --referer "$URL" --user-agent "$UA" "$IMG"; then
    echo "Letöltve: $FILENAME"
  else
    echo "Hiba történt: $FILENAME nem sikerült letölteni! ($IMG)"
  fi
done

echo "Képek letöltése kész. Fájlok a docs mappában."
