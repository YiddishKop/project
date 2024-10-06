from manim import *

# 1. 创建一个 Scene 扩展类，重写其中的 construct 方法
# 2. 利用 Mobject 全局类名，（可根据相对位置）创建 mob 对象 Circle Square 并填充属性
# 3. 最后需要将创建的形状对象，add 到 Scene 中才能展示在视频上
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK)  # set the color and transparency
        blue_circle = Circle(color=BLUE)
        green_square = Square(color=GREEN)
        green_square.next_to(blue_circle, RIGHT)
        self.add(blue_circle, green_square)  # show the circle on screen


# 1. 直角坐标系绘图常用三个形状类：Axes, Curve, Area
# 2. 这段代码展示的就是如何以动画的形式创建函数图像以及其与坐标轴围成的区域
# 3. 通过 scene 的 play 方法，展示形状被包装后的 Animation 类
class SecondExapmle(Scene):
    def construct(self):
        ax = Axes(x_range=(-3,3), y_range=(-3,3))              # 创建坐标轴及范围
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)  # plot 的第一个参数是要绘制的数学函数，返回curve mob对象
        area = ax.get_area(curve,x_range=(-2,0))               # get_area 绘制阴影面积
        self.play(Create(ax, run_time=1), Create(curve, run_time=3))
        self.play(FadeIn(area))
        self.wait(2)


class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))      # 场景一：绘制正方形
        blue_circle=Circle(color=RED, fill_opacity=0.7)

        # self.play(Transform(green_square, blue_circle))
        # self.play(FadeOut(blue_circle))
        # 注意这里有一个 manim 的 bug，在做完transform之后，两个变量名会产生交换
        # 场景二最后是正方形变圆形，按理说应该 fadeout blue_circle， 但是因为这个
        # bug，我们要 fadeout green_square。
        # 或者说这样理解，green_square 只是在外形上变成 blue_circle，但本源对象
        # 还是 green_square

        # 另种方法是直接使用 ReplacementTransform 这样就可以直接 fade out bluecircle 了
        self.play(ReplacementTransform(green_square, blue_circle))  # 场景二：正方形变成圆形

        self.play(Indicate(blue_circle))  # 通过变大凸显该 mob，引导用户注意力

        self.play(FadeOut(blue_circle))
        self.wait(3)
