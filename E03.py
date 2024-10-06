from manim import *

config.media_width = "80%"
config.verbosity = "WARNING"

## part1: animation basics

# since v0.18.0 we no longer use the colour module, 
# Manim brings its own Color class now:
from manim import ManimColor as Color

# manim -qm BasicAnimations

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, 
                             radius=1, 
                             # 为什么使用这种 hsv 代码格式，因为方便一个变量 ‘j’ 就可以改
                             # 变颜色。
                             # 
                             color=Color.from_hsv((j/5, 1.0, 1.0)), 
                             fill_opacity=0.5)
              for j in range(6)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time=2)

        # 1. vgruop 中的元素可以被索引
        # 2. rotate 方法的 rate_func 是一个 lambda 函数
        # 用来描述 “变化速度曲线”， 对于 rotate 而言就是 “旋转速度曲线” 
        # manim 中预定义了很多方法，官网的图示已经非常棒了：
        # https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html
        # 期中：
        # linear 就是缓慢的一直转，转速不变
        # smooth 就是从静止开始加速（起速顺滑）
        # there_and_back 转到头又转回来
        # 也可以自定义，但注意他是一个函数

        # 理解： rate_func : [0,1] -> [0,1]
        # 就是让你自己构造一个数学概念上的函数（比如，y=sinx, 在这里就是 X=sint），
        # manim 再让 mobj 根据你的函数来改变运动速度，看完上面一堆函数，你就能更好的理解这句话的意思。 
        # 后面会有自定义动画函数，不但可以定义速度，还能定义轨迹
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t),  # rate_func=linear
            Rotate(polys[1], PI, rate_func=smooth),       # default behavior for most animations
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t*PI/2)),
            Rotate(polys[3], PI, rate_func=lambda t: np.cos(t*PI)),
            Rotate(polys[4], PI, rate_func=there_and_back),
            Rotate(polys[5], PI, rate_func=lambda t: 1 - abs(1-2*t)),
            run_time=2
        )
        self.wait()

# %%manim -qm ConflictingAnimations

# 当你对同一个 mobj 进行动画操作的时候，会出现“动画冲突”
# manim 默认使用最后一个动画作为最终效果
class ConflictingAnimations(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        self.play(Rotate(s, PI), Rotate(s, -PI), run_time=3)




# %%manim -qm LaggingGroup

# 此段代码建立了两个 group: VGroup 和 AnimationGroup
# VGroup: vectorized group, 需要通过 unpack 一个 mobj 列表来创建，用于集体动画，变换等
# AnimationGroup 是让后面的元素逐个出现，两个元素出现的间隔时间由 lag_ratio 指定，他指定
# 的是前一个mobj的入完时间。
class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=Color.from_hsv((j/20, 1.0, 1.0)), fill_opacity=0.8) for j in range(20)])
        squares.arrange_in_grid(4, 5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))

## Part 2: Animations from Method calls and Functions

# %%manim -qm AnimateSyntax

# mobj 的 animate 方法，可以将 mobj 所有的方法“动画化”，不是只呈现转换后的结果，而是
# 呈现转换过程
# move_to 移动 --animate--> 呈现移动过程
class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s, c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s, c).animate.arrange(RIGHT))
        self.play(c.animate(rate_func=linear).shift(RIGHT).scale(2))
        self.wait()


# %%manim -qm AnimateProblem

class AnimateProblem(Scene):
    def construct(self):
        left_square = Square()
        right_square = Square()
        VGroup(left_square, right_square).arrange(RIGHT, buff=1)
        self.add(left_square, right_square)
        # 这里说的 animate 函数的一个问题是：
        # 注意这里一个是 mobj 的 rotate(小写)
        # 另一个是 animation 的 Rotate(大写)
        # animate.rotate 最终动画呈现的是放大缩小的效果？
        # 因为他只关注起点和终点，然后连接他们（存疑，但不影
        # 响使用，记住 animate.roate 不要旋转180，否则就用 
        # Animation的 Rotate 就行）
        self.play(left_square.animate.rotate(PI), Rotate(right_square, PI), run_time=2)


# %%manim -qm AnimationMechanisms

# Related animations: moveToTarget and Restore
#
# GeneraI philosophy: create a COPY Of a mobject, modify it however you like, 
# then transform between original mobject and modified COPY
# 
# MoveToTarget: call mob.generate_target(), then modify 
# mob.target 一 animate with MoveToTarget(mob)
# 补充: 
# 1. 生成 target: mobj.generate_target() -> target(不可见)
# 2. 修改 target:mobj.target.改变属性、位置方法
# 3. 生成动画（三步骤）：add(c) -> wait() -> play(MoveToTarget(c))
# 
# 
# Restore: call mob.save_state(), then keep modifying mob 一 animate return to 
# saved state with Restore(mob)
# 补充：
# 1. 保存当前状态
# 2. 改状态 -> 动画化 -> 播放(play)
# 3. 恢复状态
class AnimationMechanisms(Scene):
    def construct(self):
        c = Circle()
        
        # MoveToTarget(c)
        c.generate_target() #经过这一步，原始 mobj 对象的 ‘target’属性字段才不为空，之后才能对target对象进行修改
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)
        
        self.add(c) # 这一步是预先展示原始图像，让动画更完整不突兀
        self.wait()
        self.play(MoveToTarget(c))
        
        # save_state() 
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait() # wait 可以让对象停留在画面上
        self.play(Restore(s), run_time=2)

        self.wait()


# %%manim -qm --disable_caching SimpleCustomAnimation

