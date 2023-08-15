# -*- coding: latin-1 -*-
#------------------------------------------------------------
# Created By: Delvidio Demarchi Neto
# Created Date: 03/04/2023
# Laste Update: 14/08/2023
# Version: '2.0.0'
#------------------------------------------------------------
""" Função para manipulação de datas. """

from datetime import date, datetime, timedelta
import holidays
import calendar

class PyEon():
    """Classe de manipulação de datas - PyEon
    
    PyEon(Interval, Date, Increment, Alignment)

    Interval: Intervalo de calculo (Year: ano, Month: Mês, Day: Dias).
    Date: Data de referência de calculo.
    Increment: Incremento de calculo, necessario número inteiro positivo ou negativo.
    Alignment: Alinhamento da data (B: Primeiro dia do mês, E: Ultimo dia do mês e S: Mesmo dia de referencia).

    """

    def getDates(self):
        """ getDates: Método que trás o dia de forma corrente YYYY-MM-DD """
 
        vDayClass = self._Date.day
        vMonthClass = self._Date.month
        vYearClass = self._Date.year
        
        def __getAlignment(vYearMeth, vMonthMeth, vDayMeth):
            
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
            vGetDate = __getAlignment(vInterYear, vMonthClass, vDayClass)
              
            vInterDate = date(vGetDate.year, vGetDate.month ,vGetDate.day)
 
        elif self._Interval.upper() == "MONTH":
            i = 1
            vMonth = vMonthClass
            vYear = vYearClass
            monthThirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
            monthThirtyDays = [4, 6, 9, 11] 
            cDays = 0
 
            while i <= abs(self._Increment):
                if self._Increment < 0:
                    if vMonth == 1:
                        vMonth = 13
                        vYear = vYear - 1
                    vMonth = vMonth - 1
                else: 
                    if vMonth == 12:
                        vMonth = 0
                        vYear = vYear + 1
                    vMonth = vMonth + 1
 
                for iThirtyOneDays in monthThirtyOneDays:
                    if iThirtyOneDays == vMonth:
                        cDays =  cDays + 31
                    else:
                        vldMonthThirtyOne = False
 
                if vldMonthThirtyOne == False:
                     for iThirtyDays in monthThirtyDays:
                        if iThirtyDays == vMonth:
                            cDays =  cDays + 30
 
                # Valida ano Bissexto
 
                if calendar.isleap(vYear) == True and vMonth== 2:
                    cDays =  cDays + 29
 
                elif calendar.isleap(vMonth) == False and vMonth == 2:
                    cDays =  cDays + 28
                i = i + 1
 
            if self._Increment < 0:
                interDate = self._Date + timedelta(days=(cDays * -1))
            elif self._Increment > 0:
                interDate = self._Date + timedelta(days=(cDays))
            else:
                interDate = self._Date                
 
            vInterDate = __getAlignment(interDate.year, interDate.month, interDate.day)
    
            # elif vIinterval.upper() == "WEEK":
            #     pass
 
        elif self._Interval.upper() == "DAY":
            
            interDate =  self._Date + timedelta(days=self._Increment)
            
            vInterDate = __getAlignment(interDate.year, interDate.month, interDate.day)
                
        return vInterDate
    
    def getAnoMes(self):
        """ getAnoMes: Método que trás o ano mês """
 
        vData = self.getDates()
 
        ano = str(vData.year)
 
        if vData.month < 10:            
            mes = "0"+str(vData.month)
        else:
            mes = str(vData.month)
 
        anomes = ano+mes
        return anomes
