FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set Python Path and Port
ENV PYTHONPATH=/app
ENV PORT=8000

# Start FastAPI application allowing dynamic Cloud Run port
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
