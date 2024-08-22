# Program to determine how much must be paid, given the quantity of gasoline
# to be purchased and the price of gasoline in cents
# per Liter.


g=eval (input("Favor de entrar la cantidad de galones de gasolina deseados:  "))
c=eval (input("Favor de entrar el precio de la gasolina en centavos por Litro:  "))

h=g*c*0.03785411784

h=round(h,2)

print("Favor de pagar:  $",h)

input()