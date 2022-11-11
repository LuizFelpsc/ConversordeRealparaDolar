#Conversor De Moedas
#Obs O Valor Do Dolar Era Do Dia 11/11/22 Que Estava Igual a US$ 1 = R$ 5,33

r = float(input("Digite o Valor Que Deseja Converter em Dolar? R$ "))
d = float(5.33)
total = float(r/d)
print("Com R$ {:.2f} Você Compra US$ {:.2f} ".format(r,total))