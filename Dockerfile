FROM python:alpine

COPY . .

CMD ["python3", "loadbalancer.py"]
