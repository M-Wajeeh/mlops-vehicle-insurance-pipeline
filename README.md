```md
# Vehicle Insurance MLOps Pipeline

An **end-to-end production-grade MLOps project** that covers everything from data ingestion using MongoDB, model training, evaluation, deployment on AWS, and CI/CD automation using GitHub Actions, Docker, ECR, and EC2.

This project follows **industry-level modular architecture**, proper logging, exception handling, versioning, and cloud deployment best practices.

---

## Project Highlights

- Modular MLOps architecture
- MongoDB Atlas for data storage
- End-to-end ML pipeline (Ingestion → Validation → Transformation → Training → Evaluation → Pusher)
- AWS S3 for model registry
- Dockerized application
- CI/CD using GitHub Actions
- Deployment on AWS EC2 (Self-hosted runner)
- FastAPI-based prediction pipeline

---

## Project Structure

```

├── artifact/
├── config/
│   └── schema.yaml
├── constants/
├── entity/
│   ├── config_entity.py
│   ├── artifact_entity.py
│   ├── estimator.py
│   └── s3_estimator.py
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   ├── configuration/
│   │   ├── mongo_db_connections.py
│   │   └── aws_connection.py
│   ├── aws_storage/
│   ├── data_access/
│   ├── utils/
│   │   └── main_utils.py
├── notebook/
│   ├── mongoDB_demo.ipynb
│   └── EDA_Feature_Engineering.ipynb
├── static/
├── templates/
├── app.py
├── demo.py
├── requirements.txt
├── setup.py
├── pyproject.toml
├── Dockerfile
├── .dockerignore
├── .gitignore
└── .github/workflows/aws.yaml

````

---

## Environment Setup

### 1️⃣ Create Project Template
```bash
python template.py
````

---

### 2️⃣ Local Package Setup

Add proper configuration in:

* `setup.py`
* `pyproject.toml`

📄 Refer to `crashcourse.txt` for detailed explanation.

---

### 3️⃣ Create & Activate Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

## MongoDB Atlas Setup

### 4️⃣ MongoDB Configuration Steps

1. Sign up on **MongoDB Atlas**
2. Create a new project
3. Create **M0 Cluster**
4. Create database user (username & password)
5. Network Access → Allow IP:

```
0.0.0.0/0
```

6. Get Connection String:

```
Python Driver → Version 3.6+
```

---

### 5️⃣ Notebook Setup

```text
notebook/
├── mongoDB_demo.ipynb
```

* Load dataset
* Push data to MongoDB
* Verify in **Atlas → Browse Collections**

---

## Logging & Exception Handling

* Custom logger implementation
* Centralized exception handling
* Tested using `demo.py`

---

## Data Ingestion Pipeline

### Key Components

* `constants/__init__.py`
* `configuration/mongo_db_connections.py`
* `data_access/proj1_data.py`
* `entity/config_entity.py`
* `entity/artifact_entity.py`
* `components/data_ingestion.py`

---

### MongoDB Environment Variable Setup

#### Bash

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $MONGODB_URL
```

#### PowerShell

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $env:MONGODB_URL
```

 Add `artifact/` to `.gitignore`

---

## Data Validation

* Schema validation using `schema.yaml`
* Column, datatype, and null checks
* Drift detection support

---

## Data Transformation

* Feature engineering
* Encoding & scaling
* Train-test split
* Stored as transformation artifacts

---

## Model Trainer

* Model training using sklearn
* Evaluation metrics tracking
* Model serialization

---

## AWS Setup (S3 + IAM)

### AWS IAM User Creation

* User: `firstproj`
* Policy: `AdministratorAccess`
* Generate Access Keys

---

### Environment Variables

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

---

### Constants Configuration

```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```

---

### S3 Bucket Setup

* Bucket Name: `my-model-mlopsproj`
* Region: `us-east-1`
* Public access allowed

---

## Model Evaluation & Model Pusher

* Compare new model vs existing production model
* Push best model to S3 model registry

---

## Prediction Pipeline

* FastAPI based API
* `/predict` endpoint
* `/training` endpoint for model retraining

---

## Docker & CI/CD

### Docker Setup

* `Dockerfile`
* `.dockerignore`

---

### GitHub Actions Workflow

* `.github/workflows/aws.yaml`
* Automated build & deployment

---

## Deployment (AWS EC2)

### EC2 Setup

* Ubuntu Server 24.04
* Instance: `t2.medium`
* Open Port: `5080`

---

### Docker Installation

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

### GitHub Self-Hosted Runner

* Connect EC2 with GitHub Actions
* Runner runs CI/CD pipeline

---

## GitHub Secrets

Add the following secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

---

## Application Access

```
http://<EC2_PUBLIC_IP>:5080
```

---

## Tech Stack

* Python
* MongoDB Atlas
* Scikit-learn
* FastAPI
* Docker
* AWS (S3, ECR, EC2, IAM)
* GitHub Actions

---
