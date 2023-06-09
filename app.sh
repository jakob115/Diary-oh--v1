#!/bin/sh

# ===== set variables =====
export FLASK_APP=app.py
export FLASK_ENV=development
#export FLASK_ENV=production

# ==== executable file ====
# If you make this file executable you will be able to run it.
# This is similar how batch (*.bat) files work in Windows.

# --------- Linux ---------
# To make file executable run the following command:
# > chmod +rx app.sh
# To execute file run the following command:
# > ./app.sh

# --------- MacOS ---------
# To make file executable first rename it from 'app.sh' to
# 'app.command' and then run the following command:
# > chmod +rx app.command
# To execute file run the following command:
# > ./app.command
# You can also just double-click the 'app.command' file.

# ===== running flask =====
# flask run
# Above command should work. Anyway just use command below because
# it works even if the path is not specified correctly ...
python -m flask run
