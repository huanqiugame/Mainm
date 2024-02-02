from manim import *

class DifferentArcs(Scene):
    def construct(self):
        ## Define the unit length mark of the coordinate system / 定义坐标系单位长度标记
        x_lables = {x for x in range(-8, 8, 1)}
        y_lables = {y for y in range(-9, 18, 3)}
        # Define the coordinate system / 定义坐标系
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
        
        # arc = ax.plot(lambda x: -5*x**2+5, color=RED)
        # self.play(Write(arc))
        
        ## Change numbers in range() to change the max, min and step value
        ## 更改 range() 中的数字以更改最大值、最小值和步长值
        ## Since the range() only support int input, we must divide the range() input by 10^x to pass the proper value
        ## 由于 range() 仅支持整型输入，必须将 range() 输入除以 10^x 才能传递正确的值
        ## Change your value carefully, for it could easily takes you much longer to render
        ## 小心地更改输入值，因为它很容易花费您更长的时间来渲染
        ## Just for showing purpose, please use Transform Animation instead of Directly Change in order to get smoother animations and less system resource usage
        ## 只是为了显示目的，使用 Transform Animtion 而不是 Directly Change ，以获得更流畅的动画和更少的系统资源使用
        ## Which also allows you to use the least samples to render a similar quality Manimation
        ## 这也允许您使用最少的样本来渲染类似质量的 Manimation
        for m in range(-500, 501, 5):
            a = m / 100
            arc_var = ax.plot(lambda x: a*x**2+5, color=RED)
            if a == -5:
                arc_lega = arc_var.copy()
                self.play(Write(arc_lega))
                self.wait(0.05)
            else:
                ## Directly Change / 直接变换
                # self.remove(arc_lega)
                # arc_lega = arc_var.copy()
                # self.add(arc_lega)
                # self.wait(0.05)
                
                ## Use Transform Animation (Recommended) / 使用过渡动画（默认建议）
                self.play(ReplacementTransform(arc_lega, arc_var), run_time=0.05, rate_func=linear)
                
                ## Remove this if you want to render the path / 要渲染函数路径，移除此行
                # self.remove(arc_var)
                arc_lega = arc_var.copy()
