from locust import HttpUser, between, task


class WebsiteDjangoAdmin(HttpUser):
    wait_time = between(3, 5)

    def auth(self):
        response = self.client.get("/admin/login")
        csrf_token = response.cookies['csrftoken']

        headers = {"X-CSRFToken": csrf_token}
        self.client.post("/admin/login", {
            "username": "admin",
            "password": "admin1234"
        }, headers=headers)

    def on_start(self):
        self.auth()

    @task(2)
    def user_page(self):
        self.client.get("/admin/auth/user", cookies=self.client.cookies.get_dict())

    @task
    def group_page(self):
        self.client.get("/admin/auth/group", cookies=self.client.cookies.get_dict())
