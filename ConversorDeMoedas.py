#Conversor De Moedas
#Obs O Valor Do Dolar Era Do Dia 11/11/22 Que Estava Igual a US$ 1 = R$ 5,33

r = float(input("Quanto Dinheiro Você Tem Na Carteira? R$ "))
d = float(5.33)
total = float(r/d)
print("O Valor em Dolar e US$ {:.2f} ".format(total))