# Stage 1: Build the React frontend
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build the FastAPI backend and serve static files
FROM python:3.10-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ /app/backend/

# Copy built frontend from Stage 1 into the backend's static directory
COPY --from=frontend-builder /app/frontend/dist /app/backend/dist

# Set Python Path
ENV PYTHONPATH=/app/backend
ENV PORT=8080

# Start FastAPI application
CMD uvicorn backend.app.main:app --host 0.0.0.0 --port ${PORT:-8080}
