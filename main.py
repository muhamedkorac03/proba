import turtle


def mnogougao(n, duzina_stranice):
    for i in range(n):
        turtle.forward(duzina_stranice)
        turtle.left(360 / n)


mnogougao(6, 50)
