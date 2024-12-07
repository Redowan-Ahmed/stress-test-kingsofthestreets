from locust import HttpUser, task, between


class LandingPageLoad(HttpUser):
    @task
    def Home(self):
        self.client.get("/")
        self.client.get("/fighters")
        self.client.get("/upcoming-event")
        self.client.get("/login")
        self.client.get("/fight-application")
	self.client.get("/event")

    @task
    def shop(self):
        self.client.get("/shop")

    @task
    def product(self):
        self.client.get("/produkt/underground-fight-club-t-shirt")
        self.client.get("/produkt/king-of-the-streets-gta-version-t-shirt")
        self.client.get("/produkt/king-of-the-streets-t-shirt-black-white")
        self.client.get("/produkt/king-of-the-streets-jersey")

    @task
    def plan(self):
        self.client.get("/plans")
