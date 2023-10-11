# chatbot
Backend engine for a simple chatbot

## Start backend engine locally

### With virtualenv
env FLASK_APP=app.py FLASK_DEBUG=1 flask run

### With docker
docker run -p 5000:8000 -e PORT=8000 <image_name>