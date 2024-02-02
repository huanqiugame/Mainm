from manim import *

class Updaters(Scene):
    def construct(self):
        # 定义坐标系单位长度标记
        x_lables = {x for x in range(-8, 8, 1)}
        y_lables = {y for y in range(-9, 18, 3)}
        # 定义坐标系
        ax = Axes(
            x_range = (-8, 8, 1),
            y_range = (-9, 18, 1),
            x_length = config.frame_width - 0.5,
            y_length = config.frame_height - 0.5,
        ).add_coordinates(x_lables, y_lables)
        origin_point = Dot(ax.c2p(0, 0), color=WHITE)
        origin_point_label = Tex("O").next_to(origin_point, 0.25*DL)
        self.play(Write(ax), run_time=2)
        self.play(Write(origin_point),DrawBorderThenFill(origin_point_label), run_time=1)
        
        # 二次函数图象
        arc1 = ax.plot(lambda x: (x+3)**2, color=GREEN)
        arc2 = ax.plot(lambda x: (x+3)**2, x_range=[-3,1], color=YELLOW_A)
        self.play(Write(arc1), run_time=2)
        
        # 点A
        p1 = Dot(ax.c2p(-3, 0),color=YELLOW)
        p1_label = Tex("A").next_to(p1, 0.5*DOWN)
        p1_label.add_updater(
            lambda mobject: mobject.next_to(p1, 0.5*LEFT),
        )
        p1.save_state()
        self.play(Write(p1), run_time=0.5)
        self.play(Write(p1_label), run_time=0.5)
        
        # 线段OA
        oa = Line((p1.get_center()), (origin_point.get_center()))
        self.play(Write(oa))
        oa.add_updater(
            lambda mobject: mobject.put_start_and_end_on(p1.get_center(), origin_point.get_center())
        )
        # oa_label = Tex("OA=" + str(oa.get_length())).next_to(oa, RIGHT)
        # self.play(Write(oa_label))
        # oa_label.add_updater(
        #     lambda mobject: mobject.next_to(oa, RIGHT)
        # )
        l2 = VMobject()
        self.add(l2)
        l2.add_updater(lambda x: x.become(Line(ax.c2p(-3,0), p1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(p1, arc2), run_time=3)
        self.play(Restore(p1))
        # self.play(p1.animate.move_to(ax.c2p(1, 16)))
