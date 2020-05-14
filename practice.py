from manimlib.imports import *

class FirstScene(Scene):
    def construct(self):
        text = TextMobject("This is some text")
        text2 = TextMobject("This is some other text")
        text3 = TextMobject("Third Text")
        self.play(Write(text))
        self.wait()
        self.play(FadeIn(text2))
        self.wait()
        self.play(GrowFromCenter(text3))
        self.wait()

class SecondScene(Scene):
    def construct(self):
        text = TextMobject("This is some text")
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()

class ThirdScene(Scene):
    def construct(self):
        text = TextMobject("This is some text")
        self.play(FadeInFromDown(text))
        self.wait()

class Position(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot()
        grid = NumberPlane() # To add a grid with coordinate axes
        Text1 = TextMobject("Text")
        Text2 = TextMobject("Text")

        # Absolute Position
        # - .to_edge() - UP, DOWN, LEFT, RIGHT
        # - .to_corner() - UR, UL, DR, DL
        # Both above commands have a buff parameter

        #dot.to_edge(RIGHT)
        #dot.to_corner(DR)

        # Relative Position
        # - .move_to()
        # - .next_to()
        # - .shift()

        Text1.move_to(2*UP+LEFT)
        Text2.move_to(2*DOWN+LEFT)

        #dot.move_to(ReferenceText.get_center() + 5*LEFT)
        # Moves the dot 5 units left of the reference text
        # The method .get_center() just returns the coordinates of the center of the object called

        dot1.next_to(Text1, LEFT) # Takes the coordinates of the edge of Text
        dot2.move_to(Text2.get_center() + LEFT) # Takes the coordinated of the center of the text


        self.add(grid, Text1, Text2, dot1, dot2)

        self.wait()

class ShiftingDot(Scene):
    def construct(self):
        dot = Dot()
        grid = NumberPlane()

        dot.move_to(2*UP+3*LEFT)

        self.add(dot, grid)
        self.wait()

        dot.shift(RIGHT)
        self.wait()
        dot.shift(RIGHT)
        self.wait()
        dot.shift(RIGHT)
        self.wait()
        dot.shift(RIGHT)
        self.wait()


        self.wait()

class RotatingText(Scene):
    def construct(self):
        text1 = TextMobject("Text")
        text2 = TextMobject("Reference Text")

        text1.shift(UP)

        self.add(text1, text2)
        self.wait()
        text1.rotate(PI/4)
        self.wait()
        text1.rotate(PI/4)
        self.wait()
        text1.rotate(PI/4)
        self.wait()
        text1.rotate(PI/4)
        self.wait()

class RotateAboutARef(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot()
        grid = NumberPlane()

        point = 2*UP + 3*RIGHT
        dot2.shift(2*DOWN)

        self.add(dot1, dot2, grid)

        self.wait()
        dot2.rotate(PI/3, about_point=point)
        self.wait()

class FlipSomeEggs(Scene):
    def construct(self):
        eggs = TextMobject("Eggs")
        eggs.flip(UP)

        self.play(Write(eggs))
        self.wait()

class WritingSomeMath(Scene):
    def construct(self):
        eqn = TexMobject(r"\frac{d}{dx}f(x) = \lim_{h\rightarrow 0}{\frac{f(x+h)-f(x)}{h}}")
        # Use TexMobject() to write Tex Equations
        
        eqn.scale(2) # Scaling up by 2 in size
        self.play(Write(eqn))

