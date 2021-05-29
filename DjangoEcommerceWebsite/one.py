from celery import Celery
from time import sleep

app = Celery('one', backend='rpc://', broker='amqp://localhost')


@app.task
def add(x, y):
    sleep(5)
    return x + y
