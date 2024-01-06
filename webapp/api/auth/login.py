from fastapi import Depends, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.auth.router import auth_router
from webapp.crud.user import get_user
from webapp.integrations.postgres import get_session
from webapp.schema.info.user import UserInfo, UserLoginResponse
from webapp.utils.auth.jwt import jwt_auth


@auth_router.post(
    '/login',
    response_model=UserLoginResponse,
)
async def login(
    body: UserInfo,
    session: AsyncSession = Depends(get_session),
) -> ORJSONResponse:
    user = await get_user(session, body)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return ORJSONResponse(
        {
            'access_token': jwt_auth.create_token(user.id),
        }
    )