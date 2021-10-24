from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

api_router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.get("/bs", status_code=200, response_model=schemas.BaseStationResults)
def read_bs(db: Session = Depends(get_db)):
    db_bs = crud.get_bs(db)
    if db_bs is None:
        raise HTTPException(status_code=404, detail="Base station not found")
    return {"base_station": list(db_bs)}


@api_router.get("/bs/{bs_id}", status_code=200, response_model=schemas.BaseStation)
def read_bs(bs_id: int, db: Session = Depends(get_db)):
    db_bs = crud.get_bs(db, bs_id=bs_id)
    if db_bs is None:
        raise HTTPException(status_code=404, detail="Base station not found")
    return db_bs


@api_router.get("/slice/{slice_id}", status_code=200, response_model=schemas.BaseStationResults)
def search_recipes(slice_id: int, db: Session = Depends(get_db)) -> dict:
    db_slice = crud.get_slice(db, slice_id=slice_id)
    if db_slice is None:
        raise HTTPException(status_code=404, detail="Slice not found")
    return {"base_station": list(db_slice)}


@app.get("/timesteps", status_code=200, response_model=schemas.TiemstepResults)
def read_timesteps(db: Session = Depends(get_db)):
    db_timesteps = crud.get_timesteps(db)
    if db_timesteps is None:
        raise HTTPException(status_code=404, detail="Timesteps not found")
    return {"time_series": list(db_timesteps)}


@app.get("/timesteps/time={time}", status_code=200, response_model=schemas.TiemstepResults)
def read_timesteps(time: int, db: Session = Depends(get_db)):
    db_timesteps = crud.get_timesteps(db, time=time)
    if db_timesteps is None:
        raise HTTPException(status_code=404, detail="Timesteps not found")
    return {"time_series": list(db_timesteps)}


@app.get("/timesteps/time={time}/window={window}", status_code=200, response_model=schemas.TiemstepResults)
def read_timesteps(time: int, window: int, db: Session = Depends(get_db)):
    db_timesteps = crud.get_timesteps(db, time=time, window=window)
    if db_timesteps is None:
        raise HTTPException(status_code=404, detail="Timesteps not found")
    return {"time_series": list(db_timesteps)}


@app.get("/provision/{bs_id}", status_code=200, response_model=schemas.ProvisionResults)
def read_provision(bs_id: int, db: Session = Depends(get_db)):
    db_provision = crud.get_bs_provision(db, bs_id=bs_id)
    if db_provision is None:
        raise HTTPException(status_code=404, detail="Provision not found")
    return {"series": list(db_provision)}

@app.get("/provision/{bs_id}/time={time}", status_code=200, response_model=schemas.ProvisionResults)
def read_provision(bs_id: int, time: int, db: Session = Depends(get_db)):
    db_provision = crud.get_bs_provision(db, bs_id=bs_id, time=time)
    if db_provision is None:
        raise HTTPException(status_code=404, detail="Provision not found")
    return {"series": list(db_provision)}


@app.get("/provision/{bs_id}/time={time}/window={window}", status_code=200, response_model=schemas.ProvisionResults)
def read_provision(bs_id: int, time: int, window: int, db: Session = Depends(get_db)):
    db_provision = crud.get_bs_provision(db, bs_id=bs_id, time=time, window=window)
    if db_provision is None:
        raise HTTPException(status_code=404, detail="Provision not found")
    return {"series": list(db_provision)}


app.include_router(api_router)
