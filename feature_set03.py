import bpy

class SimpleOperator(bpy.types.Operator):
    bl_idname = "mesh.generate_surface"
    bl_label = "Generate Circular Paraboloid"
    
    def execute(self, context):
        create_surface_mesh(context)
        return {'FINISHED'}

class SimpleOperatorPanel(bpy.types.Panel):
    bl_label = "Circular Paraboloid Generator"
    bl_idname = "PT_SimpleOperatorPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Feature Set'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("mesh.generate_surface")

def create_surface_mesh(context):
    bpy.ops.mesh.primitive_z_function_surface(equation="(x**2 + y**2)")

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimpleOperatorPanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(SimpleOperatorPanel)

if __name__ == "__main__":
    register()
