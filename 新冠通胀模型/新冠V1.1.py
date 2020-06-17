'''
V1 版本下的坐标间隔太密
V1_1 解决了上一版本的问题，同时让坐标轴横轴只占屏幕一半，为后面添加说明性文字作铺垫
'''

from manimlib.imports import *


class PlotFunctionsV1_1(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 55,
        "x_tick_frequency": 5,
        "x_labeled_nums": range(0, 56, 5),
        "x_axis_label": "$x$",

        "y_min": 0,
        "y_max": 55,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 56, 5),
        "y_axis_label": "$y$",
        "exclude_zero_label": True,

        "y_axis_height": 7,
        "x_axis_width": 7,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
    }

    def construct(self):
        self.setup_axes(animate=True)

        graph = self.get_graph(self.func, color=RED)
        graph_label = self.get_graph_label(graph, label="\\frac{x^2 - 4x + 5}{2}", x_val=8, direction=UP)

        self.play(ShowCreation(graph), ShowCreation(graph_label))
        self.wait(1)
        self.play(FadeOutAndShiftDown(graph_label))

        point = self.input_to_graph_point(8, graph)
        pline = self.get_vertical_line_to_graph(8, graph, color=YELLOW)
        ptext = TextMobject("(%f, %f)" % (8, self.func(8)))
        ptext.next_to(point, direction=LEFT)
        self.play(ShowCreation(pline), ShowCreation(ptext))
        self.wait(1)
        self.play(FadeOut(pline), FadeOut(ptext))

        area = self.get_area(graph, 3, 8)
        self.play(ShowCreation(area))
        self.wait(1)
        self.play(FadeOut(area))

        slop = self.get_secant_slope_group(5, graph, dx=1, dx_label="dx = 1", df_label="\\frac{dy}{dx}")
        self.play(ShowCreation(slop))
        self.wait(1)
        self.play(FadeOut(slop))

        deriv = self.get_derivative_graph(graph, color=BLUE)
        self.play(ShowCreation(deriv))
        self.wait(1)
        self.play(FadeOut(deriv))

    def func(self, x):
        return (x * x - 4 * x + 5) / 2






