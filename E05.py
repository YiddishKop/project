from manim import *
from manim.opengl import *

config.media_width = "80%"
config.verbosity = "WARNING"

# 内容概括
# 本期教程介绍了Manim中的交互性功能，重点讲解了OpenGL渲染器的使用。与默认渲染器不同，OpenGL渲染器利用GPU进行渲染，支持更复杂的场景和交互。视频中展示了如何在本地运行代码以实现交互功能，包括键盘和鼠标的操作。通过实例演示了如何创建可交互的动画，用户可以通过按键控制场景，实时查看效果。尽管当前交互功能主要在本地使用，但它为用户提供了更丰富的动画体验。 


# 亮点:
# 00:09 本集视频介绍了OpenGL渲染器的交互性特性，这些特性可能大家并不熟悉。
#       通过使用OpenGL渲染器，用户可以体验更加丰富的交互效果，但在使用时也
#       要注意相关的设置和文档不足的问题。
#           -OpenGL渲染器与Cairo渲染器的区别在于其背后的渲染方法完全不同。
#            OpenGL渲染器利用GPU进行渲染，可以实现更复杂的图形效果，尤其在
#            处理动态对象时表现更佳。
#           -在视频中提到的交互嵌入方法，可以让用户通过代码实现实时的交互效果。
#            通过特定的命令设置，用户可以激活OpenGL渲染器，以便体验这些交互功能。
#           -视频还提到键盘和鼠标的交互方式，这对于创建用户友好的界面至关重要。
#           通过合理的交互设计，用户能够更有效地与模型进行互动，提升使用体验。
# 06:04 在三维场景中，使用欧拉角可以灵活地控制相机的旋转，进而改变观察视角。相机
#       本质上是一个可以操控的对象，通过设置角度来实现不同的视图效果。
#           -相机的旋转通过设置欧拉角来实现，具体来说，theta和phi角度的变化会影响观
#           察的方向和视角。通过将相机从顶视图旋转到倾斜视图，可以获得更丰富的场景观察体验。
#           -OpenGL 渲染器能够创建更复杂的表面模型，这与默认渲染器的简单拼接不同。通
#           过定义参数曲面并渲染其网格，可以实现更加平滑和自然的效果，提升视觉表现。
#           -光源的方向同样可以影响渲染效果。在 OpenGL 渲染器中，可以通过移动光源观察表面
#           在不同光照条件下的变化，增强了场景的立体感和真实感。
# 12:08 本视频介绍了如何在OpenGL渲染器中设置光源和相机角度，以实现更好的视觉效果。
# 通过调整光源的高度和旋转角度，可以观察到表面纹理的变化和渲染效果的提升。
#           -光源位置和旋转角度对渲染效果的影响很大，调整这些参数可以让我们更清晰
#           地看到物体的表面纹理。光源通常被放置在较高的位置，以便从不同角度观察对象。
#           -OpenGL纹理对象的使用能够实现复杂的视觉效果，例如在球体表面应用昼夜变化
#           的地球纹理。这种技术使得渲染物体的光照效果更加生动和真实。
#           -交互式渲染预览功能允许用户在渲染过程中与场景进行交互。这种功能通过命令
#           行标志启用，提供了更灵活的操作体验。
# 18:11 在本视频中，讲解了如何使用单独的终端窗口进行OpenGL渲染和交互操作。通过实时预览
# 和命令输入，用户可以更方便地观察和修改渲染效果，提高了开发效率。
#           -在视频中，演示了如何通过命令输入实现相机动画和图形变换。用户可以使用简
#           单的命令来改变对象的属性，例如创建一个红色的球体并调整其大小。
#           -讲解了OpenGL中的一些常见问题和解决方案。例如，在进行对象转换时可能会出
#           现意外效果，用户需要探索不同的变换方式以获得预期的结果。
#           -介绍了预览窗口的交互功能，包括鼠标和键盘的操作。用户通过鼠标移动和点击
#           可以轻松调整视角，并使用快捷键快速重置相机位置。
# 24:14 在本视频中，我们将探讨如何在场景中实现键盘交互性。我们将使用一些方法来创建用
#       户交互，包括处理鼠标移动和键盘按键事件的示例。 
#           -视频中还将讨论如何处理鼠标的位置数据，包括 `scene.mousepoint` 和
#            `scene.mouse_drag_point`，这对于确定用户在场景中的交互位置至关重要。
#           -我们将详细介绍如何使用 `scene.on_keypress` 方法来处理键盘输入，以及
#           如何比较按键符号与预定义常量。通过这种方式，可以实现不同键位的交互功能。
#           -接下来，我们将通过两个具体的例子来展示如何实现这些交互功能，其中一个例
#           子涉及到根据鼠标位置动态调整圆的半径，这将帮助理解如何实现图形交互。
# 30:18 在这个视频中，讲解了如何使用Piglet库中的键盘输入来控制光标的动画。通过按下特
# 定的键，可以使光标跳转到鼠标当前位置，动态交互增强了用户体验。
#           -首先，视频展示了如何导入Piglet库的键常量，这是在处理键盘输入时的关键步骤。
#           导入的时机也很重要，必须在需要时才进行，以避免错误发生。
#           -接下来，视频演示了如何通过按下键盘上的特定按键来播放动画。具体来说，按下
#           'g'键会使光标移动到鼠标的当前位置，展示了动态交互的实现。
#           -最后，视频介绍了牛顿迭代法的应用，展示了如何通过选择起始点并显示迭代步骤来
#           找到函数的根。这个示例展示了更加复杂的数学应用，增加了内容的深度。
# 36:23 在这个视频中，讲述了如何通过自定义交互来实现图形的动态展示。通过调用交互嵌入方法，
# 可以让用户与场景进行互动，使得图形更加生动直观。
#           -自定义交互的实现方法是通过按下特定的键来控制图形中点的移动。这种方式允许用
#           户通过鼠标指针的相对位置来更新图形的数据展示，增强了用户体验。
#           -视频中还介绍了如何利用牛顿迭代法来计算新的x值。这一方法通过函数的导数进行
#           计算，能够有效地逼近目标值，是一种常用的数值分析技术。
#           -此外，视频还提到如何绘制切线来辅助理解函数的变化。通过动态绘制切线，用户可
#           以更好地理解函数在特定点的斜率及其变化趋势，这对学习微积分非常有帮助。
# 42:26 该视频讨论了交互式动画的实现过程，特别是在图形和坐标系中如何动态移动点以展示函数
# 变化。这种方法虽然有趣，但目前只能在本地使用，缺乏与他人分享的有效方式。
#           -首先，视频展示了如何通过调整坐标来移动图形中的点，并动态更新y坐标以匹配函数
#           值。这种实时交互增强了学习体验，使得观众能够更好地理解函数的变化。
#           -其次，视频提到在实现过程中遇到的错误，尤其是如何确保点的位置正确。这种错误
#           的识别和修正过程强调了编程和数学模型之间的紧密联系。
#           -最后，尽管这种交互式动画很有趣，但视频也提到目前的局限性，特别是在分享方面。
#           虽然无法直接分享这些动画，录制屏幕的方法可以作为一种替代方案。


