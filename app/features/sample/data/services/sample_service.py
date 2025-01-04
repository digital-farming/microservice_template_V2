from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database.tables.sample_tables import SampleTable
from app.shared.db_utils.save_data import commit_and_refresh
from app.shared.logger.setup import app_logger


class SampleService:
    def __init__(self, db: Session):
        self.db = db

    def add_new(self, name: str):
        new_data = SampleTable()
        new_data.name = name

        try:
            self.db.add(new_data)
            return commit_and_refresh(db=self.db, obj=new_data)
        except Exception as e:
            app_logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
