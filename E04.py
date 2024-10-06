from manim import *

config.media_width = "80%"
config.verbosity = "WARNING"

# 本集视频介绍了Manim中的更新函数，
# 解释了它们的定义、用途及类型。某个对象的更新函数会在这个对象每帧渲染前被调用，
# 确保场景中的对象根据时间变化而更新。
# 视频中展示了
# 对象更新器和场景更新器的使用方法，
# 以及如何通过更新函数实现对象间的相互依赖。
# 还介绍了如何使用值跟踪器来平滑地动画化数值变化，
# 具体示例包括绘制抛物线并实时更新其参数。
# 最后，视频鼓励观众提出问题并订阅频道。


# What is an Updater Function?
# Special function that is called right before Manim captures a
# new frame

# ... can be attached to Mobjects ("Mobject updater") or the Scene
# itself ("Scene updater")

# ... can depend on time passed since last rendered frame ("time
# dependent updaters")


# Why are updaters useful?
# Mobjects can be made dependent on other mobjects!
# Example: make a label move with its mobject:
# construct ( selt )
# def construct(self):
#   blue_dot = Dot(color=BLUE)
#   dot_label = Text( "Hello dot! ").next_to(blue_dot, UP)

# 下面这条语句的意思就是把 updater 函数绑定到 dot_label 上。
# updater 就是去始终保持 mobject 在 blue_dot 的上面。

# 谁要作为随从，就用谁的 updater（可以把 updater 理解为一个自我更新器），
# 并绑到主人的 mobj 对象上
# dot_label.add_updater(
#     lambda mobject: mobject.next_to(blue_dot, UP))

# self. dot
# self. play ( blue_dot. anGate. shift ( RIGHT) )
# self. play (blue_dot. animate. scale ( 3 ) )
# self .play(blue dot. animate.center( ) )


# %%manim -qm MovingLabel

class MovingLabel(Scene):
    def construct(self):
        blue_dot = Dot(color=BLUE)
        dot_label = Text("Hello dot!").next_to(blue_dot, UP)

        # 已更新 update 的形式，让标签始终处在 bluedot 上面。
        # 这就相当于对二人进行了分组，一个动另一个也跟随者的着动
        # add_updater 需要被传入函数参数，这里传入的是一个匿名函数
        # 其接收 mobj(这里就是 dot_label)，然后调用这个 mobj 的next_to
        # 方法，将他设置为 blue_dot 旁边

        # 原理是，每一帧，主动对象先渲染，然后被动对象(被 updater 绑定）被
        # 按照 updater 方法中定义的方式（比如这里是 next_to）‘随着’主动对象而渲染。
        dot_label.add_updater(
            lambda mobject: mobject.next_to(blue_dot, UP)
        )
        self.add(blue_dot, dot_label)
        self.play(blue_dot.animate.shift(RIGHT))
        self.play(blue_dot.animate.scale(10))
        self.play(blue_dot.animate.move_to([-2, -2, 0]))


#### Examples using Updater Functions
#### %%manim -qm --disable_caching AllUpdaterTypes

# add_updater 第一个参数一般都是 add_updater 的调用者 --- 也就是随从。
#             第二个参数一般都是 dt，表示下一帧位置等，类似于alpha的作用
# add_updater(mob) --> 使 mob 与其他mobj绑定位置比如 next_to
# add_updater(mob,dt) --> 使 mob 按照逐帧生成的方式已经变换比如 mob.shift(2*dt*RIGHT)
# add_updater(dt) --> 看似没有 mob，但是你可以通过其他方式来获取mob，比如 for mob in self.mobjects
class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)

        # 注意 add_updater 对调用者使用的方式是：谁调用，谁就作为 add_updatter
        # 的函数参数的参数。
        pointer.add_updater( # place arrow left of dot
            lambda mob: mob.next_to(red_dot, LEFT)
        )
        
        # 这里的 dt 相当于微积分，也就是我们产生动画的另一个方式：通过时间给出下一帧的状态、位置
        # 然后渲染出下一帧即可
        def shifter(mob, dt): # make dot move 2 units RIGHT/sec
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)
        
        def scene_scaler(dt): # scale mobjects depending on distance to origin
            for mob in self.mobjects:
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)
        
        self.add(red_dot, pointer)
        # scene has to update initially   to fix first frame:
        # first mobject updaters are called, then scene updaters
        self.update_self(0)
        self.wait(5)


#### Combining Updater Functions and Animations

# %%manim -qm --disable_caching UpdaterAndAnimation

class UpdaterAndAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(lambda mob, dt: mob.rotate(dt*PI))
        
        def shifter(mob, dt): # make dot move 2 units RIGHT/sec
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)
        
        self.add(red_dot, rotating_square)
        self.wait(1)

        # 随时可以通过 suspend_updating 来终止 updater
        red_dot.suspend_updating()
        self.wait(1)
        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2, -2, 0])
        )
        self.wait(1)

#### `ValueTracker`
# %%manim -qm ValueTrackerMove

class ValueTrackerMove(Scene):
    def construct(self):
        line = NumberLine(x_range=[-5, 5])

        # 1. value tracker 是整个动画过程的源动力

        # 2. mathtex 依赖 vector，vector 需要依赖一个‘位置’，而这个位置是
        # 由 numberLine 的 方法 n2p （number_to_point）提供的

        # 3. 整个动画怎么动起来？通过移动 valuetracker 动起来的。

        # ValueTracker 是 Manim 中一个用于跟踪实时参数的对象，它专门用于存储和管理
        # 实数值的变化。它是一个不可见的辅助 mobject，通常用于与可见元素
        # （如 DecimalNumber）结合使用，以实现动态效果。
        position = ValueTracker(0)
        pointer = Vector(DOWN)
        pointer.add_updater(
            lambda mob: mob.next_to(
                line.number_to_point(position.get_value()), UP
            )
        )
        pointer.update()
        self.add(line, pointer)
        self.wait()
        self.play(position.animate.set_value(4))
        self.play(position.animate.set_value(-2))

# %%manim -qm ValueTrackerPlot

class ValueTrackerPlot(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        parabola = ax.plot(lambda x: a.get_value() * x**2, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color=RED))
        )
        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))

