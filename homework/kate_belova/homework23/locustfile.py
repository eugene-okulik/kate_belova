import logging
import random

from locust import HttpUser, between, task

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO
)


class ObjectAPIUser(HttpUser):
    host = 'http://objapi.course.qa-practice.com'
    wait_time = between(1, 5)

    @task(5)
    def get_all_objects(self):
        response = self.client.get('/object')
        logging.info(f'GET /object → {response.status_code}')

    @task(2)
    def get_single_object(self):
        object_id = random.randint(1, 200)
        response = self.client.get(f'/object/{object_id}')
        logging.info(f'GET /object/{object_id} → {response.status_code}')

    @task(1)
    def create_and_manage_object(self):
        payload = {
            'name': f'Test object {random.randint(1, 999)}',
            'data': {
                'color': random.choice(['red', 'green', 'blue', 'pink']),
                'size': random.choice(['small', 'medium', 'large']),
            },
        }
        response = self.client.post('/object', json=payload)

        if response.status_code == 200:
            obj = response.json()
            obj_id = obj.get('id')
            logging.info(f'✅ CREATED object {obj_id}')
            if obj_id:
                self.update_object(obj_id)
                self.partial_update_object(obj_id)
                self.delete_object(obj_id)
        else:
            logging.warning(
                f'❌ Failed to create object: {response.status_code}'
            )

    def update_object(self, obj_id):
        payload = {
            'name': f'Updated object {obj_id}',
            'data': {'color': 'black', 'size': 'huge'},
        }
        response = self.client.put(f'/object/{obj_id}', json=payload)
        logging.info(f'PUT /object/{obj_id} → {response.status_code}')

    def partial_update_object(self, obj_id):
        payload = {'data': {'color': random.choice(['yellow', 'white'])}}
        response = self.client.patch(f'/object/{obj_id}', json=payload)
        logging.info(f'PATCH /object/{obj_id} → {response.status_code}')

    def delete_object(self, obj_id):
        response = self.client.delete(f'/object/{obj_id}')
        if response.status_code == 200:
            logging.info(f'🗑️  DELETED object {obj_id}')
        else:
            logging.warning(
                f'❌ Failed to delete {obj_id}: {response.status_code}'
            )
