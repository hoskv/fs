
# geodb test

#PREFIX="/private"

#How to get prefix and the necessary parts of the
#db adress from an ini file to use for this - have
#????

import sys
import geodb
from geodb import model

import random
from datetime import datetime
#model.init(address='postgresql://adamryan@localhost/fs')

from geoalchemy import WKTSpatialElement
from geojson import dumps

def geom_test(dbhost, dbuserpass ):
    
    name = "demo%s" % random.randint(100,1000)
    
    # Make a new db
    print "\nMaking demo db '%s' ..." % name
    model.meta.make_db(name)
    
    print "\nInitiating"
    model.meta.connect("postgresql://adamryan@localhost/%s" % name)
    
    print "\nCreating tables"
    model.meta.create_tables()
    
    print "\nGetting a session"
    session = model.meta.SessionFactory()
    
    print "\nAdding Point"
    point = model.Point()
    point.name = u"Foo"
    point.value = 13.78
    point.created = datetime.now()
    point.geom = WKTSpatialElement("POINT(-81.40 38.08)")
    session.add(point)
    session.commit()

    print "\nAdding a Line"
    line = model.Line()
    line.name = u"Foo"
    line.value = 13.78
    line.created = datetime.now()
    line.geom = WKTSpatialElement( "LINESTRING(-80.3 38.2, -81.03 38.04, -81.2 37.89)")
    session.add(line)
    session.commit()    

    print "\nAdding a Polygon"
    poly = model.Polygon()
    poly.name = u"Foo"
    poly.value = 13.78
    poly.created = datetime.now()
    poly.geom = WKTSpatialElement( "POLYGON((-79.8 38.5, -80.03 38.2, -80.02 37.89, -79.92 37.75, -79.8 38.5))")
    session.add(poly)
    session.commit()  
    
    print "\nprint Point in different formats"
    point = session.query(model.Point).first()
    print point
    print session.scalar(point.geom.wkt)
    print session.scalar(point.geom.kml)
    print session.scalar(point.geom.gml)    
    print point.geom.coords(session)
    
    
    #print point.geom
    #print session.scalar(point.geom.wkt)
    #print dumps(point)
    #print point.geom.wkt
    
    print "\nClosing..."
    model.meta.close()
    
    print "\nDropping db '%s' ..." % name
    model.meta.drop_db(name)
    
    #geodb.create_db()


if __name__=="__main__":
    
     args = sys.argv
     print args
     if not len(args) == 3:
     	print "Usage: geom_test.py dbhost dbuserpass"
     else:
     	geom_test(args[1], args[2])
