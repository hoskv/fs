
from meta import *
from datetime import datetime

class Point(Base):
    __tablename__ = 'point'
    id = Column(SAT.Integer, primary_key=True)
    name = Column(SAT.Unicode, nullable=False)
    value = Column(SAT.Float)
    created = Column(SAT.DateTime, default=datetime.now)
    geom = GA.GeometryColumn(GA.Point(2))
    
GA.GeometryDDL(Point.__table__)

