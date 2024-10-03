from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict


class BaseModel(_BaseModel):
  model_config = ConfigDict(extra="forbid")
