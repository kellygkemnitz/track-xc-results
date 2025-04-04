FROM python:3.12

WORKDIR /track-xc-results

COPY ../requirements.txt /track-xc-results/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./data /track-xc-results/data/
COPY ./modules /track-xc-results/modules/
COPY ./app /track-xc-results/app/

EXPOSE 8002

CMD ["python3", "/track-xc-results/app/app.py"]
