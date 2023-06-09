from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo : '))
seno = sin(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang,seno))
cosseno= cos(radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tan = tan(radians(ang))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ang, tan))
