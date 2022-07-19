import xlrd

arquivo=xlrd.open_workbook("basededados.xls")
planilha1=arquivo.sheet_by_name("01")
planilha2=arquivo.sheet_by_name("01(2)")

idPlanilha1=planilha1.col_values(0)
idPlanilha2=planilha2.col_values(0)
nomesPlanilha1=planilha1.col_values(1)
nomesPlanilha2=planilha2.col_values(1)
salarioPlanilha1=planilha1.col_values(2)
salarioPlanilha2=planilha2.col_values(2)

totalPlanilha1 = 0
totalPlanilha2 = 0
print("---------------RELATÓRIO--------------")
print("\nColaboradores que estão com o salário errado | Diferença entre os valores")
for i in range(0, 10):
    if(salarioPlanilha1[i]!=salarioPlanilha2[i]):
        print(nomesPlanilha1[i], " | ", format(salarioPlanilha1[i]-salarioPlanilha2[i], '.2f'))
    totalPlanilha1+=salarioPlanilha1[i]
    totalPlanilha2+=salarioPlanilha2[i]
    
print("\nA diferença entre o valor total da folha de referência e o valor da folha que foi enviada pela empresa especializada é de:", " ", format(totalPlanilha1-totalPlanilha2, '.2f'))

print("\nA diferença média entre os valores da folha de referência e os valores da folha enviada pela empresa especializada é de:", " ", format((totalPlanilha1/10)-(totalPlanilha2/10),'.3f'))

print("\n---------------------------------------")
    
