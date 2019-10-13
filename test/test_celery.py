from celery import Celery
from celery.signals import worker_ready

app = Celery(__name__, broker='redis://localhost:6379/0')

@worker_ready.connect()
def hello_world(**kwargs):
	print('hello_world')
	real_task.delay(10)


@app.task
def real_task(x):
	print(x*x)
