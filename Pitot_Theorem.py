# python -m manim Pitot_Theorem.py fig -pm

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


class fig(Scene):
    def construct(self):
    	self.add_sound("audio6")
    	#intro
    	intro1=TextMobject("Proof of")
    	intro1.scale(2)

    	intro2=TextMobject("Pitot Theorem")
    	intro2.scale(2)
    	intro2.set_color_by_gradient(RED, GREEN)

    	intro3=TextMobject("In a quadrilateral circumscribed around a circle, the \\\\ sum of two"," opposite sides", " equals to the sum of two \\\\ remaining (and opposite) sides")
    	intro3.set_color(YELLOW)
    	intro3[1].set_color(BLUE)
    	intro3.scale(1.2)

    	self.wait(1.5)
    	self.play(Write(intro1))
    	self.wait(2)
    	self.play(ReplacementTransform(intro1, intro2))
    	self.wait(2)

    	self.play(ApplyMethod(intro2.shift, 3*UP+3.7*LEFT))
    	self.play(Write(intro3), run_time=6)

    	self.wait(4)
    	self.play(FadeOut(intro3), FadeOut(intro2))
    	self.wait(1.5)


    	#Defining & adding circle, polygon
    	circle=Circle(radius=2, color=WHITE)
    	polygon=Polygon(np.array([0.392,2.436,0]), np.array([-1.78,1.35,0]), np.array([-2.45,-2,0]), np.array([4.828,-2,0]))
    	self.play(ShowCreation(polygon), run_time=5)
    	self.wait(2)
    	self.play(ShowCreation(circle))
    	self.wait(3)

    	#Displaying Vertex A, B, C, D
