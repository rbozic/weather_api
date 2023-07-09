FROM python

COPY ./*.py /app/
COPY ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
