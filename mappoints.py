#!/usr/bin/env python3
#
# mappoints.py <scene> 
#
import sys
import importlib
from math import sqrt

def die( msg, prefix='ERROR: ' ):
    print( prefix + msg )
    sys.exit( 1 )

if len( sys.argv ) < 2: die( 'usage: mappoints.py <scene>', '' )

#------------------------------------------------------------
# Parse the scene and set up our data structures.
#------------------------------------------------------------
scene = importlib.import_module( sys.argv[1] )
points = {}
for point in scene.points:
    if point in points: die( f'{point} listed twice in points' )
    points[point] = { 'desc': scene.points[point], 'dists': [] }

for point in scenes.knowns:
    if not point in points: die( f'{point} is in knowns but not in points' )
    if 'xy' in points[point]: die( f'{point} already has an xy assigned' )
    points[point]['xy'] = scenes.known[point]

for dist in scenes.dist:
    p1 = dist[0]
    p2 = dist[1]
    d  = dist[2]
    if p1 not in points: die( f'{p1} is in dists but not in points' )
    if p2 not in points: die( f'{p2} is in dists but not in points' )
    points[p1]['dists'].append( [p2, d] )
    points[p2]['dists'].append( [p1, d] )

# see: https://planetcalc.com/8098/
# set need_higher_y=True if you want the point that has the higher value of y
#
def circles_intersection( p1, p2, r1, r2, need_higher_y=True ):
    d = sqrt( r1*r1 + r2*r2 )
    if d > (r1+r2): return None
    if d < abs(r1+r2): return None
    a = (r1*r1 - r2*r2 + d*d) / (2.0*d)
    h = sqrt( r1*r1 - a*a )
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p1[0] + a/d*(x2-x1)
    y3 = p1[1] + a/d*(y2-y1)
    x4_0 = x3 + h/d*(y2-y1)
    y4_0 = y3 - h/d*(x2-x1)
    x4_1 = x3 - h/d*(y2-y1)
    y4_1 = y3 + h/d*(x2-x1)
    return [x4_0, y4_0] if need_higher_y == (y4_0 >= y4_1) else [x4_1, y4_1]
    
#------------------------------------------------------------
# Try to map a point that has distances to at least two other points
# that have been mapped. Keep doing this until we can map no more points
# for whatever reason.
#------------------------------------------------------------
can_map = True
while can_map:
    can_map = False
    p = None
    for point in points:
        other_cnt = 0
        if not 'xy' in points: 
            for dist in points[point]['dists']:

#------------------------------------------------------------
# Print out final mappings and points that could not be mapped.
#------------------------------------------------------------
