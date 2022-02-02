from python:3.8
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev git libffi python3-dev
RUN apt update && apt install -y libffi-dev libnacl-dev python3-dev ffmpeg && rm -rf /var/lib/apt/lists/*
run pip install psycopg2
copy requirements.txt /
run pip3 install -r /requirements.txt
copy . /
ENV PYTHONPATH="/simplebot:${PYTHONPATH}"
entrypoint ["/entrypoint.py"]
