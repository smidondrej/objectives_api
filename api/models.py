from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from .database import Base


class BaseStation(Base):
    __tablename__ = "bs"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    slice_id = Column(Integer, index=True)

    provision = relationship("Provision", back_populates="bs_")


class Timestep(Base):
    __tablename__ = "timesteps"

    timestep = Column(Integer, primary_key=True, index=True)
    cost_mean_ddc_old = Column(Float, index=True)
    cost_mean_slice_old = Column(Float, index=True)
    cost_mean_ddc_new = Column(Float, index=True)
    cost_mean_slice_new = Column(Float, index=True)

    provision = relationship("Provision", back_populates="timestep_")


class Provision(Base):
    __tablename__ = "provision"

    timestep = Column(Integer, ForeignKey("timesteps.timestep"))
    demand = Column(Float, index=True)
    alloc_ddc = Column(Float, index=True)
    alloc_slice = Column(Float, index=True)
    diff_ddc = Column(Float, index=True)
    diff_slice = Column(Float, index=True)
    bs = Column(Integer, ForeignKey("bs.id"))
    cost_ddc = Column(Float, index=True)
    slice_cost_ddc = Column(Float, index=True)
    cost_slice = Column(Float, index=True)
    slice_cost_slice = Column(Float, index=True)
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    bs_ = relationship("BaseStation", back_populates="provision")
    timestep_ = relationship("Timestep", back_populates="provision")