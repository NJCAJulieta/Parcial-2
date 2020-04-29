Estado_Proyecto = []
Departamento = []
Municipio= []
Cliente= []
Direccion = []
Telefono = []

for x in range(5):
    codigo = input("Codigo del Cliente "+str(x) + "  : ")
    codigos.append(codigo)
    proyectos = input("Nombre del proyecto "+str(x) + "  : ")
    proyecto.append(proyectos)
    Estados_Proyectos = input("Estado del Proyecto "+str(x) + "  : ")
    Estado_Proyecto.append(Estados_Proyectos)
    Departamentos = input("Departamento "+str(x) + "  : ")
    Departamento.append(Departamentos)
    Municipios = input("Municipio "+str(x) + "  : ")
    Municipio.append(Municipios)
    Clientes = input("Nombre del Cliente " + str(x) + "  : ")
    Cliente.append(Clientes)
    Direcciones = input("Direccion del Cliente " + str(x) + "  : ")
    Direccion.append(Direcciones)
    Telefonos = input("Numero de Telefono " + str(x) + "  : ")
    Telefono.append(Telefonos)

print('{:<30} {:<22} {:<23} {:<25} {:<15} {:<23} {:<25} {:<15}'.format("\n\nCodigo", "proyecto", "Estado_Proyecto", "Departamento", "Municipio", "Cliente", "Direccion", "Telefono"))
for x in range(5):
    print('{:<25} {:<26} {:<20} {:<30} {:<5} {:<20} {:<30} {:<5}'.format(codigos[x], proyecto[x], Estado_Proyecto[x], Departamento[x], Municipio[x], Cliente[x], Direccion[x], Telefono[x] ))