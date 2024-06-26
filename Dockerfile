# This code has been almost completely borrowed from https://fastapi.tiangolo.com/deployment/docker/

FROM python:latest

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./app /app

# 
CMD ["fastapi", "run", "app/main.py", "--port", "80"]