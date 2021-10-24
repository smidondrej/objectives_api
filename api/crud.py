from typing import Optional

from sqlalchemy.orm import Session

from . import models


def get_bs(db: Session, bs_id: Optional[int] = None) -> Optional[models.BaseStation]:
    if bs_id is None:
        return db.query(models.BaseStation).all()
    else:
        return db.query(models.BaseStation).filter(models.BaseStation.id == bs_id).first()

def get_bs_provision(db: Session, bs_id: int, time: Optional[int] = None, window: Optional[int] = None):
    if window is None and time is not None:
        return db.query(models.Provision).filter(models.Provision.bs == bs_id).filter(models.Provision.timestep >= time).all()
    elif window is not None and time is not None:
        return db.query(models.Provision).filter(models.Provision.bs == bs_id).filter(models.Provision.timestep >= time).filter(models.Provision.timestep < time + window).all()
    else:
        return db.query(models.Provision).filter(models.Provision.bs == bs_id).all()

def get_slice(db: Session, slice_id: int):
    return db.query(models.BaseStation).filter(models.BaseStation.slice_id == slice_id).all()

def get_timesteps(db: Session, time: Optional[int] = None, window: Optional[int] = None):
    if window is None and time is not None:
        return db.query(models.Timestep).offset(time).all()
    elif window is not None and time is not None:
        return db.query(models.Timestep).offset(time).limit(window).all()
    else:
        return db.query(models.Timestep).all()
