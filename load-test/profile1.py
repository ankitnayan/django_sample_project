from locust import HttpLocust, TaskSet

def polls(l):
    l.client.get("/polls/2xx_success/")

def error(l):
    l.client.get("/polls/4xx_not_found/")

def exception(l):
    l.client.get("/polls/5xx_exception/")

class UserBehavior(TaskSet):
    tasks = {polls: 2, error: 1, exception: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000