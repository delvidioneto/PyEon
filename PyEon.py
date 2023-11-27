# -*- coding: latin-1 -*-

from datetime import date, datetime, timedelta
import calendar


class PyEon():
    """Pacote para manipulação de datas. - PyEon

    - Created By: Delvidio Demarchi Neto
    - Created Date: 03/04/2023
    - Laste Update: 14/08/2023
    - Version: '2.0.0'

    PyEon(Interval, Date, Increment, Alignment)

    Atributos: 
        Interval (str): Intervalo do periodo de calculo (Year: ano, Month: Mês, Day: Dias).
        Date (date ou str): Data de referência de calculo no formado yyyy-mm-dd.
        Increment: Incremento de calculo, número inteiro positivo ou negativo.
        Alignment: Alinhamento da data (B: Primeiro dia do mês, E: Ultimo dia do mês e S: Mesmo dia de referencia).

    """

    def __init__(self, Interval: str, Date: date | str, Increment: int, Alignment: str):

        self._Interval = Interval
        self._Increment = Increment
        self._Alignment = Alignment
        self._EndDate = ''

        if type(Date) == str:
            self._Date = datetime.strptime(Date, '%Y-%m-%d')
        else:
            self._Date = datetime.combine(Date, datetime.min.time())

    def getDates(self) -> date:
        """ getDates: Método que retorna o dia no formato YYYY-MM-DD """

        vDayClass = self._Date.day
        vMonthClass = self._Date.month
        vYearClass = self._Date.year

        def __getAlignment(vYearMeth: int, vMonthMeth: int, vDayMeth: int) -> date:

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

            vInterDate = date(vGetDate.year, vGetDate.month, vGetDate.day)

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

                if vMonth in monthThirtyDays:
                    cDays = cDays + 30

                elif vMonth in monthThirtyOneDays:
                    cDays = cDays + 31

                # Valida ano Bissexto
                elif calendar.isleap(vYear) is True and vMonth == 2:
                    cDays = cDays + 29

                elif calendar.isleap(vYear) is False and vMonth == 2:
                    cDays = cDays + 28
                i = i + 1

            if self._Increment < 0:
                interDate = self._Date - timedelta(days=(cDays))
            elif self._Increment > 0:
                interDate = self._Date + timedelta(days=(cDays))
            else:
                interDate = self._Date

            vInterDate = __getAlignment(
                interDate.year, interDate.month, interDate.day)

            # elif vIinterval.upper() == "WEEK":
            #     pass

        elif self._Interval.upper() == "DAY":

            interDate = self._Date + timedelta(days=self._Increment)

            vInterDate = __getAlignment(
                interDate.year, interDate.month, interDate.day)

        return vInterDate

    def getAnoMes(self) -> int:
        """ getAnoMes: Método que trás o ano mês """

        vData = self.getDates()

        ano = str(vData.year)

        if vData.month < 10:
            mes = "0"+str(vData.month)
        else:
            mes = str(vData.month)

        anomes = ano+mes

        return int(anomes)


if __name__ == "__main__":

    dia_atual = date.today()
    print('Dia Atual:', dia_atual)
    print("")

    # # Um mês a frente da data atual com a data inicial do mês

    M1 = PyEon('MONTH', dia_atual, 3, 'B').getDates()
    M1_anomes = PyEon('MONTH', dia_atual, 1, 'B').getAnoMes()

    print('M1_dia:', M1)
    print('M1_anomes:', M1_anomes)
    print("")
