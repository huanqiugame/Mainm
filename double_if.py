from manim import *

class double_if(Scene):
    def construct(self):
        x_labels = {x for x in range(-10, 10, 1)}
        ax = Axes(
            x_range=[-10, 10],
            y_range=[-6, 6],
            x_length=config.frame_width-0.5,
            y_length=config.frame_height-0.5
        ).add_coordinates(x_labels)
        
        arc_expression = lambda x: 0.5*(x-x_of_arc_center_line)**2-5
        x_of_arc_center_line = -1
        
        def get_y_from_x(x):
            return 0.5*(x-x_of_arc_center_line)**2-5
        def get_vertical_line_by_x(x, color):
            return VGroup(ax.get_vertical_line(ax.c2p(x, 0)+(0,5,0), color=color), ax.get_vertical_line(ax.c2p(x, 0)+(0,-5,0), color=color))
        def get_vertical_line_by_point(point, color):
            return VGroup(ax.get_vertical_line(point+(0,5,0), color=color), ax.get_vertical_line(point+(0,-5,0), color=color))
        
        
        arc = ax.plot(arc_expression, color=RED)
        # arc_center_line = get_vertical_line_by_x(x_of_arc_center_line, color=RED)
        # arc_entire = VGroup(arc, arc_center_line)
        center_line = Line(ax.c2p(1, 8), ax.c2p(1, -8), color=YELLOW)
        
        #
        # self.play(Write(ax))
        # self.wait()
        # self.play(Write(arc), FadeIn(arc_center_line), run_time=2)
        # self.play(FadeIn(center_line))
        #
        # self.add(ax, arc, arc_center_line, center_line)
        self.add(ax, arc, center_line)
        
        p1 = Dot(ax.c2p(-3, get_y_from_x(-3)), color=YELLOW)
        p2 = Dot(ax.c2p(1.5, get_y_from_x(1.5)), color=YELLOW)
        p_center = (p1.get_x() + p2.get_x())/2
        p_center_line = get_vertical_line_by_point(p_center, color=GREEN)
        
        #
        # self.play(Create(p1))
        # self.play(Create(p2),FadeIn(p_center_line))
        #
        self.add(p1, p2, p_center_line)
        
        def update_p_center_line(p_center_line, p1, p2):
            p_center_line.become(get_vertical_line_by_point((p1.get_x() + p2.get_x())/2, color=GREEN))
        
        p1.add_updater(lambda m, dt: update_p_center_line(p_center_line, p1, p2))
        
        
        #
        # self.wait()
        #