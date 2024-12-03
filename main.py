import os
import uvicorn
from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/healthcheck")
def healthcheck():
    return 'Health - OK'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv('APP_PORT')))