# CC_git_github

ML project with data pipeline, model training and evaluation.

## Structure

```
├── data/           # Données (raw, processed, external)
├── notebooks/      # Jupyter notebooks
├── src/            # Code source
│   ├── data/       # Ingestion & preprocessing
│   ├── features/   # Feature engineering
│   ├── models/     # Architectures
│   └── evaluation/ # Métriques
├── models/         # Modèles entraînés
├── config.yaml     # Configuration
├── train.py        # Script d'entraînement
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Entraînement

```bash
python train.py
```
