proc_demon=$(netstat -ano | findstr 0.0.0.0:8000 | awk '{print $NF}' | cut -d'/' -f1)

taskkill -PID $proc_demon -F