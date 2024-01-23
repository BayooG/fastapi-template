from fastapi import FastAPI, Response, status
from service.endpoints.root import rootRouter
from fastapi_utilities import repeat_at, repeat_every

app = FastAPI()


app.include_router(rootRouter)


@app.on_event("startup")
@repeat_every(seconds=5)  # 1 hour
def remove_expired_tokens_task() -> None:
    print("running cron")


@app.on_event("startup")
@repeat_at(cron="0 0 * * *")
async def cron_at_midnight() -> None:
    pass
