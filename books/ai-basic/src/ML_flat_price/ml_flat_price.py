import numpy as np

# 1. Tanító adatok (alapterület m2-ben, ár millió Ft-ban)
# Ezek csak példaadatok, de nagyjából lineáris kapcsolatot követnek.
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

# 2. Bemeneti mátrix előkészítése (X_design = [x, 1] hogy legyen bias is)
X = sizes.reshape(-1, 1)                # (20, 1)
ones = np.ones_like(X)                  # (20, 1)
X_design = np.hstack([X, ones])         # (20, 2) -> oszlopok: [méret, 1]

y = prices                              # (20,)

# 3. Paraméterek inicializálása: theta = [w, b]
theta = np.zeros(2)                     # w = theta[0], b = theta[1]

# 4. Tanulási ráta és epoch szám
learning_rate = 1e-4
epochs = 20000

n = len(X_design)

for epoch in range(epochs):
    # Előrejelzés: y_hat = X_design @ theta
    y_hat = X_design @ theta            # (20,)

    # Hiba
    error = y_hat - y

    # Gradiens számítás (MSE deriváltja)
    grad = (2.0 / n) * (X_design.T @ error)  # (2,)

    # Súlyfrissítés (gradient descent)
    theta -= learning_rate * grad

# A tanult paraméterek
w, b = theta

print("Betanult modell:")
print(f"  Ár ≈ {w:.3f} * alapterület + {b:.3f}   (millió Ft)")

# 5. Felhasználói kérdés: új lakás alapterülete
while True:
    try:
        user_size = float(input("\nAdd meg a lakás méretét négyzetméterben (pl. 54): "))
        break
    except ValueError:
        print("Hibás input, kérlek számot adj meg!")

pred_price = w * user_size + b
print(f"\nA becsült ár: {pred_price:.2f} millió Ft")
