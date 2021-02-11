from unittest.case import TestCase

from fastapi.testclient import TestClient

from main import app
from sales.container import car_repository
from sales.domain.state import CarState


class TestCreateSale(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_create_sale(self):
        sale = {
            'frame_id': 123,
            'customer': 1,
            'prize': 23000.0
        }

        response = self.client.post('/sale/', json=sale)
        self.assertEqual(response.status_code, 204)

        car = car_repository.find_by_id(123)

        self.assertEqual(car.owner, 1)
        self.assertEqual(car.state, CarState.SOLD.value)
        self.assertEqual(car.prize, 23000.0)
