from pydantic import BaseModel, ConfigDict, TypeAdapter


class Repo(BaseModel):
    name: str
    full_name: str
    default_branch: str

    model_config = ConfigDict(extra="allow")


Repos = TypeAdapter(list[Repo])
