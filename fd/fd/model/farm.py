
from meta import *
from datetime import datetime

class Farm(Base):
    __tablename__ = 'farm'
    id = Column(SAT.Integer, primary_key=True)
    name = Column(SAT.Unicode, nullable=False)
    nickname = Column(SAT.Unicode, nullable=False)
    created = Column(SAT.DateTime, default=datetime.now)
    geom_extent = GA.GeometryColumn(GA.Polygon(2))
    
    def __init__(self, name, nickname, geom_extent):
        self.name = name
        self.nickname = nickname
        self.geom_extent = geom_extent
        self.created = datetime.now()
        

GA.GeometryDDL(Farm.__table__)

