# USTC-Register
A simple flask app for event registration.

**WARNING: THIS IS A DEMO VERSION UNDER DEVELOPMENT.**

# Init

Modify the `ADMIN_USER`, `ADMIN_PASS`, `USTC_CAS_URL`, `SECRET_KEY` in `config_sample.py`.

```
cp config_sample.py config.py
pip install -r requirements.txt
python db_create.py
python db_migrate.py
python db_upgrade.py
```

# Run
```
python app.py
```

# Manager

```
http://YOUR_HOST:YOUR_PORT/admin
```

# About CAS
See https://github.com/volltin/USTC-CAS-Redirect