# python -m manim figures.py fig2 -ps
# Status: Published
# https://www.youtube.com/watch?v=EUg4Ib7nick

from manimlib.imports import *

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



class fig2(Scene):
	def construct(self):
		self.add_sound("audio4")
		self.wait()
		intro1=TextMobject("Proof of ")
		intro2=TexMobject(r"{ (a+b) }^{ 2 }=\quad { a }^{ 2 }+2ab+{ b }^{ 2 }")
		
		intro2.set_color_by_gradient(BLUE, PURPLE)
		self.play(Write(intro1))
		self.wait()
		self.play(ApplyMethod(intro1.shift, 1.5*LEFT))
		intro2.next_to(intro1, RIGHT)
		self.play(FadeIn(intro2))
		self.wait(3)
		self.play(FadeOut(intro1), FadeOutAndShiftDown(intro2))
		self.wait()


#LINE 1
#FIRST WHITE, THEN COLOR, PUT A(PINK), B(YELLOW)		
		line1a=Line(np.array([-2,2,0]), np.array([-1,2,0]))
		line1b=Line(np.array([-1,2,0]), np.array([2,2,0]))
		self.play(FadeIn(line1a), FadeIn(line1b))
		self.wait(1.5)
		line1a.set_color(PINK)
		line1b.set_color(YELLOW)
		text1a=TexMobject("a", color=PINK)
		text1b=TexMobject("b", color=YELLOW)
		text1a.next_to(line1a, UP)
		text1b.next_to(line1b, UP)
		self.play(GrowFromCenter(text1a), GrowFromCenter(text1b))
		self.wait()

# LINE 2, 3, 4(WHITE)
		line2=Line(np.array([2,2,0]), np.array([2,-2,0]))
		line3=Line(np.array([2,-2,0]), np.array([-2,-2,0]))
		line4=Line(np.array([-2,-2,0]), np.array([-2,2,0]))
		self.play(ShowCreation(line2))
		self.play(ShowCreation(line3))
		self.play(ShowCreation(line4))
		self.wait(2)
#LINE 5(WHITE)
		line5=Line(np.array([-1,2,0]), np.array([-1,-2,0]))
		self.play(ShowCreation(line5))
#LINE 3 COLOURING, PUT A, B
		line3a=Line(np.array([-2,-2,0]), np.array([-1,-2,0]))
		line3b=Line(np.array([-1,-2,0]), np.array([2,-2,0]))
		line3a.set_color(PINK)
		line3b.set_color(YELLOW)
		self.add(line3a, line3b)
		text3a=TexMobject("a", color=PINK)
		text3b=TexMobject("b", color=YELLOW)
		text3a.next_to(line3a, DOWN)
		text3b.next_to(line3b, DOWN)
		self.play(GrowFromCenter(text3a), GrowFromCenter(text3b))
		self.wait(2)
#LINE 6(WHITE)
		line6=Line(np.array([-2,1,0]), np.array([2,1,0]))
		self.play(ShowCreation(line6))
#LINE 2, 4 COLOURING AND LABELING
		line4a=Line(np.array([-2,2,0]), np.array([-2,1,0]))
		line4b=Line(np.array([-2,1,0]), np.array([-2,-2,0]))
		line4a.set_color(PINK)
		line4b.set_color(YELLOW)
		text4a=TexMobject("a", color=PINK)
		text4b=TexMobject("b", color=YELLOW)
		text4a.next_to(line4a, LEFT)
		text4b.next_to(line4b, LEFT)

		line2a=Line(np.array([2,2,0]), np.array([2,1,0]))
		line2b=Line(np.array([2,1,0]), np.array([2,-2,0]))
		line2a.set_color(PINK)
		line2b.set_color(YELLOW)
		text2a=TexMobject("a", color=PINK)
		text2b=TexMobject("b", color=YELLOW)
		text2a.next_to(line2a, RIGHT)
		text2b.next_to(line2b, RIGHT)
		self.add(line2a, line2b, line4a, line4b)
		self.play(GrowFromCenter(text2a), GrowFromCenter(text2b), GrowFromCenter(text4a), GrowFromCenter(text4b))
		self.wait(3)
#a^2
		a2square=Polygon(np.array([-2,2,0]), np.array([-1,2,0]), np.array([-1,1,0]), np.array([-2,1,0]), fill_color=PINK, fill_opacity=1)		
		a2text=TexMobject("{ a }^{ 2 }", color=BLACK)
		a2text.move_to(1.5*LEFT + 1.5*UP)
		self.add(a2square, line1a, line4a, a2text)
		self.wait(1.5)

#b^2
		b2square=Polygon(np.array([-1,1,0]), np.array([2,1,0]), np.array([2,-2,0]), np.array([-1,-2,0]), fill_color=YELLOW, fill_opacity=1)
		b2text=TexMobject("{ b }^{ 2 }", color=BLACK)
		b2text.move_to(0.5*RIGHT + 0.5*DOWN)
		self.add(b2square, line2b, line3b, b2text)
		self.wait(1.5)
#ab1rectangle
		ab1rectangle=Polygon(np.array([-1,2,0]), np.array([2,2,0]), np.array([2,1,0]), np.array([-1,1,0]), fill_color=[PINK, YELLOW], fill_opacity=1)
		ab1text=TexMobject("ab", color=BLACK)
		ab1text.move_to(0.5*RIGHT + 1.5*UP)
		self.add(ab1rectangle, line2a, line1b, ab1text)
		self.wait(1.5)
#ab2rectangle
		ab2rectangle=Polygon(np.array([-2,1,0]), np.array([-1,1,0]), np.array([-1,-2,0]), np.array([-2,-2,0]), fill_color=[PINK, YELLOW], fill_opacity=1)
		ab2text=TexMobject("ba", color=BLACK)
		ab2text.move_to(1.5*LEFT + 0.5*DOWN)
		self.add(ab2rectangle, line4b, line3a, ab2text)
		self.wait(3)

#
		a2textc=TexMobject("{ a }^{ 2 } +", color=BLUE)
		abtextc=TexMobject(" ab + ba", color=BLUE)
		b2textc=TexMobject(" + { b }^{ 2 }", color=BLUE)
		ab2final=TexMobject("2ab", color=BLUE)

		question=TexMobject(r"{ (a\quad +\quad b) }^{ 2 } =", color=RED)

		a2textc.move_to(3.5*RIGHT + 2*UP)
		abtextc.next_to(a2textc, RIGHT)
		b2textc.next_to(abtextc, RIGHT)
		question.move_to(4.5*RIGHT + 3*UP)
		ab2final.move_to(4.9*RIGHT + 2*UP)
		self.play(FadeInFromDown(question))
		self.wait(2)
#
		self.play(ReplacementTransform(a2text.copy(), a2textc), ReplacementTransform(ab1text.copy(), abtextc), ReplacementTransform(ab2text.copy(), abtextc), ReplacementTransform(b2text.copy(), b2textc))
		self.wait(2)
		self.play(ReplacementTransform(abtextc, ab2final))
		self.wait(2)
		self.play(*[FadeOut(mob)for mob in self.mobjects])
		self.wait()
		



		













		




