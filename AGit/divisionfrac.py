from manim import *

class divisionfrac(Scene):
    def construct(self):

        #Elementos
        dividendo = MathTex(r"{a}", "\over","{b}").move_to(1.5*LEFT)
        dospuntos = MathTex(r"\div").next_to(dividendo,RIGHT)
        divisor = MathTex(r"{c}", "\over","{d}").next_to(dospuntos,RIGHT)
        igual= MathTex(r"=").next_to(divisor,RIGHT)
        titulo = Title(f"División de FRACCIONES")
        cociente = MathTex(r"{a\cdot d}", "\over","{b\cdot c}").next_to(igual,RIGHT)
        dividendo_aux1 = MathTex(r"{a}", "\over","{b}",color=RED).move_to(1.5*LEFT)
        divisor_aux1 = MathTex(r"{c}", "\over","{d}",color=RED).next_to(dospuntos,RIGHT)
        dividendo_aux1[0].next_to(dividendo[0],UP) 
        divisor_aux1[0].next_to(divisor[0],UP)
        dividendo_aux1[2].next_to(dividendo[2],DOWN) 
        divisor_aux1[2].next_to(divisor[2],DOWN) 
        numerador=VGroup(dividendo_aux1[0],divisor_aux1[2]) 
        denominador=VGroup(dividendo_aux1[2],divisor_aux1[0]) 

        #Animación
        self.play(FadeIn(titulo))
        self.wait(1)
        
        self.play(Write(dividendo))
        self.play(Write(dospuntos))
        self.play(Write(divisor))
        self.play(Write(igual))
        self.play(Write(cociente[1]))
        self.wait(1)
        self.play(Write(dividendo_aux1[0]),Write(divisor_aux1[2]))
        self.wait(1)
        self.play(Transform(numerador,cociente[0]))
        self.wait(1)
        self.play(Write(dividendo_aux1[2]),Write(divisor_aux1[0]))
        self.wait(1)
        self.play(Transform(denominador,cociente[2]))
        self.wait(4)