from fastapi import FastAPI
from user.interface.controllers.user_controller import router as user_routers
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from containers import Container
import uvicorn

app = FastAPI()
app.include_router(user_routers)
app.container = Container()

@app.exception_handler(RequestValidationError) # 핸들러 등록
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",reload=True)