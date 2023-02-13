from manim import *

class productofrac(Scene):
    def construct(self):

        #Elementos
        producto1 = MathTex(r"{a}", "\over","{b}").move_to(1.5*LEFT)
        punto = MathTex(r"\cdot").next_to(producto1,RIGHT).scale(2)
        producto2 = MathTex(r"{c}", "\over","{d}").next_to(punto,RIGHT)
        igual= MathTex(r"=").next_to(producto2,RIGHT)
        titulo = Title(f"Producto de FRACCIONES")
        producto = MathTex(r"{a\cdot c}", "\over","{b\cdot d}").next_to(igual,RIGHT)
        producto1_aux1 = MathTex(r"{a}", "\over","{b}",color=RED)
        producto2_aux1 = MathTex(r"{c}", "\over","{d}",color=RED)
        producto1_aux1[0].next_to(producto1[0],UP) 
        producto2_aux1[0].next_to(producto2[0],UP) 
        producto1_aux1[2].next_to(producto1[2],DOWN) 
        producto2_aux1[2].next_to(producto2[2],DOWN) 
        numerador=VGroup(producto1_aux1[0],producto2_aux1[0]) 
        denominador=VGroup(producto1_aux1[2],producto2_aux1[2]) 

        #Animación
        self.play(FadeIn(titulo))
        self.wait(1)
        
        self.play(Write(producto1))
        self.play(Write(punto))
        self.play(Write(producto2))
        self.play(Write(igual))
        self.play(Write(producto[1]))
        self.wait(1)
        self.play(Write(producto1_aux1[0]),Write(producto2_aux1[0]))
        self.wait(1)
        self.play(Transform(numerador,producto[0]))
        self.wait(1)
        self.play(Write(producto1_aux1[2]),Write(producto2_aux1[2]))
        self.wait(1)
        self.play(Transform(denominador,producto[2]))
        self.wait(5)