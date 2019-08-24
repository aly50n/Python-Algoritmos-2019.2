print("Calcule quantas carteiras cabem na sua sala de aula informando os dados a seguir:")
ls=float(input("Qual a largura da sua sala de aula em metros? "))
cs=float(input("Qual o comprimento da sua sala de aula em metros? "))
lc=float(input("Qual a largura de uma carteira em metros? "))
cc=float(input("Qual o comprimento de uma carteira em metros? "))
cts= (cs-1.5)+0.2
lts= ls+0.5
ctc= cc+0.2
ltc= lc+0.5
cpc= cts//ctc
cpl= lts//ltc
total= cpc*cpl
print("Na sua sala de aula cabem", total, "Carteiras.")

# Lengenda: cts= Comprimento total da sala, lts= Largura total da sala
#           ctc= comprimento total da carteira, ltc= largura total da carteira
#           cpc= cadeira por comprimento, cpl= cadeira por largura.