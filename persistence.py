import mlflow
import mlflow.sklearn
import shutil

# Import the model from model.py
from model import model, x  # Ensure to import x for prediction as well

# Define the path where the model will be saved
model_path = "models/logit_games_v1"

# Remove any existing model at the specified path (optional)
# shutil.rmtree(model_path)  # Uncomment this line if you want to clear the previous model

# Save the model using MLflow
mlflow.sklearn.save_model(model, model_path)

# Load the model back using MLflow
loaded_model = mlflow.sklearn.load_model(model_path)

# Use the loaded model for prediction
print(loaded_model.predict_proba(x))

