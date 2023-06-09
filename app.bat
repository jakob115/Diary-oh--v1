:: ===== set variables =====
set FLASK_APP=app.py
set FLASK_ENV=development
::set FLASK_ENV=production

:: ===== running flask =====
:: flask run
:: Above command should work. Anyway just use command below because
:: it works even if the path is not specified correctly ...
python -m flask run

pause
