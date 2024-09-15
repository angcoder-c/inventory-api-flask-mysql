FROM python:3.11-alpine

WORKDIR .
    
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev pkgconf && \
    apk add --no-cache --update python3 && \ 
    pip install --upgrade pip setuptools && \ 
    pip install --upgrade pip
    
RUN pip install --no-cache-dir -r requirements.txt
    
COPY . .
    
USER root

EXPOSE 8080
    
CMD ["python", "main.py"]