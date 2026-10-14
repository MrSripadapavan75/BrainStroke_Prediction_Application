# BrainStroke_Prediction_Application

A machine learning web application that predicts stroke risk from user-provided health and lifestyle features. The model is served through Flask and can be run locally or inside Docker.

> **Disclaimer:** This project is for educational and demonstration purposes only. Its output is not a medical diagnosis and must not be used to make healthcare decisions. Consult a qualified healthcare professional for medical advice.

## Features

- Machine learning predictions through a Flask application
- HTML interface served from the `templates/` directory
- JSON prediction endpoint at `/predict`
- Model loading with Joblib
- Docker image build and containerized execution

## Tech Stack

- Python
- Flask
- Pandas and NumPy
- scikit-learn
- Joblib
- Gunicorn
- HTML
- Docker

## Project Structure

```text
BrainStroke_Prediction_Application/
├── templates/
│   └── index.html
├── app.py
├── brainstroke_model.pkl
├── brain.csv
├── train.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

Your actual filenames may differ. Keep the model filename in `app.py` consistent with the saved model file.

## Input Features

The application expects these features:

- `gender`
- `age`
- `hypertension`
- `heart_disease`
- `ever_married`
- `work_type`
- `Residence_type`
- `avg_glucose_level`
- `bmi`
- `smoking_status`

Input values and column names must match the preprocessing and feature schema used to train the saved model.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/BrainStroke_Prediction_Application.git
cd BrainStroke_Prediction_Application
```

Replace `<your-username>` with your GitHub username.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

Ensure `requirements.txt` includes the libraries used by the application, such as Flask, pandas, NumPy, scikit-learn, Joblib, and Gunicorn.

### 4. Start the Flask application

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Run with Docker

Ensure Docker Desktop is running and that the project directory contains the `Dockerfile`, `requirements.txt`, `app.py`, model file, and `templates/index.html`.

### 1. Build the image

```powershell
docker build -t brainstrokeapp .
```

### 2. Start the container

```powershell
docker run -d -p 5000:5000 --name brainstrokeapp brainstrokeapp
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 3. Useful Docker commands

View running containers:

```powershell
docker ps
```

View application logs:

```powershell
docker logs brainstrokeapp
```

Stop the container:

```powershell
docker stop brainstrokeapp
```

Remove the stopped container:

```powershell
docker rm brainstrokeapp
```

If the container name or host port is already in use, stop or remove the existing container as appropriate, or choose a different host port.

## Prediction API

The Flask application exposes a `POST /predict` endpoint that expects JSON.

Example request body (use category values accepted by your trained model):

```json
{
  "gender": "Male",
  "age": 67,
  "hypertension": 0,
  "heart_disease": 1,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 180.5,
  "bmi": 29.4,
  "smoking_status": "formerly smoked"
}
```

Example request using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"gender\":\"Male\",\"age\":67,\"hypertension\":0,\"heart_disease\":1,\"ever_married\":\"Yes\",\"work_type\":\"Private\",\"Residence_type\":\"Urban\",\"avg_glucose_level\":180.5,\"bmi\":29.4,\"smoking_status\":\"formerly smoked\"}"
```

A successful response should contain `prediction` and `result` fields. The actual prediction depends on the trained model.

## Model and Data

- `train.py` contains the model-training workflow, if included in your project.
- `brain.csv` is the dataset file included in this project.
- `brainstroke_model.pkl` is the saved model loaded by the Flask application.

Only load pickle/Joblib model files from trusted sources. For reproducible deployment, use compatible Python and scikit-learn versions between training and serving.

## Troubleshooting

- **Model file not found:** Confirm `brainstroke_model.pkl` is in the project directory and copied into the Docker image.
- **Template not found:** Confirm `index.html` is inside the `templates/` folder.
- **Port 5000 is already allocated:** Stop the container using the port, or map another host port, for example `-p 5001:5000`, then visit `http://127.0.0.1:5001`.
- **Prediction request fails:** Ensure the request is valid JSON and contains all ten required fields. Check logs with `docker logs brainstrokeapp`.
- **Feature errors:** Confirm feature names, data types, category values, and preprocessing agree with the training pipeline.

## Future Improvements

- Add automated tests for the prediction endpoint
- Validate feature ranges and allowed category values
- Add structured logging and production error handling
- Deploy to a cloud hosting platform
- Document model evaluation metrics and limitations

## Author

**SRIPADA PAVAN KUMAR**  

GitHub :https://github.com/MrSripadapavan75/

output_link :https://brainstroke-prediction-application.onrender.com/ <--- Deployed it in **RENDER**

---

If you use or extend this project, please retain the educational-use and medical disclaimer.
