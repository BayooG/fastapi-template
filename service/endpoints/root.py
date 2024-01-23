from fastapi import APIRouter, status, Response

rootRouter = APIRouter()


@rootRouter.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["Health Check"],
    summary="Performs health check",
    description="Performs health check and returns information about running service.",
)
def health_check():
    return Response(content="service is up and running", status_code=status.HTTP_200_OK)


# @rootRouter.lifespan("startup")
# @repeat_at(cron="0 0 * * *")
# async def daily_at_midnight() -> None:
#     print("--running cron--")
