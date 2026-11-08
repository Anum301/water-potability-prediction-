import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dataset load karo
try:
    df = pd.read_csv("water_potability.csv")
    df = df.fillna(df.mean(numeric_only=True))
    X = df.drop("Potability", axis=1)
    y = df["Potability"]
except:
    # Agar CSV na ho to dummy data se train karo
    import numpy as np
    np.random.seed(42)
    X = pd.DataFrame(np.random.rand(500, 9), columns=["ph","Hardness","Solids","Chloramines","Sulfate","Conductivity","Organic_carbon","Trihalomethanes","Turbidity"])
    y = (X["ph"] > 0.4).astype(int)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl - Made by Samina")