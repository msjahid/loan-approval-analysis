import pickle
import os

# Dynamically get the directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the trained model relative to this script
MODEL_PATH = os.path.join(BASE_DIR, 'model_storage', 'gnb_model.pkl')


# Load the pre-trained model
def load_model():
    try:
        # Check if the model file exists
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please train and save the model.")

        # Load the model
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError as e:
        print(e)
        return None
    except pickle.UnpicklingError as e:
        print(f"Error: Failed to unpickle the model file. Details: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the model: {e}")
        return None


# Prediction function
def predict(model, features):
    try:
        prediction = model.predict([features])
        return prediction[0]  # Return the predicted label (e.g., "Approved" or "Not Approved")
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
