from python:3.8
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev git libffi python3-dev
RUN apt update && apt install -y libffi-dev libnacl-dev python3-dev ffmpeg && rm -rf /var/lib/apt/lists/*
copy requirements.txt /
run pip3 install -r /requirements.txt
ENV PYTHONPATH="/simplebot:${PYTHONPATH}"
ARG token=
ENV TOKEN="${token}"
copy . /
entrypoint ["python", "/simplebot/run.py"]
