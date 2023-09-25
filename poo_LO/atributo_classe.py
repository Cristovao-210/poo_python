
'''
Os atributos/variáveis de classe tem o seu valor disponível para todas as instâncias da classe.
No entanto, pertecem a classe e não a instância.
Se forem alteradas dentro de uma instância, essa alteração não impactará no valor das outras instâncias.
Quando são alteradas em uma instância é como se tornassem um variável local da instância.
Para alterar o valor do atributo para todas as instâncias é necessário usar a classe diretamente, sem instanciá-la.

'''

class A:
    vc = 123


a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)

print("Alterando o valor para todas a instâncias: ")

A.vc = 369 # Usar a classe diretamente

print(a1.vc)
print(a2.vc)
print(A.vc)

print("Alterando o valor apenas na instância: ")

a1.vc = 456

print(a1.vc) # só altera nessa instância. Como se fosse uma variável local.
print(a2.vc)
print(A.vc)

class B:
    xy = 987

    # Quando o mesmo atributo/variável é criano na classe e no construtor/inicializador da classe, 
    # ela terá o valor do inicializador/construtor nas instâncias e o valor 'global' apenas se for chamada diretamente pela classe

    def __init__(self): 
        self.xy = 111

b1 = B()
b2 = B()

print("VALOR DE B NAS INSTÂNCIAS")
print(b1.xy)
print(b2.xy)
print("\nVALOR DE B DIRETAMENTE NA CLASSE")
print(B.xy)

print("\nALTERANDO O VALOR DE B NAS INSTÂNCIAS")

b1.xy = 'ALTERADO INSTÂNCIA B1'
print(b1.xy)
print("b2: ",b2.xy)

print("\nATERANDO O VALOR DE B NA CLASSE")

B.xy = 'ALTERADO NA CLASSE'
print(B.xy)

print("\nVerificando se ao alterar na classe altera nas instâncias")
print(b1.xy)
print(b2.xy)

print("\nUsando o valor da classe combinado com da instância")

B.xy = 2
b1.xy = 4

b2.xy = B.xy * b1.xy

print(f'{b1.xy} x {B.xy} = {b2.xy}')
