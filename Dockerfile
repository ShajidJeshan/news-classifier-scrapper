#FROM  python:3.10.13-alpine3.18
FROM python:3.10.12-slim-bullseye
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf
WORKDIR /api
COPY . /api
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
