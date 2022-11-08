# Homework №1
### _To get started_
```
export LOCAL_DATA_DIR=$(pwd)/data
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker-compose up --build
```

### _To run tests_
```
docker exec -it airflow_ml_dags_scheduler_1 bash
pip3 install pytest
python3 -m pytest --disable-warnings tests/test_dag_structure.py
python3 -m pytest --disable-warnings tests/test_dag_loading.py
```
