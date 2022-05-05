from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_req(self):
        self.client.get("/")
