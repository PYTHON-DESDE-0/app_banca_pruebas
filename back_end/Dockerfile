

ARG VERSION=3.13.1-slim-bookworm 
FROM python:${VERSION}      

WORKDIR /code

COPY ./requirements-linux.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

EXPOSE 8000

COPY main.py database.py /code

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]