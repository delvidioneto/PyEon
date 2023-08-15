# PyEon
Função pratica para manipulação de datas.

Exemplo de utilização:
```
import pyDateManipulation.PyEon as pe
from datetime import date 

dia_atual = date.today()
print('Dia Atual:', dia_atual)
```

# Um mês a frente da data atual com a data inicial do mês
```
M1 = pe.PyEon('MONTH', dia_atual, 1,'B').getDates()
M1_anomes = pe.PyEon('MONTH',dia_atual, 1,'B').getAnoMes()

print('M1_dia:', M1)
print('M1_anomes:', M1_anomes)
```
# o mesmo dia 12 meses anterior da data atual
```
M1 = pe.PyEon('MONTH', dia_atual, -12,'S').getDates()
M1_anomes = pe.PyEon('MONTH',dia_atual, -12,'S').getAnoMes()

print('M1_dia:', M1)
print('M1_anomes:', M1_anomes)
```

# 2 anos anterior da data atual com o ultimo dia do mês
```
M1 = pe.PyEon('YEAR', dia_atual, -2,'E').getDates()
M1_anomes = pe.PyEon('YEAR',dia_atual, -2,'E').getAnoMes()
```
