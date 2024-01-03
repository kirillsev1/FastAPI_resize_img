from pathlib import Path

import pytest
from httpx import AsyncClient
from starlette import status

from tests.conf import URLS

BASE_DIR = Path(__file__).parent
FIXTURES_PATH = BASE_DIR / 'fixtures'


@pytest.mark.parametrize(
    ('reservation_id', 'username', 'password', 'expected_status', 'fixtures'),
    [
        (
            '1',
            'test',
            'qwerty',
            status.HTTP_200_OK,
            [
                FIXTURES_PATH / 'sirius.user.json',
                FIXTURES_PATH / 'sirius.tour.json',
                FIXTURES_PATH / 'sirius.reservation.json',
            ],
        ),
    ],
)
@pytest.mark.asyncio()
@pytest.mark.usefixtures('_common_api_with_redis_fixture')
async def test_cache(
    client: AsyncClient,
    reservation_id: str,
    expected_status: int,
    access_token: str,
    db_session: None,
) -> None:
    response = await client.get(
        ''.join([URLS['crud']['reservation']['read'], reservation_id]),
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert 'reservation' in response.json()
    assert 'cached_reservation' not in response.json()
    assert response.status_code == expected_status

    response = await client.get(
        ''.join([URLS['crud']['reservation']['read'], reservation_id]),
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert 'review' not in response.json()
    assert 'cached_reservation' in response.json()
    assert response.status_code == expected_status