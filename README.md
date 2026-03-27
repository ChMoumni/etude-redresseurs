# Étude des redresseurs non commandés

Ce projet présente une étude théorique, expérimentale et numérique des redresseurs non commandés : mono-alternance, double-alternance (pont de Graëtz) et double-alternance avec filtrage capacitif.

## 📁 Contenu du dépôt

- `rapport/` : dossier contenant le rapport final au format PDF (`Les_redresseurs_etude.pdf`)
- `code/` : dossier contenant le script Python de simulation (`Simulation_redresseurs.py`)

## 🛠️ Technologies utilisées

- **Python 3** – NumPy, Matplotlib, SciPy pour la simulation et l’analyse spectrale
- **LaTeX** – Rédaction du rapport, schémas électriques avec `circuitikz`, insertion de code avec `minted`
- **Matériel** – GBF, oscilloscope, multimètre pour la validation expérimentale

## 🚀 Utilisation

1. Cloner le dépôt :
   ```bash
   git clonechttps://github.com/ChMoumni/etude-redresseurs.git

mais ducoup cette section elle fait bien partie du redue OUI ou NON : Installer les dépendances :

bash
pip install numpy matplotlib scipy
Lancer le script :

bash
python code/Simulation_redresseurs.py
Choisir le type de redresseur (1, 2 ou 3) et visualiser les courbes temporelles ainsi que les spectres de fréquence.
📄 Résultats

Les figures générées sont automatiquement sauvegardées au format PDF dans le dossier d’exécution. Elles sont également intégrées dans le rapport final.

🔗 Liens

Rapport PDF
Code source
📅 Année

2025 – Travail personnel dans le cadre d’une première approche de l’électronique de puissance
