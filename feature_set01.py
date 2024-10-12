bl_info = {
    "name": "Feature Set 01",
    "author": "Swapnil Ranadive",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "category": "3D View",
}

import bpy
import math

def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

class NumberCubesPanel(bpy.types.Panel):
    bl_label = "Feature Set 01"
    bl_idname = "PT_NumberCubesPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Feature Set'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.prop(scene, "composite_number")

        row = layout.row()
        row.operator("object.generate_cubes", text="Generate Cubes")

        row = layout.row()
        row.operator("object.delete_selected_cubes", text="Delete Selected Cubes")
        
        row = layout.row()
        row.operator("object.clear_all_cubes", text="Clear All Cubes")

class GenerateCubesOperator(bpy.types.Operator):
    bl_idname = "object.generate_cubes"
    bl_label = "Generate Cubes"

    def execute(self, context):
        scene = context.scene

        if check_prime(scene.composite_number):
            self.report({'INFO'}, "N must be composite.")
            return {'CANCELLED'}

        cubes = []
        composite_number = scene.composite_number

        m = int(math.sqrt(composite_number))
        while composite_number % m != 0:
            m -= 1
        n = composite_number // m

        x_offset = 2

        for i in range(m):
            row = []
            for j in range(n):
                bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                               location=(i * x_offset, j * x_offset, 0))
                cube = bpy.context.active_object
                row.append(cube)
            cubes.append(row)

        return {'FINISHED'}


class DeleteSelectedCubesOperator(bpy.types.Operator):
    bl_idname = "object.delete_selected_cubes"
    bl_label = "Delete Selected Cubes"

    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        for obj in selected_objects:
            obj.select_set(True)
            bpy.ops.object.delete()

        return {'FINISHED'}

class ClearAllCubesOperator(bpy.types.Operator):
    bl_idname = "object.clear_all_cubes"
    bl_label = "Clear All Cubes"

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(NumberCubesPanel)
    bpy.utils.register_class(GenerateCubesOperator)
    bpy.utils.register_class(DeleteSelectedCubesOperator)
    bpy.utils.register_class(ClearAllCubesOperator)
    bpy.types.Scene.composite_number = bpy.props.IntProperty(
        name="Number",
        min=0,
        max=50,
        subtype='UNSIGNED',
    )

def unregister():
    bpy.utils.unregister_class(NumberCubesPanel)
    bpy.utils.unregister_class(GenerateCubesOperator)
    bpy.utils.unregister_class(DeleteSelectedCubesOperator)
    bpy.utils.unregister_class(DeleteSelectedCubesOperator)
    del bpy.types.Scene.composite_number

if __name__ == "__main__":
    register()
