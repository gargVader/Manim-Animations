# python -m manim Pythagoras_Theorem.py fig -pm
#Status: Published
# https://youtu.be/KNhyMjZLtNY

from manimlib.imports import *


# REMOVE ALL OBJECTS FROM THE SCREEN
class RemoveAllObjectsInScreen(Scene):
    def construct(self):
        self.add(
            VGroup(
                *[
                    VGroup(
                        *[
                            Dot()
                            for i in range(30)
                        ]
                    ).arrange_submobjects(RIGHT)
                    for j in range(10)
                ]
            ).arrange_submobjects(DOWN)
        )


# Animation Starts

class fig(Scene):
	def construct(self):
		self.add_sound("audio5")
		intro=TextMobject("Proof of ")
		intro.scale(2)
		intro2=TextMobject("Pythagoras Theorem")
		intro2.set_color_by_gradient(BLUE, GREEN)
		intro2.scale(2)
		self.wait(1.5)
		self.play(Write(intro))
		self.wait(3)
		self.play(Transform(intro, intro2))
		self.wait(4)
		self.play(FadeOut(intro))
		self.wait(3)
#LINE 1
		line1a=Line(np.array([-2,2,0]), np.array([-1,2,0]))
		line1b=Line(np.array([-1,2,0]), np.array([2,2,0]))
		self.play(FadeIn(line1a), FadeIn(line1b))
		self.wait(1.5)
		line1a.set_color(RED2)
		line1b.set_color(BLUE)
		text1a=TexMobject("a", color=RED2)
		text1b=TexMobject("b", color=BLUE)
		text1a.next_to(line1a, UP)
		text1b.next_to(line1b, UP)
		self.play(GrowFromCenter(text1a), GrowFromCenter(text1b))
		self.wait(2)

# LINE 2, 3, 4(WHITE)
		line2=Line(np.array([2,2,0]), np.array([2,-2,0]))
		line3=Line(np.array([2,-2,0]), np.array([-2,-2,0]))
		line4=Line(np.array([-2,-2,0]), np.array([-2,2,0]))
		self.play(ShowCreation(line2))
		self.play(ShowCreation(line3))
		self.play(ShowCreation(line4))
		self.wait(2)

#Line 4 colouring, Line 5

		line4a=Line(np.array([-2,-2,0]), np.array([-2,-1,0]))
		line4b=Line(np.array([-2,-1,0]), np.array([-2,2,0]))
		line4a.set_color(RED2)
		line4b.set_color(BLUE)
		self.add(line4a, line4b)
		text4a=TexMobject("a", color=RED2)
		text4b=TexMobject("b", color=BLUE)
		text4a.next_to(line4a, LEFT)
		text4b.next_to(line4b, LEFT)
		self.play(GrowFromCenter(text4a), GrowFromCenter(text4b))
		self.wait(2)

		line5=Line(np.array([-1,2,0]), np.array([-2,-1,0]))
		line5.set_color(GREEN2)
		self.play(ShowCreation(line5))
		text5c=TextMobject("c", color=GREEN2)
		text5c.move_to(1*LEFT + 1*UP)
		self.wait()
		self.play(GrowFromCenter(text5c))
		self.wait(2.5)	

# LINE 3 COLOURING, Line 6

		line3a=Line(np.array([1,-2,0]), np.array([2,-2,0]))
		line3b=Line(np.array([-2,-2,0]), np.array([1,-2,0]))
		line3a.set_color(RED2)
		line3b.set_color(BLUE)
		self.add(line3a, line3b)
		text3a=TexMobject("a", color=RED2)
		text3b=TexMobject("b", color=BLUE)
		text3a.next_to(line3a, DOWN)
		text3b.next_to(line3b, DOWN)
		self.play(GrowFromCenter(text3a), GrowFromCenter(text3b))
		self.wait(2)

		line6=Line(np.array([-2,-1,0]), np.array([1,-2,0]))
		line6.set_color(GREEN2)
		self.play(ShowCreation(line6))
		text6c=TextMobject("c", color=GREEN2)
		text6c.move_to(1*LEFT + 1*DOWN)
		self.play(GrowFromCenter(text6c))
		self.wait(2)

#Line 2 colouring, Line 7
		line2a=Line(np.array([2,2,0]), np.array([2,1,0]))
		line2b=Line(np.array([2,1,0]), np.array([2,-2,0]))
		line2a.set_color(RED2)
		line2b.set_color(BLUE)
		self.add(line2a, line2b)
		text2a=TexMobject("a", color=RED2)
		text2b=TexMobject("b", color=BLUE)
		text2a.next_to(line2a, RIGHT)
		text2b.next_to(line2b, RIGHT)
		self.play(GrowFromCenter(text2a), GrowFromCenter(text2b))
		self.wait(2)	

		line7=Line(np.array([1,-2,0]), np.array([2,1,0]))
		line7.set_color(GREEN2)
		self.play(ShowCreation(line7))
		text7c=TextMobject("c", color=GREEN2)
		text7c.move_to(1.4*RIGHT)
		self.play(GrowFromCenter(text7c))	

#Line 8
		
		line8=Line(np.array([2,1,0]), np.array([-1,2,0]))
		line8.set_color(GREEN2)
		self.play(ShowCreation(line8))
		text8c=TextMobject("c", color=GREEN2)
		text8c.move_to(1.4*UP)
		self.play(GrowFromCenter(text8c))

		triangle1=Polygon(np.array([-1,2,0]), np.array([-2,2,0]), np.array([-2,-1,0]), fill_color=[RED2, BLUE], fill_opacity=1)
		triangle2=Polygon(np.array([-2,-1,0]), np.array([-2,-2,0]), np.array([1,-2,0]), fill_color=[RED2, BLUE], fill_opacity=1)
		triangle3=Polygon(np.array([1,-2,0]), np.array([2,-2,0]), np.array([2,1,0]), fill_color=[RED2, BLUE], fill_opacity=1)
		triangle4=Polygon(np.array([2,1,0]), np.array([2,2,0]), np.array([-1,2,0]), fill_color=[RED2, BLUE], fill_opacity=1)
		square=Polygon(np.array([2,1,0]), np.array([1,-2,0]), np.array([-2,-1,0]), np.array([-1,2,0]), fill_color=GREEN2, fill_opacity=1)

