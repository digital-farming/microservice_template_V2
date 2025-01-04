from fastapi import FastAPI

from app.app_setup import App
from app.shared.config.endpoints.details import APIEndpointDetail


# app
app = FastAPI(
    title=App.TITLE,
    description=App.DESCRIPTION,
    version=App.VERSION
)


# Root Route
@app.get(path=APIEndpointDetail.root.path,
         tags=APIEndpointDetail.root.tags,
         summary=APIEndpointDetail.root.summary,
         description=APIEndpointDetail.root.description,
         )
async def root():
    return {"message": "Hello World"}
