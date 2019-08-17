print("Calculador de média de Combustível por Quilômetro")
ki=int(input("Informe qual era a quilometragem no inicio do percurso-> "))
kf=int(input("Agora informe qual foi a quilometragem no final do percurso-> "))
l=int(input("Quantos litros de combustível foram gastos no percurso? "))
kl=(kf-ki)//l
resultado=str ("Quilômetro(s) percorrido(s).")
print("O seu veículo gasta 1 Litro de combustível a cada", kl, resultado)