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

#------------------------------------------------------------
# Parse the scene and set up our data structures.
#------------------------------------------------------------
scene = importlib.import_module( sys.argv[1] )
points = {}
for point in scene.points:
    if point in points: die( f'{point} listed twice in points' )
    points[point] = { 'desc': scene.points[point], 'dists': [] }}

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
