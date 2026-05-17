import joblib

#Load Model

model = joblib.load("model/model.pkl")

# Example input
sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

print("Pridiction: ", prediction)
