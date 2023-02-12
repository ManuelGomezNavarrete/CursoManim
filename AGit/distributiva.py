from manim import *

class Distributiva(Scene):

    def construct(self):

        titulo=Title("Propiedad DISTRIBUTIVA")

        eqn0 = MathTex(r"a","\cdot", "(","b","+","c",")=", "a","\cdot","b","+","a","\cdot","c").scale(1.5)
        eqn1 = MathTex(r"a","\cdot", "(","b","+","c",")=", "a","\cdot","b","+","a","\cdot","c").move_to(UP).scale(1.5)
        eqn2 = MathTex(r"a","\cdot", "(","b","+","c",")=", "a","\cdot","b","+","a","\cdot","c").scale(1.5)
        eqn2bis = MathTex(r"a","\cdot", "(","b","+","c",")=", "a","\cdot","b","+","a","\cdot","c").scale(1.5)
        eqn1bis = MathTex(r"a","\cdot", "(","b","+","c",")=", "a","\cdot","b","+","a","\cdot","c").move_to(UP).scale(1.5)
        eqn1.color=RED
        eqn1bis.color=RED

        self.play(FadeIn(titulo))
        self.play(Write(eqn0[:7]),Write(eqn2[:7]))
        self.wait()
        self.play(Write(eqn0[8]),Write(eqn2[10]),Write(eqn2[12]))
        self.wait()
        self.play(ReplacementTransform(eqn2[0],eqn1[0]),ReplacementTransform(eqn2[3],eqn1[3]),run_time=1)
        self.wait()
        self.play(ReplacementTransform(eqn1[0],eqn1[7]),ReplacementTransform(eqn1[3],eqn1[9]),run_time=1)
        self.wait()
        self.play(ReplacementTransform(eqn1[7],eqn2[7]),ReplacementTransform(eqn1[9],eqn2[9]),run_time=1)
        self.wait(2)
        self.play(ReplacementTransform(eqn2bis[0],eqn1bis[0]),ReplacementTransform(eqn2bis[5],eqn1bis[5]),run_time=1)
        self.wait()
        self.play(ReplacementTransform(eqn1bis[0],eqn1bis[11]),ReplacementTransform(eqn1bis[5],eqn1bis[13]),run_time=1)
        self.wait()
        self.play(ReplacementTransform(eqn1bis[11],eqn2bis[11]),ReplacementTransform(eqn1bis[13],eqn2bis[13]),run_time=1)
        self.wait(2)
        
       
       
       