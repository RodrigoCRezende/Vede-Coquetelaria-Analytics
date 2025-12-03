@echo off
echo LIGANDO O SISTEMA VEDE...

start cmd /k "cd ia && python app.py"
start cmd /k "cd backend && node server.js"

timeout /t 3
start frontend/index.html

echo PRONTO! O sistema esta rodando.
pause