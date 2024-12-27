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

    def add_basic_add(self, pos):
        id = "basic_add"
        with dpg.node(label="Add", parent="node_editor", pos=pos) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_multiply(self, pos):
        id = "basic_multiply"
        with dpg.node(label="Multiply", parent="node_editor", pos=pos) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_blend(self, pos):  
        id = "basic_blend"
        with dpg.node(label="Blend", parent="node_editor", pos=pos) as node:
            with dpg.node_attribute(label="ImageA"):
                dpg.add_text("Image A")
            with dpg.node_attribute(label="ImageB"):
                dpg.add_text("Image B")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Output Image")
            self.nodes[node] = id

    def add_basic_converttograyscale(self, pos):
        id = "basic_converttograyscale"
        with dpg.node(label="Convert To Grayscale", parent="node_editor", pos=pos) as node:
            with dpg.node_attribute(label="Image"):
                dpg.add_text("Image")
            
            with dpg.node_attribute(label="OutputImage", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text("Grayscale Image")
            self.nodes[node] = id

    def add_basic_mapcolor(self, pos):
        pass

    def add_basic_channelsplit(self, pos):
        pass

    def add_basic_channeljoin(self, pos):
        pass

    def add_noise_perlin(self, pos):
        pass

    def add_noise_simplex(self, pos):
        pass

    def add_noise_voronoi(self, pos):
        pass

    def add_noise_worley(self, pos):
        pass

    def add_filter_blur(self, pos):
        pass

    def add_filter_sharpen(self, pos):
        pass

    def add_filter_edgedetection(self, pos):
        pass

    def add_filter_emboss(self, pos):
        pass

    def add_filter_gaussianblur(self, pos):
        pass

    def add_transform_rotate(self, pos):
        pass

    def add_transform_scale(self, pos):
        pass

    def add_transform_translate(self, pos):
        pass

    def add_transform_flip(self, pos):
        pass

    def add_transform_mirror(self, pos):
        pass

    def add_random_seed(self, pos):
        pass

    def add_random_range(self, pos):
        pass

    def add_input_texture(self, pos):
        pass

    def add_input_color(self, pos):
        pass

    def add_output_preview(self, pos):
        pass

    def add_output_export(self, pos):
        pass