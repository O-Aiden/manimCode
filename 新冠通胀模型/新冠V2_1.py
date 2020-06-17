
'''
V1 版本下的坐标间隔太密
V1_1 解决了上一版本的问题，同时让坐标轴横轴只占屏幕一半，为后面添加说明性文字作铺垫
V1_2 添加了直线 (-x + 35)
V1_3 添加了直线 (-x + 50)和(-x + 70)
v1_4 更改直线 (-x + 50) 为 (-x + 60)，为直线限制了x值的最大和最小值
V1_5 添加了直线 (x + 3)
V1_6 更改横坐标为income，纵坐标为price（这里发现横纵坐标为中文时会报错）
V1_7 添加了直线 x=15
V1_8 测试了 self.wait(2)函数，坐标轴相关功能基本实现
V1_9 粗略实现了文字相关功能
V2_0 坐标和文字都基本实现
V2_1 对三个均衡点添加了标签，对图形动画顺序基本完成
'''

from manimlib.imports import *


class PlotFunctionsV2_1(GraphScene,Scene):





    CONFIG = {
        "x_min": 0,
        "x_max": 55,
        "x_tick_frequency": 5,
        "x_labeled_nums": range(0, 56, 5),
        "x_axis_label": "$income$",

        "y_min": 0,
        "y_max": 55,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 56, 5),
        "y_axis_label": "$price$",
        "exclude_zero_label": True,

        "y_axis_height": 7,
        "x_axis_width": 7,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
    }

    def construct(self):
        self.setup_axes(animate=True)

        # y=(-x + 35)
        graph = self.get_graph(self.func, color=RED, x_min=1, x_max=34)

        # y=(-x + 60)
        graph2 = self.get_graph(self.func2, color=RED, x_min=13.5, x_max=46.5)
        # y=(-x + 70)
        graph3 = self.get_graph(self.func3, color=RED, x_min=18.5, x_max=51.5)
        # y=(x + 3)
        graph4 = self.get_graph(self.func4, color=RED, x_min=10, x_max=50)
        # x=15
        graph5 = self.get_vertical_line_to_graph(15, graph3, color=YELLOW)
        graph_label1 = self.get_graph_label(graph3, label="(1)", x_val=33.5, direction=UP)
        graph_label2 = self.get_graph_label(graph, label="(2)", x_val=17, direction=UP)
        graph_label3 = self.get_graph_label(graph2, label="(3)", x_val=17, direction=UP)




        text = VGroup(
            Text("点(1)：正常经济下的市场均衡价格和收入", font='未署名的信'),# 1
            Text("(看成所对应的数量更好理解)", font='未署名的信'),# 2
            Text("点(2)：被疫情影响后，供给无弹性", font='未署名的信'),# 3
            Text("价格再怎么波动，但供给数量受到供应链", font='未署名的信'),# 4
            Text("断裂影响中短期不变，供给线由S1变到S2", font='未署名的信'),# 5
            Text("需求下滑(需求线由D1下滑到D2)", font='未署名的信'),# 6
            Text("新的市场均衡价格和数量为点(2)", font='未署名的信'),# 7
            Text("点(3)：政府部门入市干预，发布纾困方案，", font='未署名的信'),# 8
            Text("通过印钞增加需求，但由于供给仍跟不上，", font='未署名的信'),# 9
            Text("(供给者弹性受到伤害后更难调整)", font='未署名的信'),# 10
            Text("造成过多的货币追逐不足的商品的局面", font='未署名的信'),# 11
            Text("(价格狂飙，即点(3))", font='未署名的信'),# 12
        ).scale(0.5).set_color('#EEC591')

        ## 点（1）
        # y=(-x + 70)
        self.play(ShowCreation(graph3))
        # self.wait(2)

        # y=(x + 3)
        self.play(ShowCreation(graph4), ShowCreation(graph_label1))

        #self.coords_to_point(33.5, 36.5)
        # self.wait(2)
        text[0].to_corner(RIGHT + 5*UP)
        text[1].to_corner(RIGHT + 6*UP)
        self.play(Write(text[0]), run_time=2)
        self.play(Write(text[1]), run_time=2)


        [
            VGroup(
                text[0][0:2].set_color('#EEAEEE'),
                text[0][2:4].set_color('#5F9EA0'),
                text[0][5:7].set_color('#00FF00'),
                text[0][-10:-8].set_color('#00FF00'),
                text[0][-3:-1].set_color('#FF7F24'),
                text[0][8:8 + (5, 4)[i == 1]].set_color('#9B30FF'),
            ) for i in range(4)
        ]
        self.wait(2)
        self.remove(text[0])
        self.remove(text[1])
        self.remove(graph3)
        self.remove(graph4)
        self.remove(graph_label1)

        ## 点（2）
        # y=(-x + 35)
        self.play(ShowCreation(graph))
        # self.wait(2)

        # x=15
        self.play(ShowCreation(graph5), ShowCreation(graph_label2))
        self.wait(2)
        #self.play(FadeOutAndShiftDown(graph_label2))

        text[2].to_corner(RIGHT + 5*UP)
        text[3].to_corner(RIGHT + 6*UP)
        text[4].to_corner(RIGHT + 7*UP)
        text[5].to_corner(RIGHT + 8*UP)
        text[6].to_corner(RIGHT + 9*UP)

        self.play(Write(text[2]), run_time=2)
        self.play(Write(text[3]), run_time=2)
        self.play(Write(text[4]), run_time=2)
        self.play(Write(text[5]), run_time=2)
        self.play(Write(text[6]), run_time=2)
        self.wait(2)

        self.remove(text[2])
        self.remove(text[3])
        self.remove(text[4])
        self.remove(text[5])
        self.remove(text[6])
        self.remove(graph)
        self.remove(graph_label2)




        ## 点（3）
        # y=(-x + 60)
        self.play(ShowCreation(graph2), ShowCreation(graph_label3))
        # self.wait(2)


        text[7].to_corner(RIGHT + 5*UP)
        text[8].to_corner(RIGHT + 6*UP)
        text[9].to_corner(RIGHT + 7*UP)
        text[10].to_corner(RIGHT + 8*UP)
        text[11].to_corner(RIGHT + 9*UP)


        self.play(Write(text[7]), run_time=2)
        self.play(Write(text[8]), run_time=2)
        self.play(Write(text[9]), run_time=2)
        self.play(Write(text[10]), run_time=2)
        self.play(Write(text[11]), run_time=2)


        self.wait(2)





        point = self.input_to_graph_point(8, graph)
        # 直线x=15
        pline = self.get_vertical_line_to_graph(8, graph, color=YELLOW)
        ptext = TextMobject("(%f, %s)" % (8, 'o'))
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
        return (-x + 35)

    def func2(self, x):
        return (-x + 60)

    def func3(self, x):
        return (-x + 70)

    def func4(self, x):
        return (x + 3)












