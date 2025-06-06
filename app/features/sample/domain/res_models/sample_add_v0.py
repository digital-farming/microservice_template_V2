from pydantic import (
    BaseModel,
    ConfigDict,
)


class SampleAddV0ResModel(BaseModel):
    id: int
    name: str
    status: str = "success"
    # sample response
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "sample name",
                "status": "success"
            }
        }
    )
