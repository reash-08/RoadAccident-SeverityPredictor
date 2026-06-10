import joblib

# Load old package (contains encoders)
old_package = joblib.load("road_accident_model.pkl")

# Load best tuned model
tuned_model = joblib.load("tuned_model.pkl")

# Create new deployment package
new_package = {
    "model": tuned_model,
    "encoders": old_package["encoders"],
    "severity_encoder": old_package["severity_encoder"]
}

joblib.dump(new_package, "road_accident_model_final.pkl")

print("Created road_accident_model_final.pkl")

import joblib

package = joblib.load("road_accident_model_final.pkl")

print(package["model"].get_params()["n_estimators"])
print(package["model"].get_params()["max_depth"])
print(package["model"].get_params()["min_samples_split"])
