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
V2_2 场景一和场景二实现
V2_3 动画的各个场景已经布置完成
'''

from manimlib.imports import *


class PlotFunctionsV2_3(GraphScene, Scene):
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
        # y=x
        graph6 = self.get_graph(self.func5, color=RED, x_min=10, x_max=50)

        graph_label1 = self.get_graph_label(graph3, label="(1)", x_val=33.5, direction=UP)
        graph_label2 = self.get_graph_label(graph, label="(2)", x_val=17, direction=UP)
        graph_label3 = self.get_graph_label(graph2, label="(3)", x_val=17, direction=UP)

        text = VGroup(
            ## 场景一
            Text("纵轴:价格 横轴:收入(可以理解为数量)", font='我的', buff=2),  # 0
            ## 场景二
            Text("需求曲线", font='我的'),  # 1
            Text("供给曲线", font='我的'),  # 2
            Text("交点(1)为正常经济下", font='未署名的信'),  # 3
            Text("的市场均衡价格和收入", font='未署名的信'),  # 4
            ## 场景三
            Text("新冠开始", font='未署名的信'),  # 5
            Text("各国陆续封锁", font='未署名的信'),  # 6
            Text("需求受到严重冲击", font='未署名的信'),  # 7
            Text("需求曲线发生变化", font='未署名的信'),  # 8
            ## 场景四
            Text("供应链受到更严重冲击", font='未署名的信'),  # 9
            Text("供给曲线变得无弹性", font='未署名的信'),  # 10
            Text("(供给不再随价格变化)", font='未署名的信'),  # 11

            Text("供给数量甚至不增反减", font='未署名的信'),  # 12

            Text("中短期会形成新的均衡点(2)", font='未署名的信'),  # 13
            Text("价格下降，数量减少", font='未署名的信'),  # 14


            Text("各国开始财政和货币政策刺激", font='未署名的信'),  # 15
            Text("通过印钞增加需求", font='未署名的信'),  # 16
            Text("(财政货币政策刺激需求曲线回移)", font='未署名的信'),  # 17


            Text("长期来看", font='未署名的信'),  # 18
            Text("供给弹性受到伤害后很难调整", font='未署名的信'),  # 19
            Text("造成过多的货币追逐不足的商品的局面", font='未署名的信'),  # 20
            Text("价格狂飙形成新的市场均衡点(3)", font='未署名的信'),  # 21

        ).scale(0.5).set_color('#EEC591')

        text.arrange(
            aligned_edge = LEFT,
        )

        ## 场景一：坐标简介
        text[0].scale(0.7)
        text[0].to_corner(UR)
        [
            VGroup(
                text[0][0:5].set_color('#00FF00'),
                text[1][5:].set_color('#5F9EA0'),
            ) for i in range(2)
        ]

        self.wait(2)

        self.play(Write(text[0]), run_time=2)

        ## 场景二：正常市场均衡点

        ## 点（1）
        # y=(-x + 70) 需求曲线
        self.play(ShowCreation(graph3))
        text[1].move_to((1 * LEFT) + (1 * DOWN))
        self.play(Write(text[1]), run_time=2)
        self.wait(1)
        self.remove(text[1])

        # y=(x + 3) 供给曲线
        self.play(ShowCreation(graph4))
        text[2].move_to((5 * LEFT) + (2 * DOWN))
        self.play(Write(text[2]), run_time=2)
        self.wait(1)
        self.remove(text[2])

        self.play(ShowCreation(graph_label1))

        # self.coords_to_point(33.5, 36.5)
        # self.wait(2)
        text[3].to_corner(RIGHT + 5 * UP)
        text[4].to_corner(RIGHT + 6 * UP)
        self.play(Write(text[3]), run_time=2)
        self.play(Write(text[4]), run_time=2)
        self.wait(2)
        self.remove(text[3])
        self.remove(text[4])
        # self.remove(graph3)
        # self.remove(graph4)
        self.remove(graph_label1)

        ## 场景三：需求曲线发生变化

        # self.add(graph3)
        # self.add(graph)


        text[5].to_corner(RIGHT + 5 * UP)
        text[6].to_corner(RIGHT + 6 * UP)
        self.play(Write(text[5]), run_time=2)
        self.play(Write(text[6]), run_time=2)
        self.wait(2)
        self.remove(text[5])
        self.remove(text[6])

        text[7].to_corner(RIGHT + 5 * UP)
        text[8].to_corner(RIGHT + 6 * UP)
        self.play(Write(text[7]), run_time=2)
        self.play(Write(text[8]), run_time=2)

        text[1].move_to((1 * LEFT) + (1 * DOWN))
        self.play(Write(text[1]), run_time=2)
        self.remove(text[1])

        self.play(graph3.move_to, graph, run_time=3)
        self.wait(2)
        self.remove(text[7])
        self.remove(text[8])

        ## 场景四：供应曲线发生变化
        text[9].to_corner(RIGHT + 5 * UP)
        text[10].to_corner(RIGHT + 6 * UP)
        text[11].to_corner(RIGHT + 7 * UP)
        self.play(Write(text[9]), run_time=2)
        self.play(Write(text[10]), run_time=2)
        self.play(Write(text[11]), run_time=2)

        self.play(graph4.rotate, 45 * DEGREES, axis=OUT, run_time=3)
        self.wait(2)
        self.remove(text[9])
        self.remove(text[10])
        self.remove(text[11])

        text[12].to_corner(RIGHT + 5 * UP)
        self.play(Write(text[12]), run_time=2)
        text[2].move_to((2 * LEFT) + (1 * DOWN))
        self.play(Write(text[2]), run_time=2)
        self.remove(text[2])
        self.play(graph4.move_to, graph5, run_time=3)
        self.remove(text[12])


        # self.play(graph3.shift, LEFT*5 + DOWN*5)
        # self.play(MoveAlongPath(graph3, graph6), run_time=10)


        ## 场景五：新的均衡点（2）
        text[13].to_corner(RIGHT + 5 * UP)
        text[14].to_corner(RIGHT + 6 * UP)
        self.play(Write(text[13]), run_time=2)
        self.play(ShowCreation(graph_label2), run_time=2)
        self.play(Write(text[14]), run_time=2)

        self.remove(text[13])
        self.remove(text[14])
        self.remove(graph_label2)

        ## 场景六：强刺激
        text[15].to_corner(RIGHT + 5 * UP)
        text[16].to_corner(RIGHT + 6 * UP)
        text[17].to_corner(RIGHT + 7 * UP)
        self.play(Write(text[15]), run_time=2)
        self.play(Write(text[16]), run_time=2)
        self.play(Write(text[17]), run_time=2)

        ## 点（3）
        # y=(-x + 60)
        self.remove(graph3)
        self.play(graph.move_to, graph2, run_time=3)
        self.remove(text[15])
        self.remove(text[16])
        self.remove(text[17])
        #self.remove(graph2)

        ## 场景七：新的均衡点（3）




        text[18].to_corner(RIGHT + 5 * UP)
        text[19].to_corner(RIGHT + 6 * UP)
        text[20].to_corner(RIGHT + 7 * UP)
        text[21].to_corner(RIGHT + 8 * UP)

        self.play(Write(text[18]), run_time=2)
        self.play(Write(text[19]), run_time=2)
        self.play(Write(text[20]), run_time=2)
        self.play(ShowCreation(graph_label3))
        self.play(Write(text[21]), run_time=2)
        self.remove(text[18])
        self.remove(text[19])
        self.remove(text[20])
        self.remove(text[21])
        self.remove(graph_label3)

        self.wait(2)


    def func(self, x):
        return (-x + 35)

    def func2(self, x):
        return (-x + 60)

    def func3(self, x):
        return (-x + 70)

    def func4(self, x):
        return (x + 3)

    def func5(self, x):
        return x











