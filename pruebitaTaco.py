
nombres_vien = {1:"Lun", 2:"Mar", 3:"Mie", 4:"Jue", 5:"Vie", 6:"Sab", 7:"Dom"}

nombres_bien = {"Lun":1, "Mar":2, "Mie":3, "Jue":4, "Vie":5, "Sab":6, "Dom":7}

class Weeker:
    
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        añadir_dias = nombres_bien.get(self.day) + n
        dia_resultado = nombres_vien.setdefault(añadir_dias)
        if dia_resultado == None:
            self.day = nombres_vien[0]
            añadir_dias = nombres_bien.get(self.day) + n
            dia_resultado = nombres_vien.setdefault(añadir_dias)
            print(dia_resultado) 
        print(dia_resultado) 

    def subtract_days(self, n):
        restar_dias = nombres_bien.get(self.day) - n
        dias_restados = int(restar_dias)
        if dias_restados < 0:
            cuenta_final = (7 + dias_restados)
            caca = nombres_vien[cuenta_final]
            print(caca)
        else:
            dia_resultado = nombres_vien.setdefault(dias_restados)
            print(dia_resultado) 
        
        
weekday = Weeker('Lun')
print(weekday)
weekday.add_days(5)
weekday.subtract_days(3)  






























