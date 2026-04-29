import torch
import numpy as np

# ── Load model checkpoint ───────────────────────────
MODEL_PATH = "ecg_module/models/ecg_attention_calibrated.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

checkpoint = torch.load(MODEL_PATH, map_location=device)

model = checkpoint["model"]
model.load_state_dict(checkpoint["model_state_dict"])
model.to(device)
model.eval()

# Mean & std (IMPORTANT for normalization)
mean = checkpoint["mean"]
std = checkpoint["std"]

# Class mapping → Risk levels
CLASS_TO_LEVEL = {
    0: "Low",     # NORM
    1: "High",    # MI
    2: "Medium",  # STTC
    3: "Medium",  # CD
    4: "High"     # HYP
}


# ── Preprocess ECG signal ───────────────────────────
def preprocess(ecg_signal):
    ecg = np.array(ecg_signal, dtype=np.float32)

    # Ensure shape (1, length)
    if len(ecg.shape) == 1:
        ecg = np.expand_dims(ecg, axis=0)

    # Normalize
    ecg = (ecg - mean) / (std + 1e-8)

    # Convert to tensor
    ecg_tensor = torch.tensor(ecg, dtype=torch.float32).unsqueeze(0).to(device)

    return ecg_tensor


# ── FINAL PREDICT FUNCTION ──────────────────────────
def predict(ecg_signal):
    """
    ecg_signal: list or numpy array
    """

    ecg_tensor = preprocess(ecg_signal)

    with torch.no_grad():
        outputs = model(ecg_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]

    label = int(np.argmax(probs))

    return {
        "level": CLASS_TO_LEVEL[label],
        "score": float(probs[label])
    }


# ── TEST ───────────────────────────────────────────
if __name__ == "__main__":
    # Dummy ECG signal (replace later with real input)
    sample_signal = np.random.randn(1000)

    result = predict(sample_signal)
    print(result)