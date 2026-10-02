bl_info = {
    "name": "Meu Add-on",
    "author": "Seu nome",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "category": "3D View",
}

import bpy

class MEUADDON_OT_hello(bpy.types.Operator):
    bl_idname = "meu_addon.hello"
    bl_label = "Dizer ola"

    def execute(self, context):
        self.report({'INFO'}, "Ola, Blender!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MEUADDON_OT_hello)

def unregister():
    bpy.utils.unregister_class(MEUADDON_OT_hello)

if __name__ == "__main__":
    register()
