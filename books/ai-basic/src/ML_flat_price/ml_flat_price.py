import numpy as np  # NumPy: a mátrixműveletek alapkönyvtára (ML-ben minden vektor + mátrix)

# -------------------------------------------------------------------
# 1. TANÍTÓ ADATOK
# -------------------------------------------------------------------
# Ezek valós (x, y) párok: x = lakás alapterülete, y = lakás ára.
# A modell célja: megtanulni a kapcsolatot az x és y között.
# A valóságban ez sok ezer adat lenne; itt csak 20 példa.
sizes = np.array([
    35, 40, 42, 45, 48,
    50, 52, 55, 58, 60,
    62, 65, 68, 70, 72,
    75, 78, 80, 85, 90
], dtype=float)

prices = np.array([
    30, 33, 34, 36, 38,
    40, 41, 43, 45, 47,
    48, 50, 52, 53, 55,
    57, 59, 60, 63, 67
], dtype=float)

# -------------------------------------------------------------------
# 2. DESIGN MÁTRIX ELŐKÉSZÍTÉSE (X_design)
# -------------------------------------------------------------------
# A lineáris modell alakja:
#   ŷ = w * x + b
#
# A 'b' egy konstans (bias), amely minden predikcióhoz hozzáadódik.
#
# Matematikailag sokkal kényelmesebb úgy kezelni,
# hogy az X mátrixban legyen egy külön oszlop állandó 1-esekkel.
# Így leírható egyetlen mátrixszorzással:
#
#   ŷ = X_design @ theta
#
# ahol:
#   X_design = [ x, 1 ]
#   theta = [ w, b ]
#
# Ez a neurális hálóknál is így működik egyetlen neuron esetén!
X = sizes.reshape(-1, 1)    # Átalakítjuk (20,) -> (20,1) vektorrá (oszlopvektor)
ones = np.ones_like(X)      # Készítünk egy (20,1) oszlopot csupa 1-essel a bias számára
X_design = np.hstack([X, ones])  # Összerakjuk: [méret, 1] => (20,2) mátrix

y = prices  # A célértékek (árak). Mérete (20,).

# -------------------------------------------------------------------
# 3. PARAMÉTEREK INICIALIZÁLÁSA
# -------------------------------------------------------------------
# A theta = [ w, b ] tartalmazza:
#   w = súly (meredekség)
#   b = bias (eltolás)
#
# Ezeket NEM kézzel állítjuk be.
# A gépi tanulás célja: megtalálni a legjobb w-t és b-t.
theta = np.zeros(2)  # Kezdőérték: w=0, b=0

# -------------------------------------------------------------------
# 4. TANULÁSI HYPERPARAMÉTEREK
# -------------------------------------------------------------------
# learning_rate = η (eta) — gradient descent lépésnagyság
# epoch = hányszor fut végig a modell az adatokon
learning_rate = 1e-4
epochs = 20000

n = len(X_design)  # minta elemszáma, itt 20

# -------------------------------------------------------------------
# 5. GRADIENT DESCENT TANÍTÓ CIKLUS
# -------------------------------------------------------------------
for epoch in range(epochs):

    # -------------------------------------------
    # ELŐREJELZÉS (PREDIKCIÓ)
    # -------------------------------------------
    # Ez a neurális háló "forward pass"-a:
    #   ŷ = X_design @ theta
    #
    # A @ a mátrixszorzás operátor: (20×2) @ (2,) -> (20,)
    y_hat = X_design @ theta

    # -------------------------------------------
    # HIBA (ERROR)
    # -------------------------------------------
    # error = ŷ - y
    #
    # Ez megmondja, mennyire tér el a modell válasza
    # a tanító adat valódi értékétől.
    error = y_hat - y

    # -------------------------------------------
    # GRADIENS (A LEJTŐ IRÁNYA)
    # -------------------------------------------
    # A veszteségfüggvény: MSE = mean squared error
    #
    # Ennek deriváltja (gradiens):
    #   grad = (2/n) * X_design^T @ error
    #
    # Ez mutatja meg, hogy merre kell módosítani a w és b értékeket,
    # hogy csökkenjen a hiba. Ez a "backpropagation" leegyszerűsített 1D verziója.
    grad = (2.0 / n) * (X_design.T @ error)

    # -------------------------------------------
    # SÚLYFRISSÍTÉS (GRADIENT DESCENT)
    # -------------------------------------------
    # theta = theta - η * grad
    #
    # Ez a gépi tanulás lényege:
    #   - ha a gradiens pozitív → lefelé megyünk → csökkentjük a súlyt
    #   - ha a gradiens negatív → növeljük a súlyt
    theta -= learning_rate * grad

# -------------------------------------------------------------------
# 6. TANULT PARAMÉTEREK KICSOMAGOLÁSA
# -------------------------------------------------------------------
w, b = theta

print(f"Tanult súly (w): {w:.4f}")
print(f"Tanult bias (b): {b:.4f}")

print("Betanult modell:")
print(f"  Ár ≈ {w:.3f} * alapterület + {b:.3f}   (millió Ft)")

# -------------------------------------------------------------------
# 7. ELŐREJELZÉS FELHASZNÁLÓTÓL KAPOTT ADATRA
# -------------------------------------------------------------------
# A modell itt már tudása alapján becslést ad egy új adatra.
while True:
    try:
        user_size = float(input("\nAdd meg a lakás méretét négyzetméterben (pl. 54): "))
        break
    except ValueError:
        print("Hibás input, kérlek számot adj meg!")

pred_price = w * user_size + b
print(f"\nA becsült ár: {pred_price:.2f} millió Ft")
