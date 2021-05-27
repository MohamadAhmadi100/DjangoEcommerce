from celery import Celery
from time import sleep


app= Celery('one', broker='amqp://localhost')
def add(x, y):
    sleep(5)
    return x + y