# Custom Animations Via Functions
#
# Abstraction: an animation is a function mapping (mobject,completion,ratio) to 
# a # mobject
#
# def move_somewhere （ mobj, alpha) ：
#      mobj.move_to(alpha * RIGHT + alpha**2 * 2*UP)
#
# Given such a function, UpdateFromAIphaFunc constructs the corresponding animation!
# 
# Tip: store initial state in custom mobject attribute to allow for more flexibility!
# mobj.initial_position = mobj.get_center()
# ....then mobj·initial_position is available in the animation function 一 or write 
# custom animation

class SimpleCustomAnimation(Scene):
    def construct(self):

        # spiral_out 方法解析：
        # 整体轨迹就是：螺旋形的往外扩展
        # t 是类似 rate_func 参数 't' 是一个类似 percent 的数字
        # 表示从开始(0) 到结束（1）的时间内，mobject 会随着时间如何
        # 变化，所以，mobject 的关键属性都要写成关于 t 的变量。
        # mobject 是被处理的对象，所以两个参数是必须的
        def spiral_out(mobject, t):
            radius = 4 * t
            angle = 2*t * 2*PI
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(Color.from_hsv((t, 1.0, 1.0)))
            mobject.set_opacity(1-t)
        
        d = Dot(color=YELLOW)
        self.add(d)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))



## Part 3: Anatomy of Animations

# %%manim -qm --disable_caching CustomAnimationExample

# begin() — prepares first animation frame; stores mobject
# copy in self. starting_mobject

# interpolate_mobject(alpha) — brings self.mobject to
# the state of alpha% of animation completed; default: delegates
# to submobjects

# interpolate_submobject(sub, sub_start, alpha) —
# same as above, but for a specific submobject (in argument'

# finish() finishes animation, produces last frame

# clean_up_from_scene(scene) — all remaining mobjer+
# and scene cleanup (e.g., removing mobjects)

# Implementing your own Animation class
# Basically: inherit from Animation, override
# interpolate_mobject or interpolate_submobject

# Compare how other Animations in the library are
# implemented

# Good luck e

class Disperse(Animation):
    def __init__(self, mobject, dot_radius=0.05, dot_number=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_number = dot_number
    
    # begin 函数是用来展示视频第一帧的
    def begin(self):

        # 把一个 mobj 图形的外边框，变成点集
        dots = VGroup(
            # point_from_proportion 函数是把 mobj 的【边界】变成比例坐标，什么是比例坐标。
            # 举个例子，一个圆，从 [r, 0, 0] 处开始，就是 0%，走一圈回到 [r,0,0] 是 100%
            # 这里的意思是我生成指定数量（默认100）个点，然后先将他们移动到 mobj 图形的边界处
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_number)]
        )

        # 这里是遍历所有点，指定他们的初始位置和结束位置（通过位移向量 shift_vector指定），
        # 初始位置即为当前位置（边界处），结束位置是 2倍的从点当前位置到原点的距离。
        for dot in dots:
            dot.initial_position = dot.get_center()

            # shif_vector 是移动向量偏移量，末位置 - 初位置，这里用来给出结束位置的坐标
            dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())

        # 注意将这些点透明度设置为0
        dots.set_opacity(0)
        self.mobject.add(dots)

        # 上面针对每个点，设置了很多属性，比如 shif_vector, initial_position，我们需要
        # 让其他方法比如 interpolate_mobject 去使用这些被我们初始化的值，那就要把他们
        # 传递给父类对象。
        # 点集生成完毕后，要把他们赋值给父类对象点集属性，方便其他方法调用
        self.dots = dots
        super().begin()
        
    # 清理所有点
    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.dots)

    # 注意这里 alpha 是一个 mobj 朝目标状态变化的百分比，该 mobj 从初始到目标状态，变化了百分之多少
    # rate_func 是一个把均匀变化的时间值，映射成不均匀变化的时间值 --- 改变进程速度的一个函数（总时间
    # 不变，一部分变快了，另一部分变慢了，想想物理 s-t 函数）。 
    # 
    # 1. 这里，interploate_mobject 为了进行‘补间’，它就需要知道我在哪个时间点‘补’，就需要知道‘映射后进度条’
    # 也就是 alpha， 因为每个动画使用者都会尝试自己的 rate_func, 所以他需要做的第一件事就是获得‘映射后进度条’
    # 因为‘匀速进度条’和‘映射后进度条’就是通过 rate_func 联系起来的。
    # 
    # 2. 得到‘进度条’也就是‘时间值’之后，interpolate 就可以根据时间值按照自己希望的那样，处理 mobj 的属性
    # 使得该 mobj 在“对的时间做对的事”！
    def interpolate_mobject(self, alpha):

        # 首先接受一个系统均匀进度条，然后根据用户指定的 rate_func 将其转换成映射后进度条
        # 然后共给整个函数定义域下使用。
        alpha = self.rate_func(alpha)  # manually apply rate function
        # 如果不到一半
        if alpha <= 0.5:
            self.mobject.set_opacity(1 - 2*alpha, family=False)
            self.dots.set_opacity(2*alpha)
        
        # 如果超过一半
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1 - alpha))
            for dot in self.dots:

                # 不要特别纠结 alpha 是什么，用就完事了，就把它当成一个时间点
                # interpolate_mobject 是用来根据时间点生成帧的，你要做的就是
                # 接受时间（alpha），然后根据时间写出目标位置。
                dot.move_to(dot.initial_position + 2*(alpha-0.5)*dot.shift_vector)
            
            

class CustomAnimationExample(Scene):
    def construct(self):
        st = Star(color=YELLOW, fill_opacity=1).scale(3)
        self.add(st)
        self.wait()
        self.play(Disperse(st, dot_number=200, run_time=4))



