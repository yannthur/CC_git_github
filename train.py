import yaml
import torch
from src.data import load_data
from src.models import build_model


def train(config_path: str = "config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    print(f"Training {config['project']['name']} v{config['project']['version']}")

    train_loader, val_loader = load_data(config["data"])
    model = build_model()

    optimizer = torch.optim.Adam(
        model.parameters(), lr=config["training"]["learning_rate"]
    )
    criterion = torch.nn.CrossEntropyLoss()

    for epoch in range(config["training"]["epochs"]):
        model.train()
        for batch in train_loader:
            optimizer.zero_grad()
            outputs = model(batch["data"])
            loss = criterion(outputs, batch["labels"])
            loss.backward()
            optimizer.step()

        print(
            f"Epoch {epoch + 1}/{config['training']['epochs']} - Loss: {loss.item():.4f}"
        )

    torch.save(model.state_dict(), f"{config['training']['model_save_path']}/model.pt")
    print("Model saved!")


if __name__ == "__main__":
    train()
