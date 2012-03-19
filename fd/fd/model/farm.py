
from meta import *
from datetime import datetime

class Farm(Base):
    __tablename__ = 'farm'
    id = Column(SAT.Integer, primary_key=True)
    name = Column(SAT.Unicode, nullable=False)
    nickname = Column(SAT.Unicode, nullable=False)
    created = Column(SAT.DateTime, default=datetime.now)
    geom = GA.GeometryColumn(GA.Polygon(2))
    
    def __init__(self, name, nickname, geom):
        self.name = name
        self.nickname = nickname
        self.geom = geom
        self.created = datetime.now()
        
class Block(Base):
    __tablename__ = 'block'
    id = Column(SAT.Integer, primary_key=True)
    farmid = Column(SAT.Integer, ForeignKey('farm.id'), nullable = False)
    name = Column(SAT.Unicode, nullable=False)    
    geom = GA.GeometryColumn(GA.Polygon(2))
    created = Column(SAT.DateTime, default=datetime.now)

    farm = relation('Farm', backref=backref('blocks', order_by=id ))

    def __init__(self, name, farm, geom):
        self.name = name
        self.geom = geom
        self.farm = farm
        self.created = datetime.now()

GA.GeometryDDL(Farm.__table__)
GA.GeometryDDL(Block.__table__) 





