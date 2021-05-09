#!/usr/bin/env python3
#
# mappoints.py <scene> 
#
import sys
import importlib

def die( msg, prefix='ERROR: ' ):
    print( prefix + msg )
    sys.exit( 1 )

if len( sys.argv ) < 2: die( 'usage: mappoints.py <scene>', '' )

scene = importlib.import_module( sys.argv[1] )
print( scene.points )
print( scene.knowns )
print( scene.dists )
