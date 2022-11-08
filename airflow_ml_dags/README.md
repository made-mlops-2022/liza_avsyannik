export LOCAL_DATA_DIR=$(pwd)/data
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

pip3 install pytest
docker exec -it airflow_ml_dags_scheduler_1 bash
python3 -m pytest --disable-warnings test_dag_structure.py
python3 -m pytest --disable-warnings test_dag_loading.py