#TEXT ON DIAGRAM
		#TEXT CREATION
		triangletext1=TexMobject(r"\frac { 1 }{ 2 } ab", color=BLACK)
		triangletext2=TexMobject(r"\frac { 1 }{ 2 } ab", color=BLACK)
		triangletext3=TexMobject(r"\frac { 1 }{ 2 } ab", color=BLACK)
		triangletext4=TexMobject(r"\frac { 1 }{ 2 } ab", color=BLACK)
		squaretext=TexMobject(r"{ c }^{ 2 }", color=BLACK)
		triangletext1.scale(0.5)
		triangletext2.scale(0.5)
		triangletext3.scale(0.5)
		triangletext4.scale(0.5)
		squaretext.scale(1.2)

		#TEXT POSITIONING
		triangletext1.move_to(1.6*LEFT + 1.5*UP)
		triangletext2.move_to(1.6*LEFT + 1.5*DOWN)
		triangletext3.move_to(1.6*RIGHT + 1.5*DOWN)
		triangletext4.move_to(1.6*RIGHT + 1.6*UP)
		#TEXT DISPLAY

		#TRIANGLE DISPLAY
		self.wait(2)
		self.play(WiggleOutThenIn(triangle1), WiggleOutThenIn(triangle2), WiggleOutThenIn(triangle3), WiggleOutThenIn(triangle4), run_time=3)
		self.add(line1a, line1b, line2a, line2b,line3a, line3b, line4a, line4b)
		self.wait(2)
		self.play(ReplacementTransform(triangle1.copy(), triangletext1), ReplacementTransform(triangle2.copy(), triangletext2), ReplacementTransform(triangle3.copy(), triangletext3), ReplacementTransform(triangle4.copy(), triangletext4))
		#SQUARE DISPLAY
		self.wait(3)
		self.play(WiggleOutThenIn(square))
		self.wait(2)
		self.play(ReplacementTransform(square.copy(), squaretext))
		self.wait(2)
#solution a
# (a+b)^2 = a^2 + 2ab + b^2

		#CREATION
		solna1=TextMobject("Total Area=", color=RED)
		solna2=TexMobject(r"{ (a+b) }^{ 2 }", color=BLUE)
		solna3=TexMobject(r"{ a }^{ 2 }", "+", "2ab", r"+{ b }^{ 2 }", color=BLUE)
		#POSITIONING
		solna1.move_to(4.5*RIGHT + 3.5*UP)
		solna2.next_to(solna1, DOWN)
		solna3.next_to(solna1, DOWN)
		#DISPLAY
		self.play(FadeInFromDown(solna1))
		self.wait()
		self.play(Write(solna2))
		self.wait(2.5)
		self.play(ReplacementTransform(solna2, solna3))
		self.wait(3)

#solution b 
		solnb1=TextMobject("Total Area=", color=RED)
		solnb2=TexMobject(r"4(\frac { 1 }{ 2 } ab)", "+", "{ c }^{ 2 }", color=BLUE)
		solnb3=TexMobject("2ab", color=BLUE)

		solnb1.next_to(solna2, DOWN, buff=1)
		solnb2.next_to(solnb1, DOWN)
		solnb3.next_to(solnb2[1], LEFT)

		self.play(FadeInFromDown(solnb1))
		self.wait()
		self.play(ReplacementTransform(triangletext1.copy(), solnb2[0]), ReplacementTransform(triangletext2.copy(), solnb2[0]), ReplacementTransform(triangletext3.copy(), solnb2[0]), ReplacementTransform(triangletext4.copy(), solnb2[0]))
		self.play(ReplacementTransform(squaretext.copy(), solnb2[2]), Write(solnb2[1]))
		self.wait(2)
		self.play(ReplacementTransform(solnb2[0], solnb3))
		self.wait(3)
#coloring
		solna3.set_color(YELLOW)
		solnb2.set_color(YELLOW)
		solnb3.set_color(YELLOW)
		equal=TexMobject("=", color=YELLOW)
		self.wait(4)

		self.remove(solna1, solnb1)
		self.wait(2)
		solna3.scale(0.8)
		solnb2.scale(0.8)
		solnb3.scale(0.8)
		equal.scale(0.8)
		
#final shifting
		self.play(ApplyMethod(solnb3.shift, 1.04*RIGHT), ApplyMethod(solnb2[1].shift, 1.04*RIGHT), ApplyMethod(solnb2[2].shift, 1.04*RIGHT))
		equal.next_to(solnb3, LEFT)
		self.add(equal)
		self.play(ApplyMethod(solna3.shift, 2.3*DOWN + 1.2*LEFT))

		solna3[2].set_color(ORANGE)
		solnb3.set_color(ORANGE)
		self.wait(3)

		self.play(FadeOutAndShiftDown(solnb3), FadeOutAndShiftDown(solnb2[1]) , FadeOutAndShiftDown(solna3[1]), FadeOutAndShiftDown(solna3[2]))
		self.play(ApplyMethod(solna3[0].shift, 1*RIGHT), ApplyMethod(solnb2[2].shift, 1.3*LEFT))
		self.wait(5)
		self.play(*[FadeOut(mob)for mob in self.mobjects])
		self.wait()


		



		