#    	vertex=TextMobject("A", "B", "C", "D")
 #   	vertex[0].move_to(0.392*RIGHT + 2.67*UP)
 #   	vertex[1].move_to(2.1*LEFT + 1.35*UP)
  #  	vertex[2].move_to(2.45*LEFT + 2.3*DOWN)
   # 	vertex[3].move_to(4.828*RIGHT + 2.3*DOWN)
    #	self.play(Write(vertex))

    	#line making
    	line1a=Line(np.array([0.392,2.436,0]), np.array([-0.89,1.795,0]))
    	line1b=Line(np.array([-1.78,1.35,0]), np.array([-0.89,1.795,0]))

    	line2a=Line(np.array([-1.78,1.35,0]), np.array([-1.97,0.4,0]))
    	line2b=Line(np.array([-2.45,-2,0]), np.array([-1.97,0.4,0]))

    	line3a=Line(np.array([-2.45,-2,0]), np.array([0,-2,0]))
    	line3b=Line(np.array([4.828,-2,0]), np.array([0,-2,0]))

    	line4a=Line(np.array([4.828,-2,0]), np.array([1.4437,1.3841,0]))
    	line4b=Line(np.array([0.392,2.436,0]), np.array([1.4437,1.3841,0]))

    	#line coloring

    	line1a.set_color(RED)
    	line4b.set_color(RED)

    	line1b.set_color(BLUE)
    	line2a.set_color(BLUE)

    	line2b.set_color(GREEN)
    	line3a.set_color(GREEN)

    	line3b.set_color(YELLOW)
    	line4a.set_color(YELLOW)

    	#Line displaying

    	self.play(ShowCreation(line1a),
    	ShowCreation(line1b),
    	ShowCreation(line2a),
    	ShowCreation(line2b),
    	ShowCreation(line3a),
    	ShowCreation(line3b),
    	ShowCreation(line4a),
    	ShowCreation(line4b), run_time=2.5 )
    	self.remove(polygon)
    	

    	#line labelling
		#					0			1			2		3		  4			5			6			7	   8
    	label=TexMobject(r"\alpha", r"\alpha", r"\beta",r"\beta", r"\gamma", r"\gamma", r"\delta", r"\delta", "")

    		# coloring
    	label[0].set_color(RED)
    	label[1].set_color(RED)

    	label[2].set_color(BLUE)
    	label[3].set_color(BLUE)

    	label[4].set_color(GREEN)
    	label[5].set_color(GREEN)

    	label[6].set_color(YELLOW)
    	label[7].set_color(YELLOW)

    		#positioning
    	label[0].next_to(line1a, UP)		#alpha
    	label[1].next_to(line4b, UP)		#alpha

    	label[2].next_to(line1b, UP)		#beta
    	label[3].next_to(line2a, LEFT)		#beta

    	label[4].next_to(line2b, LEFT)		#gamma
    	label[5].next_to(line3a, DOWN)		#gamma

    	label[6].next_to(line3b, DOWN)		#delta
    	label[7].move_to(3.3*RIGHT)			#delta

    		#displaying
    	self.play(Write(label[0]), 
    		Write(label[1]), 
    		Write(label[2]), 
    		Write(label[3]), 
    		Write(label[4]),
    		Write(label[5]),
    		Write(label[6]),
    		Write(label[7]))
    	self.wait(4)
    	


    	#Solution

    	# ...............Part 1....................

    	#text creation & positioning
    	text=TextMobject("Sum of opposite sides =")
    	text.to_edge(RIGHT)
    	text.scale(1.2)
    	
    	# Shifting Everything
    	self.play(ApplyMethod(circle.shift, 4*LEFT), 
    		ApplyMethod(line1a.shift, 4*LEFT), 
    		ApplyMethod(line1b.shift, 4*LEFT), 
    		ApplyMethod(line2a.shift, 4*LEFT), 
    		ApplyMethod(line2b.shift, 4*LEFT), 
    		ApplyMethod(line3a.shift, 4*LEFT), 
    		ApplyMethod(line3b.shift, 4*LEFT),
    		ApplyMethod(line4a.shift, 4*LEFT), 
    		ApplyMethod(line4b.shift, 4*LEFT),
    		ApplyMethod(label.shift, 4*LEFT),
    		FadeInFromDown(text))
    	self.wait(2)
    	

    	#alpha beta gamma delta
    	#				     0       1       2       3       4	  5	   6       7       8       9        10
    	solution1=TexMobject("(" ,r"\alpha", "+" , r"\beta", ")", "+", "(" ,r"\gamma", "+" , r"\delta", ")")
    	solution1[1].set_color(RED)
    	solution1[3].set_color(BLUE)
    	solution1[7].set_color(GREEN)
    	solution1[9].set_color(YELLOW)
    	solution1.next_to(text, DOWN)
    	#self.play(GrowFromPoint(line1a))
    	self.play(WiggleOutThenIn(line1a), WiggleOutThenIn(line1b), WiggleOutThenIn(line3a), WiggleOutThenIn(line3b), run_time=3)

    	self.play(ReplacementTransform(label[0].copy(), solution1[1]), ReplacementTransform(label[2].copy(), solution1[3]), run_time=2.5)
    	self.play(FadeInFromDown(solution1[0:5:2]))
    	self.wait()
    	self.play(ReplacementTransform(label[5].copy(), solution1[7]), ReplacementTransform(label[6].copy(), solution1[9]), run_time=2.5)
    	self.play(FadeInFromDown(solution1[6:11:2]), FadeInFromDown(solution1[5]))
    	self.wait(2)

    	# ...............Part 2....................

    	#				     0       1       2       3       4	  5	   6       7       8       9        10	 11
    	solution2=TexMobject("(" ,r"\beta", "+" , r"\gamma", ")", "+", "(" ,r"\alpha", "+" , r"\delta", ")", "")
    	solution2.next_to(text, DOWN)
    	solution2[7].set_color(RED)
    	solution2[1].set_color(BLUE)
    	solution2[3].set_color(GREEN)
    	solution2[9].set_color(YELLOW)

    	self.play(ReplacementTransform(solution1[1:4], solution2[1:4]), ReplacementTransform(solution1[7:10], solution2[7:10]) )
    	self.wait(2)

    	# ...............Part 3....................

    	self.play(WiggleOutThenIn(line2a), WiggleOutThenIn(line2b), WiggleOutThenIn(line4a), WiggleOutThenIn(line4b), run_time=3)
    	self.wait()
    	self.play(Transform(solution2[0:5].copy(), label[3:5]), run_time=2.5)
    	self.play(Transform(solution2[6:11].copy(), label[1:8:6]), run_time=2.5)
    	self.wait(4)
    	self.play(*[FadeOut(mob)for mob in self.mobjects])
    	self.wait()




# python -m manim Pitot_Theorem.py fig2 -pm





    	


        