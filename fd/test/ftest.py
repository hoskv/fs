
# Farm Test

import sys 
import geodb
from fd import model

import random
from datetime import datetime
from time import sleep

from geoalchemy import WKTSpatialElement
from geojson import dumps


def ftest(dbhost, dbuserpass ):

    # Make a new db --------------------------------
    
    name = "demo%s" % random.randint(100,1000)

    print "\nMaking demo db '%s' ..." % name
    model.meta.make_db(name)

    print "\nInitiating"
    model.meta.connect("postgresql://%s@%s/%s" % (dbuserpass,dbhost,name))

    print "\nCreating tables"
    model.meta.create_tables()

    print "\nGetting a session"
    session = model.meta.SessionFactory()

    # Start the farm -------------------------------
    
    farm = model.Farm( name="Test Farm",
                       nickname="tester",
                       geom = WKTSpatialElement( "POLYGON((-123.48378372096 44.677325990715, \
                                                           -123.43983840845 44.677325990715, \
                                                           -123.43983840845 44.659746023719, \
                                                           -123.48378372096 44.659746023719, \
                                                           -123.48378372096 44.677325990715 ))" ))
    session.add(farm)
    session.commit()
    
    # Add a block

    block = model.Block( name="Block 1", 
                         farm=farm, 
                         geom=WKTSpatialElement( "POLYGON((-123.46747589014 44.669131825792, \
							   -123.4644289007 44.670535750071, \
                                                           -123.46271228694 44.666903789197, \
                                                           -123.46781921289 44.667086918723, \
                                                           -123.46747589014 44.669131825792))" ))
    session.add(block)
    session.commit()

    
    
    # Next step - create rows with equal spacing inside this block
    """
    How to know the orientation?
    How to know/fix the non-parallel nature of the sides?  Option?  what's the fix?
    
    first, make more blocks with different init options.

    THis should be part of the block code - optional settings for width and length and
    settings for taking approximate geometry and massaging it to fit known (desired)
    dimensions
 
    One set of options could be based on a trapazoid with two opposite sides parallel

    """




    # Close all  -------------------------------

    print "\nClosing..."
    model.meta.close()

    # ReOpen

    print "\nInitiating"
    model.meta.connect("postgresql://%s@%s/%s" % (dbuserpass,dbhost,name))

    print "\nGetting a session"
    session = model.meta.SessionFactory()

    # Query

    f = session.query(model.Farm).filter_by(nickname="tester").first()
    b = f.blocks[0]
    p = b.geom.coords(session)

    print "Farm '%s' Block '%s' geom: %s" % ( f.name, b.name, p )
    #print block
    #print dir(block)
    #print str( block.geom )
    
    # Close all again 
    print "\nClosing..."
    model.meta.close()



 
    print "\nDropping db '%s' ..." % name
    model.meta.drop_db(name)
    



if __name__=="__main__":
   
    import os
    from optparse import OptionParser

    parser = OptionParser( "%prog [options]" )    
    parser.add_option('-H', '--host', action='store', default='localhost',
                          help="""Database host name""")
    parser.add_option('-u', '--user', action='store', default=os.getlogin(),
                          help="""Database user name""")
    parser.add_option('-p', '--password', action ='store', default="",
                          help="""Database password""")
    
    opts, args = parser.parse_args()
    
    if opts.password != "": 
        up = "%s:%s" % (opts.user, opts.password)
    else:
        up = opts.user    

    ftest(opts.host, up) 



 
