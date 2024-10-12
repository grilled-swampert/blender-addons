bl_info = {
    "name": "Feature Set 02",
    "author": "Swapnil Ranadive",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "category": "3D View",
}

import bpy
import bgl
import blf
import math

class SineWavePanel(bpy.types.Panel):
    bl_label = "Feature Set 02"
    bl_idname = "PT_SineWavePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Feature Set'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.prop(scene, "sine_wave_amplitude", text="Amplitude")
        
        row = layout.row()
        row.prop(scene, "sine_wave_frequency", text="Frequency")
    
        row = layout.row()
        row.prop(scene, "sine_wave_points", text="Number of Points")
        
        row = layout.row()
        row.operator("object.generate_wave", text="Generate Sine Wave")

class GenerateSineWave(bpy.types.Operator):
    bl_idname = "object.generate_wave"
    bl_label = "Generate Sine Wave"
    
    def execute(self, context):
        amplitude = context.scene.sine_wave_amplitude
        frequency = context.scene.sine_wave_frequency
        num_points = context.scene.sine_wave_points
        
        vertices = []
        for i in range(num_points):
            x = i / (num_points - 1)
            y = 0
            z = amplitude * math.sin(2 * math.pi * frequency * x)
            vertices.append((x, y, z))
        
        mesh = bpy.data.meshes.new(name="SineWaveMesh")
        mesh.from_pydata(vertices, [], [])
        mesh.update()

        if "SineWaveMesh" in bpy.data.objects:
            bpy.data.objects.remove(bpy.data.objects["SineWaveMesh"], do_unlink=True)

        sine_wave_obj = bpy.data.objects.new("SineWaveMesh", mesh)
        bpy.context.collection.objects.link(sine_wave_obj)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SineWavePanel)
    bpy.utils.register_class(GenerateSineWave)
    bpy.types.Scene.sine_wave_amplitude = bpy.props.FloatProperty(
        name="Amplitude",
        default=1.0
    )
    bpy.types.Scene.sine_wave_frequency = bpy.props.FloatProperty(
        name="Frequency",
        default=1.0
    )
    bpy.types.Scene.sine_wave_points = bpy.props.IntProperty(
        name="Number of Points",
        default=100
    )


def unregister():
    bpy.utils.unregister_class(SineWavePanel)
    bpy.utils.register_class(GenerateSineWave)
    del bpy.types.Scene.sine_wave_amplitude
    del bpy.types.Scene.sine_wave_frequency
    del bpy.types.Scene.sine_wave_points

if __name__ == "__main__":
    register()
