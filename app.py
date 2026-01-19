import joblib
import numpy as np
import os

# Dossier du fichier app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "logistic_regression_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "standard_scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("Bienvenue dans l'outil de prédiction du diagnostic du cancer du sein.")

while True:

    area_worst = float(input("Valeur de l'aire maximale de la cellule : "))
    radius_worst = float(input("Valeur du rayon maximal de la cellule : "))
    perimeter_worst = float(input("Valeur du périmètre maximal de la cellule : "))
    concavity_mean = float(input("Valeur de la concavité moyenne de la cellule : "))
    concave_points_mean = float(input("Valeur du nombre moyen de points concaves sur le contour cellulaire : "))

    X_input = np.array([[area_worst, radius_worst, perimeter_worst, concavity_mean, concave_points_mean]])
    X_scaled = scaler.transform(X_input)

    y_pred = model.predict(X_scaled)
    prediction = "BENIN" if y_pred[0] == 0 else "MALIN"

    print(f"Résultat de la prédiction : {prediction}")

    continuer = input("Souhaitez-vous effectuer une autre prédiction ? (o/n) ").strip().lower()
    if continuer != "o":
        break