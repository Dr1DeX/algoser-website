run_cmd="cd backend/algoser && python -u manage.py runserver 0.0.0.0:8000 > ../log_server.log 2>&1 &"
run_cmd+="cd frontend && npm run dev > ../log_nextapp.log 2>&1 &"
nohup sh -c "$run_cmd" &