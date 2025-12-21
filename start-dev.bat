call venv\Scripts\activate

alembic upgrade head

start cmd /k uvicorn app.main:app --reload
cd smart-poultry-dashboard && start cmd /k npm run dev

timeout /t 5

python scripts\simulate_pen.py
