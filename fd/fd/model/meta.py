
import os
from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relation, backref, column_property
from sqlalchemy import types as SAT
from sqlalchemy.sql.expression import text

metadata = Base.metadata

import geoalchemy as GA

from geodb.util import sys_call

SessionFactory = None

def configure(settings, echo=False):
    """ Pass this a settings that you might find in a pyramid app 
    to set up the engine and call connect """
    engine = engine_from_config(settings, 'sqlalchemy.', echo=echo)
    connect(engine=engine)
     
def connect(address=None, engine=None, echo=False ):
    """ Bind engine to metadata and setup the SessionFactory """
    if engine is None:
        if address is not None:
            engine = create_engine(address, echo=echo)
    
    if engine is not None:
        global SessionFactory
        SessionFactory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        metadata.bind = engine

def close():
    """ Closes everything """
    metadata.bind.dispose()
    metadata.bind = None
    if SessionFactory is not None:
        SessionFactory.close_all()

def drop_tables():
    """ This will likely need to be refactored regularly """
    metadata.drop_all()
    
def create_tables():
    """ """
    metadata.create_all()
    
def drop_db(db_name, 
            prefix="/private"):
    sys_call(["%s/bin/dropdb" % prefix, db_name])
    
def make_db(db_name,
            prefix="/private",
            pg_src="/private/src/postgis-1.5.3" ):

    sys_call(["%s/bin/createdb" % prefix, db_name])
    sys_call(["%s/bin/psql" % prefix, "-d", db_name, "-f", "%s/postgis/postgis.sql" % pg_src])
    sys_call(["%s/bin/psql" % prefix, "-d", db_name, "-f", "%s/spatial_ref_sys.sql" % pg_src])
    #sys_call(["%s/bin/psql" % prefix, "-d", db_name, "-f", "%s/doc/postgis_comments.sql" % pg_src])
    
    