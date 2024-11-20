from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import Optional
import joblib
import numpy as np

# Create FastAPI app instance
app = FastAPI(
    title="Isolation Forest Anomaly Detection Service",
    description="A web service for anomaly detection using Isolation Forest",
    version="1.0.0"
)

# Load the pre-trained model
try:
    model = joblib.load('model.joblib')
except Exception as e:
    print(f"Error loading model: {e}")
    raise RuntimeError("Failed to load the model. Please ensure the model file exists.")

# Define the input data model
class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    score: Optional[bool] = False

    # Validator to ensure that features have valid float inputs
    @validator('feature_1', 'feature_2')
    def validate_features(cls, v):
        if not isinstance(v, float):
            raise ValueError('Each feature must be a float')
        return v

    # Add configuration and example within the PredictionRequest class
    class Config:
        schema_extra = {
            "example": {
                "feature_1": 0.0,
                "feature_2": 0.0,
                "score": False
            }
        }

# Rest of your code remains the same
@app.post("/prediction")
async def predict(request: PredictionRequest):
    """
    Make predictions using the Isolation Forest model.
    Returns is_inlier prediction and optionally the anomaly score.
    """
    try:
        # Use feature_1 and feature_2 directly
        features = np.array([request.feature_1, request.feature_2]).reshape(1, -1)
        
        response = {}
        prediction = model.predict(features)
        response["is_inlier"] = bool(prediction[0])
        
        if request.score:
            anomaly_score = model.score_samples(features)
            response["anomaly_score"] = float(anomaly_score[0])
        
        return response
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

@app.get("/model_information")
async def get_model_info():
    """
    Return the model's hyperparameters.
    """
    try:
        return model.get_params()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving model information: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

