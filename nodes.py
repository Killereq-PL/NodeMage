import dearpygui.dearpygui as dpg

class Nodes:
    def __init__(self):
        self.nodes = {}
    
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
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_multiply(self):
        id = "basic_multiply"
        with dpg.node(label="Multiply", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_blend(self):  
        id = "basic_blend"
        with dpg.node(label="Blend", parent="node_editor", pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]), user_data=id) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
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
        pass

    def add_basic_channelsplit(self):
        pass

    def add_basic_channeljoin(self):
        pass

    def add_noise_perlin(self):
        pass

    def add_noise_simplex(self):
        pass

    def add_noise_voronoi(self):
        pass

    def add_noise_worley(self):
        pass

    def add_filter_blur(self):
        pass

    def add_filter_sharpen(self):
        pass

    def add_filter_edgedetection(self):
        pass

    def add_filter_emboss(self):
        pass

    def add_filter_gaussianblur(self):
        pass

    def add_transform_rotate(self):
        pass

    def add_transform_scale(self):
        pass

    def add_transform_translate(self):
        pass

    def add_transform_flip(self):
        pass

    def add_transform_mirror(self):
        pass

    def add_random_seed(self):
        pass

    def add_random_range(self):
        pass

    def add_input_texture(self):
        pass

    def add_input_color(self):
        pass

    def add_output_preview(self):
        pass

    def add_output_export(self):
        pass