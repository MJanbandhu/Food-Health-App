Start-Process powershell -ArgumentList "-NoExit -Command `"cd backend; .\venv\Scripts\activate; set PYTHONPATH=.; uvicorn app.main:app --reload`""
cd frontend
npm run dev
