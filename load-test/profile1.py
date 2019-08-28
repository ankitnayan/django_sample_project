from locust import HttpLocust, TaskSet

def polls(l):
    l.client.get("/polls")

def error(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {polls: 2, error: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000