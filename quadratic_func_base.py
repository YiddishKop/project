from manim import *

FONT_CN='STZhongsong'
HEADING_1= 80
SCENE_WIDTH= 14
SCENE_HEIGHT= 8
SCENE_LEFT = - 7.11
SCENE_RIGHT = 7.11
SCENE_TOP = 4
SCENE_DOWN= -4


# 可以用 group + arrange_in_grid 来给所有画布元素进行初始布局
class TESTArrangeInGrid(Scene):
    def construct(self):
        boxes = VGroup(*[
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))
            for i in range(24)
            ])
        
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[2, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr")


class Test2(Scene):
        def construct(self):

            funcs_gp = VGroup(*[
                Rectangle(WHITE, 2, 2) for i in range(5)
            ])

            funcs_gp.arrange(buff=0.3).to_edge(UP)

            ax = NumberPlane(
                x_range=[-16,16,3],
                y_range=[-16,18,3],
                x_length=8,
                y_length=8,
                axis_config={
                    "include_numbers": False,
                    "tip_width": 0.15, # 箭头大小---宽
                    "tip_height": 0.15, # 箭头大小---高
                    "include_ticks": True,
                    "tick_size": 0.05,
                    "include_tip": True, # Add a tip to x-axis and y-axis
                    })
        
            fun1_1 = ax.plot(lambda x: x+1/x, color=RED, x_range=[-8,-0.2])
            fun1_2 = ax.plot(lambda x: x+1/x, color=RED, x_range=[0.2, 8])
            fun_nike = VGroup(fun1_1,fun1_2)

            fun2 = ax.plot(lambda x: 4*np.sin(x), color=RED, x_range=[-8,8])
            fun3 = ax.plot(lambda x: np.exp(x), color=RED, x_range=[-8,2.7])
            fun4 = ax.plot(lambda x: np.log(x), color=RED, x_range=[0.01, 15])
            fun5 = ax.plot(lambda x: 1/2*x*x*x-2*x, color=RED, x_range=[-3,3])
            # self.add(ax, fun_nike, fun2, fun3, fun4, fun5)

            self.play(Create(ax, run_time=1.5))
            self.play(Create(fun_nike))
            self.play(fun_nike.animate.scale(0.5).move_to(funcs_gp[0], UP), run_time=2)
            self.play(FadeIn(funcs_gp[0]))

            self.play(Create(fun2))
            self.play(fun2.animate.scale(0.5).move_to(funcs_gp[1], [0,0,0]), run_time=2)
            self.play(FadeIn(funcs_gp[1]))


            self.play(Create(fun3))
            self.play(fun3.animate.scale(0.5).move_to(funcs_gp[2], [0,0,0]), run_time=2)
            self.play(FadeIn(funcs_gp[2]))


            self.play(Create(fun4))
            self.play(fun4.animate.scale(0.5).move_to(funcs_gp[3], [0,0,0]), run_time=2)
            self.play(FadeIn(funcs_gp[3]))


            self.play(Create(fun5))
            self.play(fun5.animate.scale(0.5).move_to(funcs_gp[4], [0,0,0]), run_time=2)
            self.play(FadeIn(funcs_gp[4]))

            return super().construct()




# 如何导入图片文件，并且将其放置在画布上
class Test1(Scene):
    def construct(self):

        # 莱布尼茨 提出 function 这个单词
        img1 = ImageMobject("Leibniz.jpg").scale(0.5)
        # 柯西 指数函数需要两个量，一个自变量，一个因变量
        img2 = ImageMobject("Cauchy.jpg")
        # 迪利克雷 最终定义了较完整的函数意义
        img3 = ImageMobject("Dirichlet.jpg")
        # 李善兰将 fucntion 引入中国，并翻译其为 “函数”
        img4 = ImageMobject('lishanlan.jpg')

        gp_img = Group(img1, img2, img3, img4)
        gp_img.arrange_in_grid(
            rows=2,
            cols=2,
        )
        self.add(gp_img)




class Scene_1(Scene):   # 三种函数的图形展示

    def construct(self):

        # 构建其他函数图，扩展学生理解见识

        funcs_gp = VGroup(*[
            Rectangle(WHITE,3,3) for i in range(5)
        ])

        funcs_gp.arrange(buff=0.3)

        # 构建三个正方形方框4*4长宽，间隔0.5，分别放在 [-4.5,-1,0]\[0,-1,0]\[4.5,-1,0]位置
        # 作为坐标系和函数图像的目标位置
        square_lin = Square(side_length=SCENE_HEIGHT/2, color=WHITE).move_to([-4.5,-2,0])
        square_quadra = square_lin.copy().move_to([0,-2,0])
        square_inverse = square_lin.copy().move_to([4.5,-2,0])

        # 构建文字说明
        tex_lin = MarkupText('一次函数', font_size=40, font=FONT_CN).next_to(square_lin, UP)
        tex_quadra = MarkupText('二次函数', font_size=40, font=FONT_CN).next_to(square_quadra, UP)
        tex_inverse = MarkupText('反比例函数', font_size=40, font=FONT_CN).next_to(square_inverse, UP)

        # 构建三个正方形坐标系（NumpberPlane），为满足画布高度=8，所以坐标系范围从 -4 到 4
        ax_lin = NumberPlane(
            x_range=[-4,4],
            y_range=[-4,4],
            axis_config={
                "include_numbers": True,
                "tip_width": 0.15, # 箭头大小---宽
                "tip_height": 0.15, # 箭头大小---高
                "include_ticks": True,
                "tick_size": 0.05,
                "include_numbers": True,
                "include_tip": True, # Add a tip to x-axis and y-axis
                })
        ax_quadra = ax_lin.copy()
        ax_inverse = ax_lin.copy()

        # 在坐标系上分别画三个函数：一次，二次、反比例
        curve_lin = ax_lin.plot(lambda x: x-2, color=RED, x_range=[-2,4])
        curve_quadra = ax_quadra.plot(lambda x: x*x-2, color=RED, x_range=[-2,2])
        # 反比例函数涉及跨“0”点问题，只能这么写
        curve_inverse_1 = ax_inverse.plot(lambda x: 1/x, color=RED, x_range=[0.3,4])
        curve_inverse_2 = ax_inverse.plot(lambda x: 1/x, color=RED, x_range=[-4,-0.3])
        

        # 对三个对象进行分组（将边框、坐标系、函数图像组合在一起实现联动）和动画生成
        # 一次函数
        group_lin = VGroup(ax_lin, curve_lin, square_lin, tex_lin)
        self.play(Create(group_lin[0]))
        self.play(Create(group_lin[1]))
        # 下面这行代码是分组的原因，坐标系和函数图像组合联动
        self.play(group_lin[0:2].animate.scale(0.5).align_to(group_lin[2], LEFT+UP), run=2)
        self.play(FadeIn(group_lin[2], group_lin[3]))

        # 二次函数
        group_quadra = VGroup(ax_quadra, curve_quadra, square_quadra, tex_quadra)
        self.play(Create(group_quadra[0]))
        self.play(Create(group_quadra[1]))
        self.play(group_quadra[0:2].animate.scale(0.5).align_to(group_quadra[2], LEFT+UP), run=2)
        self.play(FadeIn(group_quadra[2], group_quadra[3]))

        # 反比例函数
        group_inverse = VGroup(ax_inverse, VGroup(curve_inverse_1, curve_inverse_2), square_inverse, tex_inverse)
        self.play(Create(group_inverse[0]))
        self.play(Create(group_inverse[1][0]), Create(group_inverse[1][1]))
        self.play(group_inverse[0:2].animate.scale(0.5).align_to(group_inverse[2], LEFT+UP), run=2)
        self.play(FadeIn(group_inverse[2], group_inverse[3]))

        self.wait(2)

        return super().construct()



class Scene_2(Scene):  # 简单回忆什么是一次函数
    def construct(self):


        # 1. 什么是函数
        tex_question = MarkupText('什么是函数？', font=FONT_CN, font_size=HEADING_1)

        # 2. 多种函数的不断加快放映, 最常见的函数：一次函数、二次函数、反比例函数
        # Scene-2

        # 介绍函数的产生
        # 从一个我们熟悉的规律提开始
        
        mt3 = MarkupText('1, 3, 5, ___, 9', font=FONT_CN, font_size=HEADING_1)
        mt31 = MarkupText('1, 3, 5, _<span fgcolor="red">7</span>_, 9', font=FONT_CN, font_size=HEADING_1)

        # 在换一道
        mt4 = MarkupText('再进一步', font=FONT_CN, font_size=HEADING_1)

        mt5 = Table([['第一行','1','3','5','7','9'],
                     ['第二行','2','4',' ','8','10']],
                    include_outer_lines=True,
                    line_config={
                        "stroke_width": 2,
                        "color": WHITE,
                    },)
        
        mt5.add_highlighted_cell(pos=(2,4))

        mt5.set_row_colors==[BLUE, RED]

        self.play(Write(tex_question))
        self.play(FadeOut(tex_question))

        self.play(FadeIn(mt3))
        self.play(ReplacementTransform(mt3, mt31))
        self.play(FadeOut(mt31))


        self.wait(2)
        


        return super().construct()


class QuadraFunc4Point(Scene):
    def construct(self):

        # 坐标轴
        ax = Axes(x_range=(-6,6), 
                  y_range=(-5,5),
                  tips=True,
                  axis_config={"include_numbers":True})
        
        # 给坐标轴加箭头和名称
        ax_labels = ax.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
        
        curve = ax.plot(lambda x: x*x -2*x-3, color=RED)


        # 文字
        # t = Title("二次函数基本知识")

        mtext = VGroup(
            MarkupText('二次函数<span fgcolor="red">四</span>点绘图法', font='STZhongsong', font_size=30),
            # Tex("二次函数四点绘图法"),
        )

        mtext.move_to([0,3.5,0])

        # 通过坐标获取屏幕位置
        pt1 = ax.coords_to_point(-1,0,0)
        pt2 = ax.coords_to_point(3,0,0)
        pt3 = ax.coords_to_point(0,-3,0)
        pt4 = ax.coords_to_point(1,-4,0)
        
        


        # 四点绘图，根据屏幕位置描绘四个 dot
        dot1 = Dot(radius=0.2, stroke_width=0.2,fill_opacity=0.5,color=BLUE)
        dot1.move_to(pt1)
        dot2 = dot1.copy()
        dot2.move_to(pt2)
        dot3 = dot1.copy()
        dot3.move_to(pt3)
        dot4 = dot1.copy()
        dot4.set_color(YELLOW)
        dot4.move_to(pt4)

        for i in VGroup(ax, curve, dot1, dot2, dot3, dot4): 
            self.play(Create(i))
        
        self.play(Transform(ax, mtext))
        return super().construct()