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
    return Response(title="service is up and running", status="OK")
