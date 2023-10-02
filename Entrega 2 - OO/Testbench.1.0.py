from my_libraries.shapes2D import Ponto,Circulo,Retangulo,Triangulo,Linha
from my_libraries.coordsystem import PlanoCartesiano

def Workspace():
    dashboard = PlanoCartesiano()
    p1 = Ponto(1.0,1.0)
    l1 = Linha(-5.0,-4.0,-20.0,12.0)
    c1 = Circulo(2.0,2.0,8.0)
    r1 = Retangulo(Linha(1.0,0,1.0,5.0),Linha(1.0,0,10.0,0))
    t1 = Triangulo(6.0,4.0,9.0,2.0,15.0,7.0)

    #Uso de métodos do ponto
    p1.Quadrante(p1.x0,p1.y0)
    p1.PontoCircunscrito(p1.x0,p1.y0,c1.centro,c1.raio)
    p1.Coordenadas(p1.x0,p1.y0)
    print(f"A distância do ponto até a origem é de: {p1.Distancia(p1.x0,p1.y0):,.2f}")

    #Uso de métodos da Linha
    print(f"Essa linha possui comprimento = {l1.Comprimento(l1.x0,l1.y0,l1.x1,l1.y1):,.2f}")

    #Uso de métodos do Retângulo
    print(f"O perímetro do retângulo é de {r1.Perimetro(r1.linha1,r1.linha2):,.2f}")
    print(f"A área do retângulo é de {r1.Area(r1.linha1,r1.linha2):,.2f}")

    #Uso de métodos do Círculo
    print(f"A área desse círculo é de {c1.Area(c1.raio):,.2f}")
    print(f"A circunfêrencia do círculo é de {c1.Circunferencia(c1.raio):,.2f}")

    #Uso de métodos do Triângulo
    print(f"Esse é um triângulo {t1.Tipo(t1.l0,t1.l1,t1.l2)}")
    print(f"A área desse triângulo é de {t1.Area(t1.l0,t1.h):,.2f}")
    print(f"O perímetro desse triângulo é de {t1.Perimetro(t1.l0,t1.l1,t1.l2):,.2f}")

    #Uso de métodos do Plano Cartesiano
    dashboard.InserirFormas(p1,l1,c1,r1,t1)
    dashboard.MostrarFormas()
    dashboard.RemoverFormas(l1,r1,t1)
    print("\nLista Atualizada")
    dashboard.MostrarFormas()
    dashboard.QuantidadeDeFormas()

Workspace()