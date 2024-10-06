from manim import *

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next_to from episode 1
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        blue_dot = Dot(color=BLUE)
        green_dot.next_to(red_dot, RIGHT)  # RIGHT=[1,0,0]
        blue_dot.next_to(green_dot)
        # green_dot.next_to(red_dot, RIGHT + UP)  # RIGHT+UP=[1,1,0]
        self.add(red_dot,green_dot,blue_dot)


        # shift
        # 每次生成图像都是在 plane 的中间，然后再移动图像
        s = Square(color=ORANGE)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)
        

        # move_to
        c = Circle(color=PURPLE)
        c.move_to([-3,-2,0])
        self.add(c)


        # align_to 对齐
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2,c3,c4)

# 展现几种常用的方位：UP,UR,RIGHT,DR,DOWN,DL,LEFT,UL
# 每一种方位，都对应了 np.array (可以当成python中的列表）
# 原点 [0,0,0]
# UP   [0,1,0]
# LEFT [-1,0,0]
class CriticalPoint(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [[0,0,0], UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1,0,0], aligned_edge=UP)
        # WRONG! s.move_to((1,0,0), aligned_edge=UP)
        self.add(s)


from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        p = NumberPlane()
        self.add(p)

        for perc in range(5,51,5):
            self.add(Circle(radius=perc* Percent(X_AXIS) ))
            self.add(Square(side_length=2*perc*Percent(X_AXIS), color=YELLOW))
        # return super().construct()

        # pixel 会根据渲染的分辨率相对位置发生变化
        # 就像位图和线图
        d=Dot()
        d.shift(100 * Pixels * RIGHT)
        self.add(d)


# 给 mobj 进行分组
# 分组常用函数： VGroup -> arrange/arrange_in_grid
#                     -> to_edge
# arrange(left) 和 arrange(right) 默认横向排列所有元素,效果一样
# up,down 同理
class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)      # 移动整个组到屏幕显示的上下左右边界（注意有页边距，不会贴屏幕边缘显示）
        self.add(dot_group)        # vgroup 作为一个整体传给 add 就能显示
        # return super().construct()

        # 注意这里 * 运算符是 unpack 运算符，因为 VGroup 只接受多参数，不接收列表参数
        # 所以需要 unpack 拆开列表
        circles = VGroup(*[Circle(radius=0.2) for _ in range(3)])
        circles.arrange(LEFT, buff=0.5)        # 给一组元素排序，否则他们都处在[0,0,0]位置
        # buff 可以改变 vgroup 元素彼此距离
        
        self.add(circles)

        stars = VGroup(* [Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.2)
        self.add(stars)




# manim cfg write -l cwd
# 配置文件生成之后，可以使用一些配置代码进行配置

config.background_color = BLACK
config.frame_width = 9
config.frame_height = 16

config.pixel_width = 1080   #手机常用
config.pixel_height = 1920  #手机常用


class SimpleScene(Scene):
    def construct(self):
        np = NumberPlane(x_range=(-4,4), y_range=(-8,8))
        t = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(np, t)
        # return super().construct()



class ChangeDefaults(Scene):
    def construct(self):
        # 设置默认字体颜色
        Text.set_default(color=GREEN, font_size=100)
        t = Text("Hello World!", color=PURE_RED)
        t2 = Text("世界，你好！", color=PURPLE)
        t3 = Text("Welcome@YOU", font_size=60)
        t.move_to([0, 3, 0])
        t2.next_to(t, DOWN*3)
        t3.next_to(t2, DOWN*3)
        self.add(t, t2, t3)
        # return super().construct()