#### Basic demo of the OpenGL renderer

## %%manim -qm --renderer=opengl --write_to_movie OpenGLIntro

class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Tex("Hello World!").scale(3)
        self.play(Write(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10*DEGREES,
                phi=50*DEGREES
            )
        )
        self.play(FadeOut(hello_world))
        surface = OpenGLSurface(
            lambda u, v: (u, v, u*np.sin(v) + v*np.cos(u)),
            u_range=(-3, 3),
            v_range=(-3, 3)
        )
        surface_mesh = OpenGLSurfaceMesh(surface)
        self.play(Create(surface_mesh))
        self.play(FadeTransform(surface_mesh, surface))
        self.wait()
        light = self.camera.light_source
        self.play(light.animate.shift([0, 0, -20]))
        self.play(light.animate.shift([0, 0, 10]))
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))
        
        # self.interactive_embed()

        # self.play(self.camera.animate.set_euler_angles(theta=0*DEGREES))
        # self.play(FadeOut(surface, shift=np.array([0, 0, -2])))

        # red_sphere = Sphere(color=RED)
        # self.play(Create(red_sphere))
        # self.play(red_sphere.animate.scale(3))

        # sphere_mesh = OpenGLSurfaceMesh(red_sphere)
        # play(Transform(red_sphere, sphere_mesh))  # graphics glitch :-)

        # self.play(self.camera.animate.set_euler_angles(phi=0, theta=0))
        


### Examples for keyboard interactivity

# %%manim -qm --renderer=opengl --write_to_movie InteractiveRadius

class InteractiveRadius(Scene):
    def construct(self):
        plane = NumberPlane()
        cursor_dot = Dot().move_to(3*RIGHT + 2*UP)
        red_circle = Circle(
            radius=np.linalg.norm(cursor_dot.get_center()),
            color=RED
        )
        red_circle.add_updater(
            lambda mob: mob.become(
                Circle(
                    radius=np.linalg.norm(cursor_dot.get_center()),
                    color=RED
                )
            )
        )
        self.play(Create(plane), Create(red_circle), FadeIn(cursor_dot))
        self.cursor_dot = cursor_dot
        self.interactive_embed()  # not supported in online environment

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as pyglet_key
        if symbol == pyglet_key.G:
            self.play(
                self.cursor_dot.animate.move_to(self.mouse_point.get_center())
            )
        super().on_key_press(symbol, modifiers)


# %%manim -qm --renderer=opengl --write_to_movie NewtonIteration

class NewtonIteration(Scene):
    def construct(self):
        self.axes = Axes()
        self.f = lambda x: (x+6) * (x+3) * x * (x-3) * (x-6) / 300
        curve = self.axes.plot(self.f, color=RED)
        self.cursor_dot = Dot(color=YELLOW)
        self.play(Create(self.axes), Create(curve), FadeIn(self.cursor_dot))
        self.interactive_embed()  # not supported in online environment

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as pyglet_key
        from scipy.misc import derivative
        if symbol == pyglet_key.P:
            x, y = self.axes.point_to_coords(self.mouse_point.get_center())
            self.play(
                self.cursor_dot.animate.move_to(self.axes.c2p(x, self.f(x)))
            )

        if symbol == pyglet_key.I:
            x, y = self.axes.point_to_coords(self.cursor_dot.get_center())
            # Newton iteration: x_new = x - f(x) / f'(x)
            x_new = x - self.f(x) / derivative(self.f, x, dx=0.01)
            curve_point = self.cursor_dot.get_center()
            axes_point = self.axes.c2p(x_new, 0)
            tangent = Line(
                curve_point + (curve_point - axes_point)*0.25,
                axes_point + (axes_point - curve_point)*0.25,
                color=YELLOW,
                stroke_width=2,
            )
            self.play(Create(tangent))
            self.play(self.cursor_dot.animate.move_to(self.axes.c2p(x_new, 0)))
            self.play(
                self.cursor_dot.animate.move_to(self.axes.c2p(x_new, self.f(x_new))),
                FadeOut(tangent)
            )
        
        super().on_key_press(symbol, modifiers)