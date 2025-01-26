import dearpygui.dearpygui as dpg

class Nodes:
    def __init__(self):
        self.nodes = {}
    
    def create_attribute(self, id:str, name:str, type:str, output: bool = False, **kwargs):
        attribute_type = dpg.mvNode_Attr_Output if output else dpg.mvNode_Attr_Input
        with dpg.node_attribute(label=id, attribute_type=attribute_type) as a:
            if type == "image":
                dpg.configure_item(a, category="image") # color=(0, 195, 255, 255)
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output})
                dpg.add_text(name)
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(dpg.last_item(), color=kwargs["color"])
                if kwargs.get("value", -1) != -1:
                    ud = dpg.get_item_user_data(a)
                    ud["value"] = kwargs["value"]
                    dpg.set_item_user_data(a, ud)
            if type == "float":
                dpg.configure_item(a, category="float") # color=(0, 255, 47, 255)
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output, "value": kwargs.get("value", 0)})
                step = kwargs.get("step", 0.1)
                step_fast = kwargs.get("step_fast", 1.0)
                max_value = kwargs.get("max_value", 1.0)
                min_value = kwargs.get("min_value", 0.0)
                max_clamped = kwargs.get("max_clamped", True)
                min_clamped = kwargs.get("min_clamped", True)
                if output:
                    dpg.add_text(name)
                else:
                    dpg.add_input_float(width=100, label=name, max_value=max_value, min_value=min_value, max_clamped=max_clamped, min_clamped=min_clamped, step=step, step_fast=step_fast)
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(dpg.last_item(), color=kwargs["color"])
            if type == "color":
                dpg.configure_item(a, category="color") # color=(255, 224, 20, 255)
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output, "value": kwargs.get("value", (255, 255, 255, 255))})
                if output:
                    dpg.add_text(name)
                else:
                    dpg.add_color_edit(width=200, label=name, default_value=(255, 255, 255, 255))
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(a, color=kwargs["color"])
            if type == "integer":
                dpg.configure_item(a, category="integer") # color=(179, 255, 0, 255)
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output, "value": kwargs.get("value", 0)})
                step = kwargs.get("step", 1)
                step_fast = kwargs.get("step_fast", 10)
                max_value = kwargs.get("max_value", 255)
                min_value = kwargs.get("min_value", 0)
                max_clamped = kwargs.get("max_clamped", True)
                min_clamped = kwargs.get("min_clamped", True)
                if output:
                    dpg.add_text(name)
                else:
                    dpg.add_input_int(width=100, label=name, max_value=max_value, min_value=min_value, max_clamped=max_clamped, min_clamped=min_clamped, step=step, step_fast=step_fast)
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(dpg.last_item(), color=kwargs["color"])
    
    def get_all_nodes(self):
        return self.nodes.keys()
    
    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.pop(node)
            dpg.delete_item(node)

    def add_node(self, name):
        getattr(self, f'add_{name}')()

    def add_basic_add(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("ImageA", "Image A", "image")
            self.create_attribute("ImageB", "Image B", "image")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_basic_multiply(self):
        id = "basic_multiply"
        with dpg.node(label="Multiply", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("ImageA", "Image A", "image")
            self.create_attribute("ImageB", "Image B", "image")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_basic_blend(self):  
        id = "basic_blend"
        with dpg.node(label="Blend", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("ImageA", "Image A", "image")
            self.create_attribute("ImageB", "Image B", "image")
            self.create_attribute("Factor", "Factor", "float")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_basic_converttograyscale(self):
        id = "basic_converttograyscale"
        with dpg.node(label="Convert To Grayscale", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("Image", "Image", "image")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_basic_mapcolor(self):
        id = "basic_mapcolor"
        with dpg.node(label="Map Color", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("Image", "Image", "image")
            self.create_attribute("RGB", "Color", "color")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_basic_channelsplit(self):
        id = "basic_channelsplit"
        with dpg.node(label="Channel Split", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("Image", "Image", "image")
            # -- Output --
            self.create_attribute("R", "Red", "integer", output=True)
            self.create_attribute("G", "Green", "integer", output=True)
            self.create_attribute("B", "Blue", "integer", output=True)
            self.create_attribute("A", "Alpha", "integer", output=True)
            self.nodes[node] = id

    def add_basic_channeljoin(self):
        id = "basic_channeljoin"
        with dpg.node(label="Channel Join", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("R", "Red", "integer")
            self.create_attribute("G", "Green", "integer")
            self.create_attribute("B", "Blue", "integer")
            self.create_attribute("A", "Alpha", "integer")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id

    def add_noise_perlin(self):
        id = "noise_perlin"
        with dpg.node(label="Perlin Noise", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            self.create_attribute("Seed", "Seed", "integer", min_clamped=False, max_clamped=False, min_value=False, max_value=False)
            self.create_attribute("Factor", "Factor", "float")
            # -- Output --
            self.create_attribute("OutputImage", "Output Image", "image", output=True)
            self.nodes[node] = id
###### end of finished
    def add_noise_simplex(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_noise_voronoi(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_noise_worley(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_filter_blur(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_filter_sharpen(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_filter_edgedetection(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_filter_emboss(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_filter_gaussianblur(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_transform_rotate(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_transform_scale(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_transform_translate(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_transform_flip(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_transform_mirror(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_random_seed(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_random_range(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_input_texture(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_input_color(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_output_preview(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_output_export(self):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id