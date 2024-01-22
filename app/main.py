from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/")
def read_root():
    return Response("Hello World!", status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
