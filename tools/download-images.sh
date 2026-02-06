#!/bin/bash
set -euo pipefail

# ---- KONFIGURÁCIÓ ----
DOC_ROOT="../linux/elasticsearch"  # a gyökerétől számítva, ahol a docs könyvtár létre lesz hozva
DOCS_DIR="$DOC_ROOT/docs"

URL="http://wiki.berki.org/index.php/Centralized_logging_in_swarm"
BASE="http://wiki.berki.org"

# ----------------------

mkdir -p "$DOCS_DIR"

HTML=$(curl -sS "$URL")

if [[ -z "$HTML" ]]; then
  echo "Hiba: Nem sikerült letölteni a HTML forrást."
  exit 1
fi

# img src kinyerése
mapfile -t IMAGE_URLS < <(
  echo "$HTML" \
    | grep -oE '<img[^>]+src="[^"]+"' \
    | sed -E 's/.*src="([^"]+)".*/\1/' \
    | sed -E "s|^/|$BASE/|"
)

if [[ ${#IMAGE_URLS[@]} -eq 0 ]]; then
  echo "Nem találtunk képeket az oldalon."
  exit 1
fi

UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

for IMG in "${IMAGE_URLS[@]}"; do
  FILENAME=$(basename "${IMG%%\?*}")

  # protocol-relative URL kezelése
  if [[ "$IMG" == //* ]]; then
    IMG="http:$IMG"
  fi

  if curl -sS -L --fail \
       --referer "$URL" \
       --user-agent "$UA" \
       -o "$DOCS_DIR/$FILENAME" \
       "$IMG"; then
    echo "Letöltve: $DOCS_DIR/$FILENAME"
  else
    echo "Hiba: nem sikerült letölteni: $IMG"
  fi
done

echo "Képek letöltése kész. Fájlok itt: $DOCS_DIR"
