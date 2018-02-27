# Test App
## Running Tests
```bash
pip install -r dev_requirements.txt
tox
```

## Running dev application
```bash
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites/fixtures/sites.json
./manage.py runserver
```


