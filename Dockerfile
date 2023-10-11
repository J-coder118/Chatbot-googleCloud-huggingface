FROM python:3.7-slim

WORKDIR /app
COPY app.py .
COPY load_model.py .
COPY model.py .
COPY requirements.txt .

# Install Python dependencies.
RUN pip install -r requirements.txt
RUN python load_model.py

# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 app:app