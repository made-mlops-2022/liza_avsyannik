FROM python:3.8.15-slim-buster
RUN python3 -m pip install --upgrade pip

COPY main.py schemas.py run.sh requirements.txt ./

RUN pip3 install -r requirements.txt

ENV PATH_TO_MODEL="model.pkl"
ENV PATH_TO_TRANSFORMER="transformer.pkl"

EXPOSE 8000

CMD ["bash", "run.sh"]
