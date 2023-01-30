from manim import *

class carrousel(Scene):
    def construct(self):
        
        cuadrado=Square().scale(1.25)
        elipse=Ellipse(width=4,height=2,color=RED).scale(1.25)
        circuloAzul=Circle(color=BLUE).scale(1.25)
        sector=Sector(outer_radius=2,inner_radius=0,fill_color=RED).scale(1.25)
        anillo=Annulus(outer_radius=0.6,inner_radius=0.3,color=YELLOW,fill_opacity=0.4).scale(1.25)
        equilatero=Triangle().scale(1.25)
        polregular=RegularPolygon(n=8).scale(1.25)
        
        self.play(Create(cuadrado))
        self.wait(2)
        self.play(ReplacementTransform(cuadrado,circuloAzul))
        self.wait(1)
        self.play(ReplacementTransform(circuloAzul,sector))
        self.wait(1)
        self.play(ReplacementTransform(sector,anillo))
        self.wait(1)
        self.play(ReplacementTransform(anillo,equilatero))
        self.wait(1)
        self.play(ReplacementTransform(equilatero,polregular))
        self.wait(4)
        
        
        