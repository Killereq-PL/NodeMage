import dearpygui.dearpygui as dpg

class Nodes:
    def __init__(self):
        self.nodes = {}
    
    def create_attribute(self, id:str, name:str, type:str, output: bool = False, **kwargs):
        atrribute_type = dpg.mvNode_Attr_Output if output else dpg.mvNode_Attr_Input
        with dpg.node_attribute(label=id, attribute_type=atrribute_type) as a:
            if type == "image":
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output})
                dpg.add_text(name)
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(dpg.last_item(), color=kwargs["color"])
                if kwargs.get("value", -1) != -1:
                    ud = dpg.get_item_user_data(dpg.last_item())
                    ud["value"] = kwargs["value"]
                    dpg.set_item_user_data(dpg.last_item(), ud)
            if type == "float":
                dpg.set_item_user_data(a, {"id": id, "type": type, "name": name, "output": output})
                max_value = kwargs.get("max_value", 1.0)
                min_value = kwargs.get("min_value", 0.0)
                max_clamped = kwargs.get("max_clamped", True)
                min_clamped = kwargs.get("min_clamped", True)
                dpg.add_input_float(width=100, label=name, max_value=max_value, min_value=min_value, max_clamped=max_clamped, min_clamped=min_clamped)
                if kwargs.get("color", -1) != -1:
                    dpg.configure_item(dpg.last_item(), color=kwargs["color"])
                if kwargs.get("value", -1) != -1:
                    ud = dpg.get_item_user_data(dpg.last_item())
                    ud["value"] = kwargs["value"]
                    dpg.set_item_user_data(dpg.last_item(), ud)
    
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
            with dpg.node_attribute(label="Image"):
                dpg.add_text("Image")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Grayscale Image")
            self.nodes[node] = id

    def add_basic_mapcolor(self):
        id = "basic_mapcolor"
        with dpg.node(label="Map Color", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="Image"):
                dpg.add_text("Image")
            with dpg.node_attribute(label="RGB"):
                dpg.add_color_edit(width=200, label="Color", default_value=(255, 255, 255, 255))
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_channelsplit(self):
        id = "basic_channelsplit"
        with dpg.node(label="Channel Split", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="Image"):
                dpg.add_text("Image")
            
            with dpg.node_attribute(label="R", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Red")
            with dpg.node_attribute(label="G", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Green")
            with dpg.node_attribute(label="B", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Blue")
            with dpg.node_attribute(label="A", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Alpha")
            self.nodes[node] = id

    def add_basic_channeljoin(self):
        id = "basic_channeljoin"
        with dpg.node(label="Channel Join", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="R"):
                dpg.add_text("Red")
            with dpg.node_attribute(label="G"):
                dpg.add_text("Green")
            with dpg.node_attribute(label="B"):
                dpg.add_text("Blue")
            with dpg.node_attribute(label="A"):
                dpg.add_text("Alpha")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_noise_perlin(self):
        id = "noise_perlin"
        with dpg.node(label="Perlin Noise", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="Seed"):
                dpg.add_input_float(width=100, label="Factor", step=1, step_fast=10)
            with dpg.node_attribute(label="Factor"):
                dpg.add_input_float(width=100, label="Factor", max_value=1.0, min_value=0.0, max_clamped=True, min_clamped=True)
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
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