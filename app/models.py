import sqlalchemy as sa

from datetime import datetime
from sqlalchemy.orm import relationship
from app.db import Base


class Item(Base):
    __tablename__ = 'items'
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String)
    price = sa.Column(sa.Numeric(12, 2))

