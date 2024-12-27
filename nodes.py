import dearpygui.dearpygui as dpg

class Nodes:
    def __init__(self):
        pass

    def add_node(self, name):
        getattr(self, f'add_{name}')()

    def add_basic_add(self):
        with dpg.node(label="Add", parent="node_editor"):
            dpg.add_node_attribute(label="Image A")
            dpg.add_node_attribute(label="Image B")

            dpg.add_node_attribute(label="Output Image", attribute_type=dpg.mvNode_Attr_Output)

    def add_basic_multiply(self):
        pass

    def add_basic_screen(self):  
        pass

    def add_basic_converttograyscale(self):
        pass

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