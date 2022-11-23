FROM python:3.10

# all the command will run from this directory - much like 'cd /usr/src/app'
WORKDIR /usr/src/app

# same as 'COPY requirements.txt /usr/src/app'
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]