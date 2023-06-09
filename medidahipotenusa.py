from math import hypot
co = float(input('Comprimento do cateto oposto '))
ca = float(input('Comprimento do cateto adjacente '))
hip = hypot(ca,co)
print('A medida da hipotenusa é {:.2}'.format(hip))
