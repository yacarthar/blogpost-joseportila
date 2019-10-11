# locustfile.py
from locust import HttpLocust, TaskSet, task 

class UserTaskSet(TaskSet):
    @task
    def get_index_task(self): 
        self.client.get("/post")

    @task
    def post_index_task(self):        # New task here
        payload = {'test': 'cheri'}
        self.client.post("/post", data=payload)

class User(HttpLocust):
    task_set = UserTaskSet 
    min_wait = 5000 
    max_wait = 15000
    host = "http://localhost:5000"