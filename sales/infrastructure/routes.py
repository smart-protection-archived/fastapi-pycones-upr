from fastapi import APIRouter

from sales.infrastructure.endpoints.sale import create_sale

router = APIRouter()

router.add_api_route(path='/sale/', endpoint=create_sale, methods=['POST'], status_code=204)
