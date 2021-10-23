from typing import Sequence
from pydantic import BaseModel


class ProvisionBase(BaseModel):
    id: int

class ProvisionCreate(ProvisionBase):
    pass


class Provision(ProvisionBase):
    timestep: int
    demand: float
    alloc_ddc: float
    alloc_slice: float
    diff_ddc: float
    diff_slice: float
    bs: int
    cost_ddc: float
    slice_cost_ddc: float
    cost_slice: float
    slice_cost_slice: float

    class Config:
        orm_mode = True


class ProvisionResults(BaseModel):
    series: Sequence[Provision]


class BaseStationBase(BaseModel):
    pass


class BaseStationCreate(BaseStationBase):
    pass


class BaseStation(BaseStationBase):
    id: int
    slice_id: int

    class Config:
        orm_mode = True


class BaseStationResults(BaseModel):
    base_station: Sequence[BaseStation]


class TimestepBase(BaseModel):
    timestep: int


class TimestepCreate(TimestepBase):
    pass


class Timestep(TimestepBase):
    cost_mean_ddc_old: float
    cost_mean_slice_old: float
    cost_mean_ddc_new: float
    cost_mean_slice_new: float

    class Config:
        orm_mode = True


class TiemstepResults(BaseModel):
    time_series: Sequence[Timestep]