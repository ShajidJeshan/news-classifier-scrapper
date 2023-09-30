# FROM  python:3.10.13-alpine3.18
# WORKDIR /api
# COPY . /api
# RUN pip install -r requirements.txt
# EXPOSE 8000
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]