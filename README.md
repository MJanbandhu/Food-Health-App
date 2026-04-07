# Food & Health Smart Application 🥗

A fully functional, intelligent "Food & Health Smart Application" designed to help users track their nutrition, receive personalized health recommendations, and achieve their health goals using AI.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Getting Started (Local Development)](#getting-started-local-development)
  - [Prerequisites](#prerequisites)
  - [Using the Quick Run Script](#using-the-quick-run-script)
  - [Manual Setup](#manual-setup)
- [API Documentation](#api-documentation)
- [Deployment on GCP](#deployment-on-gcp)
- [Project Directory](#project-directory)

---

## Features

1. **Smart Scanner Mock**: Take a picture of your food (simulated) to automatically detect calories and food type.
2. **Food Logging & Analytics**: Manually track daily food intake and view your statistics.
3. **Calorie Dashboard**: Instantly see your consumed calories vs. your daily goal along with health alerts if you exceed recommended bounds.
4. **AI Health Recommendations**: Dynamic insights delivered by Vertex AI (mocked for local MVP) to keep you on a healthier track.
5. **REST API**: Fully modular, typed, and validated backend structure using FastAPI & Pydantic.

## Tech Stack

- **Frontend**: React.js with Vite + Tailwind CSS via CDN.
- **Backend**: FastAPI (Python) with SQLAlchemy ORM and Alembic migrations.
- **Database**: PostgreSQL (Cloud SQL) via local SQLite fallback mapping during initial dev.
- **AI Integration**: Google Cloud Vertex AI logic integration placeholder.
- **Deployment & Infra**: Dockerized components, targeting Google Cloud Run.

---

## Architecture

The project consists of a strictly decoupled architecture:
- **Backend (`/backend`)**: Follows the `app/api`, `app/models`, `app/services` directory structure design. Using `uvicorn` and `FastAPI` for async endpoints. 
- **Frontend (`/frontend`)**: Built securely with Vite React. It handles the UI state dynamically parsing data from the API.

---

## Getting Started (Local Development)

### Prerequisites
- Node.js (v18+)
- Python 3.10+
- Git

### Using the Quick Run Script (Windows)
For an instant boot-up containing both the frontend and backend:
```powershell
.\run.ps1
```
This script will:
1. Activate the Python virtual environment.
2. Start the FastAPI uvicorn server in a separate background window.
3. Run the Vite development server for the frontend.

### Manual Setup
**1. Setup the Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # (On Windows)
pip install -r requirements.txt
set PYTHONPATH=.
uvicorn app.main:app --reload
```
*The backend server will run natively at `http://localhost:8000`.*

**2. Setup the Frontend:**
```bash
cd frontend
npm install
npm run dev
```
*The frontend reacts application will be available at `http://localhost:5173`.*

---

## API Documentation
Because the backend runs on FastAPI, comprehensive interactive API documentation is automatically generated.
With the backend running, visit:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Deployment on GCP

### 1. Dockerization
The project includes (or will soon include) Dockerfiles for both frontend and backend.
To build images:
```bash
docker build -t food-app-backend ./backend
docker build -t food-app-frontend ./frontend
```

### 2. Google Cloud Run
Push images to Google Artifact Registry:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/food-app-backend ./backend
gcloud run deploy food-app-backend --image gcr.io/YOUR_PROJECT_ID/food-app-backend --platform managed
```
*(Repeat similarly for the frontend, noting that it will be a static Nginx multi-stage build)*

### 3. Cloud SQL
Connect the SQLAlchemy `POSTGRES_SERVER` and database credentials in `.env` matching your Cloud SQL setup configurations.

---

## Code Quality

This project conforms to stringent engineering standards:
- **PEP 8**: Python code styled efficiently.
- **Pydantic**: Deep structural schema validation for every end-point.
- **Docker**: Portable code dependencies.
- **Security**: JWT-based Authentication hooks configured within the Auth routers.
