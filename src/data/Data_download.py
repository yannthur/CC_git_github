import shutil
from pathlib import Path

import kagglehub

dataset_name = "kaushalnandania/credit-card-fraud-detection"
path = kagglehub.dataset_download(dataset_name)

data_raw = Path("data/raw")
data_raw.mkdir(parents=True, exist_ok=True)

for file in Path(path).iterdir():
    dest = data_raw / file.name
    shutil.move(file, dest)
    print(f"Moved: {file.name} -> {dest}")
