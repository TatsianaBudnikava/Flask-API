from locust import HttpUser, task, between

class EmployeeUser(HttpUser):
    wait_time = between(1, 2)  # Simulate the behavior of real users (1-2 seconds pause)

    @task(3)
    def get_employees(self):
        self.client.get("/employees")

    @task(2)
    def get_skills(self):
        self.client.get("/skills")

    @task(1)
    def search_employee(self):
        self.client.get("/employees/search?q=Charlie")
