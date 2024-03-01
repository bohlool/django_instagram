FROM python:3.11

WORKDIR /django_instagram

COPY ./requirements.txt ./

RUN pip install --no-cache -r requirements.txt

COPY . .

RUN mkdir -p /vol/media
RUN mkdir -p /vol/static

RUN python ./manage.py migrate
RUN python ./manage.py collectstatic --no-input

EXPOSE 8000

CMD gunicorn django_instagram.wsgi:application --bind 0.0.0.0:8000 --workers 2
