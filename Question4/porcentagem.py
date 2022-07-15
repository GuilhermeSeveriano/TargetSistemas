
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53


cidades = [sp, rj, mg, es, outros]

total_soma = sum(cidades)



percentual_sp = (sp * 100)/total_soma
percentual_rj = (rj*100)/total_soma
percentual_mg = (mg*100)/total_soma
percentual_es = (es*100)/total_soma
percentual_outros = (outros *100)/total_soma


print(f"A media em porcentagem de SP é: {round(percentual_sp, 2)}%")
print(f"A media em porcentagem de RJ é: {round(percentual_rj, 2)}%")
print(f"A media em porcentagem de MG é: {round(percentual_mg, 2)}%")
print(f"A media em porcentagem de ES é: {round(percentual_es, 2)}%")
print(f"A media em porcentagem de Outros é: {round(percentual_outros, 2)}%")



