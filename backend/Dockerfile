FROM python:3.11.9-slim

COPY requarement.txt requarement.txt
RUN pip install -r requarement.txt

COPY . .


CMD [ "python", "main.py" ]