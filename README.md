# 🩺 Breast Cancer Prediction – Machine Learning Project

## 🎯 Objectif du projet

Ce projet vise à développer un **modèle de Machine Learning basé sur une régression logistique** afin de **prédire le diagnostic du cancer du sein** (tumeur bénigne ou maligne) à partir de caractéristiques morphologiques de cellules tumorales.

Le projet s’appuie sur le jeu de données **Wisconsin Breast Cancer Dataset** et met l’accent sur :

- une **analyse exploratoire approfondie**
- une **sélection raisonnée des variables**
- une **interprétation métier adaptée au contexte médical**
- une **démarche reproductible et orientée production**

---

## 🧠 Problématique métier

> Peut-on identifier efficacement la présence d’un cancer du sein à partir de mesures morphologiques cellulaires, tout en conservant une bonne capacité d’interprétation des résultats ?

Dans un contexte médical, l’objectif principal est de **maximiser la détection des cas malins**, tout en limitant les faux négatifs.

---

## 📊 Données utilisées

- **Source** : Wisconsin Breast Cancer Dataset
- **Observations** : 569 individus
- **Variables initiales** : 32
- **Cible** : `diagnosis`  
  - `B` : tumeur bénigne  
  - `M` : tumeur maligne  

### Organisation des données

```text
data/
├── raw/        → données brutes
└── processed/  → données nettoyées et filtrées
```

## 🔍 Analyse exploratoire & préparation des données

📓 **Notebook** : `01_Data_Cleaning_EDA.ipynb`

### Étapes principales

- Vérification de la structure du dataset  
- Analyse descriptive (`df.describe()`)  
- Étude des distributions (histogrammes, boxplots)  
- Analyse des outliers avec interprétation métier  
- Comparaison des profils bénins vs malins  
- Étude de la corrélation entre variables  

💡 **Important**  
Dans un contexte médical, les outliers ne sont **pas supprimés**, car ils représentent souvent des **cas pathologiques critiques** que le modèle doit apprendre à détecter.

---

## 🧬 Sélection des variables discriminantes

Les variables finales ont été sélectionnées selon :

- leur **pouvoir discriminant** observé
- leur **corrélation avec la cible**  
- la **limitation de la redondance** entre variables  
- leur **cohérence métier**

### Variables retenues pour la modélisation

- `area_worst`  
- `radius_worst`  
- `perimeter_worst`  
- `concavity_mean`  
- `concave_points_mean`  

---

## 🤖 Modélisation

📓 **Notebook** : `02_Logistic_Regression_Modeling.ipynb`

### Étapes du pipeline

- Encodage de la variable cible  
- Séparation **Train / Test**  
- Standardisation des variables numériques  
- Entraînement d’un modèle de **régression logistique**  
- Gestion du déséquilibre des classes (`class_weight="balanced"`)

---

## 📈 Évaluation du modèle

### Métriques obtenues sur le jeu de test

- **Accuracy** : 91.2 %  
- **Precision** : 89.6 %  
- **Recall** : 89.6 %  
- **F1-score** : 89.6 %  
- **ROC-AUC** : élevée (bonne capacité de discrimination)

📌 Le modèle présente un **bon équilibre entre précision et rappel**, ce qui est essentiel dans un **cadre médical**.

---

## 💾 Sauvegarde du modèle

Les éléments suivants sont sauvegardés pour une utilisation ultérieure :

```texte
models/
├── logistic_regression_model.pkl
└── standard_scaler.pkl
```

Cela permet :

- la **reproductibilité**
- l’**inférence hors notebook**
- une **future mise en production**

---

## 🧪  Exécution du modèle

📄 **Fichier** : `app.py`

Ce script permet :

- de charger le **modèle** et le **scaler**
- de saisir des **valeurs utilisateur**
- de produire une **prédiction en temps réel** (*Bénin / Malin*)

### Exécution

```bash
python app.py
```
---

## 🗂️ Structure du projet

```bash
Healthcare-Analysis-Breast-Cancer-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│   ├── 01_Data_Cleaning_EDA.ipynb
│   └── 02_Logistic_Regression_Modeling.ipynb
│
├── app.py
├── README.md
└── requirements.txt
```
---

## 🚀 Perspectives d’amélioration

- Comparaison avec d’autres modèles (SVM, Random Forest)
- Optimisation des hyperparamètres
- Mise en production via une API (FastAPI)
- Intégration d’une interface utilisateur
- Analyse de l’importance des variables

---

## 🧩 Conclusion

Ce projet illustre une démarche complète de data science, allant de l’exploration des données jusqu’à l’exploitation d’un modèle de prédiction, avec une attention particulière portée à :

- la compréhension métier
- la rigueur méthodologique
- l’interprétabilité des résultats
