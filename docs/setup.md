# Setup Instructions

1. Copy `cloud/env.example` to `backend/.env`.
2. Configure settings inside the `.env`.
3. Launch via Docker: `docker-compose up --build`.

To test migrations:
`cd backend && alembic upgrade head`
