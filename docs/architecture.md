# Architecture Overview

- **Frontend**: Vite React SPA hosted theoretically on Google Cloud Run statically using Nginx Alpine multi-stage. Connects over CORS.
- **Backend**: FastAPI layered monolith.
  - `routers/`: Controller logic processing HTTP verbs.
  - `schemas/`: Pydantic input/output parsing.
  - `services/`: Heavy algorithm and logic.
  - `models/`: Database structural definitions.
