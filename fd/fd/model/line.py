
from meta import *
from datetime import datetime

class Line(Base):
    __tablename__ = 'line'
    id = Column(SAT.Integer, primary_key=True)
    name = Column(SAT.Unicode, nullable=False)
    value = Column(SAT.Float)
    created = Column(SAT.DateTime, default=datetime.now)
    geom = GA.GeometryColumn(GA.LineString(2))
    
GA.GeometryDDL(Line.__table__)

