FROM python:3.9

WORKDIR /usr/app

COPY . ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]