from pydantic import BaseModel, ConfigDict, RootModel


class Repo(BaseModel):
    name: str
    full_name: str
    default_branch: str

    model_config = ConfigDict(extra="allow")


class Repos(RootModel[list[Repo]]):
    root: list[Repo]

    def __iter__(self):
        return iter(self.root)

    def __len__(self) -> int:
        return len(self.root)
