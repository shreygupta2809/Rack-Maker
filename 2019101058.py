import bpy
from random import randrange
import random
import sys, os

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False, confirm=False)


def append_zero(num):
    return "." + str(num).zfill(3)


# RACK SHELVES
bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 1.0))
bpy.context.object.name = "Rack1"  # to change the name but it does not work
bpy.context.object.scale = (3, 10, 0.025)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 4.0))
bpy.context.object.name = "Rack2"  # to change the name but it does not work
bpy.context.object.scale = (3, 10, 0.025)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 7.0))
bpy.context.object.name = "Rack3"  # to change the name but it does not work
bpy.context.object.scale = (3, 10, 0.025)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 10.0))
bpy.context.object.name = "Rack4"  # to change the name but it does not work
bpy.context.object.scale = (3, 10, 0.025)

# RACK WALLS
bpy.ops.mesh.primitive_cube_add(location=(0.0, 10.0, 6))
bpy.context.object.name = "Wall1"  # to change the name but it does not work
bpy.context.object.scale = (3, 0.025, 6)

bpy.ops.mesh.primitive_cube_add(location=(0.0, -10.0, 6))
bpy.context.object.name = "Wall1"  # to change the name but it does not work
bpy.context.object.scale = (3, 0.025, 6)

# BOXES ON RACK
bpy.ops.mesh.primitive_cube_add(location=(0.0, 5.0, 2.0))
bpy.context.object.name = "Box1"  # to change the name but it does not work
bpy.context.object.scale = (1, 1, 1)

bpy.ops.mesh.primitive_cube_add(location=(0.0, -6.0, 2.4))
bpy.context.object.name = "Box2"  # to change the name but it does not work
bpy.context.object.scale = (1, 1, 1.4)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 8.0, 4.5))
bpy.context.object.name = "Box3"  # to change the name but it does not work
bpy.context.object.scale = (2, 1, 0.5)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 2.0, 5))
bpy.context.object.name = "Box4"  # to change the name but it does not work
bpy.context.object.scale = (1, 2, 1)

bpy.ops.mesh.primitive_cube_add(location=(0.0, -4.5, 5.3))
bpy.context.object.name = "Box5"  # to change the name but it does not work
bpy.context.object.scale = (1, 1.5, 1.3)

bpy.ops.mesh.primitive_cube_add(location=(0.0, -5.0, 8))
bpy.context.object.name = "Box6"  # to change the name but it does not work
bpy.context.object.scale = (1, 2, 1)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 5.0, 8))
bpy.context.object.name = "Box7"  # to change the name but it does not work
bpy.context.object.scale = (2, 1.5, 1)

bpy.ops.mesh.primitive_cube_add(location=(0.0, -6.0, 12))
bpy.context.object.name = "Box8"  # to change the name but it does not work
bpy.context.object.scale = (2, 2, 2)

bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 10.75))
bpy.context.object.name = "Box9"  # to change the name but it does not work
bpy.context.object.scale = (1, 3, 0.7)

bpy.ops.mesh.primitive_cube_add(location=(0.5, 7.0, 11))
bpy.context.object.name = "Box10"  # to change the name but it does not work
bpy.context.object.scale = (1, 2, 1)


dg = bpy.context.evaluated_depsgraph_get()
dg.update()