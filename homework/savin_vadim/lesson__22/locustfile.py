import random
from locust import HttpUser, task

url = '/object'


class API(HttpUser):
    new_object_list = []

    def on_start(self):
        response = self.client.post(url=url, json={"name": "Testov Test", "data": {"age": 51}},
                                    name="Create Test Data")
        new_object_id = response.json()['id']
        self.new_object_list.append(new_object_id)

    @task(2)
    def get_all_object(self):
        self.client.get(url=url)

    @task(3)
    def one_object(self):
        self.client.get(url=f'{url}/{random.choice(self.new_object_list)}')

    @task(2)
    def full_update(self):
        self.client.put(url=f'{url}/{random.choice(self.new_object_list)}',
                        json={"name": "Apdeit Apdeitovich", "data": {"age": 66}},
                        name="Full Update")

    @task(2)
    def partial_update(self):
        self.client.patch(url=f'{url}/{random.choice(self.new_object_list)}', json={"name": "Apdeit Chactichnov"},
                          name="Partial Update")

    def on_stop(self):
        print("Тестирование завершено, удаляю тестовые данные с помощью отдельной проги ")
