
from meta import *
from datetime import datetime

class Polygon(Base):
    __tablename__ = 'polygon'
    id = Column(SAT.Integer, primary_key=True)
    name = Column(SAT.Unicode, nullable=False)
    value = Column(SAT.Float)
    created = Column(SAT.DateTime, default=datetime.now)
    geom = GA.GeometryColumn(GA.Polygon(2))
    
GA.GeometryDDL(Polygon.__table__)

