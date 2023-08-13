# -*- coding: latin-1 -*-
#------------------------------------------------------------
# Created By: Delvidio Demarchi Neto
# Created Date: 03/04/2023 
# Version: '1.0.0'
#------------------------------------------------------------
""" Função para manipulação de datas. """

from datetime import date, datetime, timedelta
import holidays
import calendar

class intnx():
    """Classe de manipulação de datas - intnx
    
    intnx(Interval, Date, Increment, Alignment)

    Interval: Intervalo de calculo (Year: ano, Month: Mês, Day: Dias).
    Date: Data de referência de calculo.
    Increment: Incremento de calculo, necessario número inteiro positivo ou negativo.
    Alignment: Alinhamento da data (B: Primeiro dia do mês, E: Ultimo dia do mês e S: Mesmo dia de referencia).

    """

    def __init__(self, Interval, Date, Increment, Alignment):
  
        self._Interval = Interval
        self._Date = Date
        self._Increment = Increment
        self._Alignment = Alignment
        self._EndDate = ''
        self.varDate = datetime.strptime(Date, '%Y-%m-%d')

    def getDates(self):
        """ getDates: Método que trás o dia de forma corrente YYYY-MM-DD """

        vDayClass = self.varDate.day
        vMonthClass = self.varDate.month
        vYearClass = self.varDate.year
        
        def __getAlignment(vDayMeth, vMonthMeth, vYearMeth):
            
            if self._Alignment.upper() == "B":
                vDateMeth = date(vYearMeth, vMonthMeth, 1)

            elif self._Alignment.upper() == "S":
                vDateMeth = date(vYearMeth, vMonthMeth, vDayMeth)

            elif self._Alignment.upper() == "E":
                endOfMonth = calendar.monthrange(vYearMeth, vMonthMeth)
                vDateMeth = date(vYearMeth, vMonthMeth, endOfMonth[1])

            return vDateMeth
        

        if self._Interval.upper() == "YEAR":

            vInterYear = abs(vYearClass + (self._Increment))      
            vGetDate = __getAlignment(vDayClass, vMonthClass, vInterYear)   
            vInterDate = date(vGetDate.year, vGetDate.month ,vGetDate.day)

        elif self._Interval.upper() == "MONTH":
            
            monthThirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
            monthThirtyDays = [4, 6, 9, 11] 

            endOfMonth = calendar.monthrange(ano, mes)

            for iThirtyOneDays in monthThirtyOneDays:
                if iThirtyOneDays == vMonthClass:
                    validMonth = True
                else:
                    validMonth = False

            for iThirtyDays in monthThirtyDays:
                if iThirtyDays == vMonthClass:
                    validMonth = True
                else:
                    validMonth = False



    #         if arDia[1] == 28 and self._Increment < 0:
    #             ldom = 31 * self._Increment

    #         elif arDia[1] == 29 and self._Increment < 0:
    #             ldom = 30 * self._Increment

    #         elif arDia[1] == 28 and self._Increment > 0:             
    #             ldom = 30 * self._Increment 

    #         else:

    #             try:
    #                 validMonth = [1, 3, 5, 7, 8, 10, 12].index(mes)
    #                 ldom = arDia[1] * self._Increment 

    #             except:
    #                 if self.varDate.day == 30:

    #                     if calendar.isleap(ano) == True:
    #                         calcDia = 31
    #                     else:
    #                         calcDia = 30

    #                     ldom = calcDia * self._Increment                
    #                 else:
    #                     ldom = arDia[1] * self._Increment 

    #         vMonth = self.varDate + timedelta(days=ldom) 

    #         vDia = getAlinhamento(dia,vMonth.month, vMonth.year)   
    #         vData = date(vMonth.year, vMonth.month ,vDia.day)

    #     # elif vIinterval.upper() == "WEEK":
    #     #     pass

    #     elif self._Interval.upper() == "DAY":
            
    #         vDia =  self.varDate + timedelta(days=self._Increment)
            
    #         vData = getAlinhamento(vDia.day,vDia.month,vDia.year)        
    #     self._DataFim = vData
    #     return vData
     
    # def getAnoMes(self):
    #     """ getAnoMes: Método que trás o ano mês """

    #     vData = self.getDates()

    #     ano = str(vData.year)

    #     if vData.month < 10:            
    #         mes = "0"+str(vData.month)
    #     else:
    #         mes = str(vData.month)

    #     anomes = ano+mes
    #     return anomes
