# Librerias
from subprocess import Popen, PIPE
from tkinter import messagebox
from datetime import datetime

class RastreoCaidas:
    def comprobar_caida(self):
        """ """
        self.ping_response = Popen(["ping", "8.8.8.8", "-n", '1'], stdout=PIPE).stdout.read()
        self.ping_response = str(self.ping_response)
        self.estado = "100%" in self.ping_response or "Impossible" in self.ping_response
        return self.estado

    def marcas_de_tiempo(self):
        if self.estado:
            #messagebox.showinfo("CAIDA!")
            self.horai = datetime.now().hour
            self.mini = datetime.now().minute
            self.seci = datetime.now().second
            self.hora_inicial = "{}:{}:{}".format(self.horai, self.mini, self.seci)
            while self.estado:
                self.comprobar_caida()
            self.horaf = datetime.now().hour
            self.minf = datetime.now().minute
            self.secf = datetime.now().second
            self.hora_final = "{}:{}:{}".format(self.horaf, self.minf, self.secf)
            self.duracion = "{} horas con {} minutos y {} segundos".format(self.horaf-self.horai, self.minf-self.mini, abs(self.secf-self.seci))
 
    def capturar_trafico(self):
        pass
    
    def resumen(self):
        return {"hora_inicial": self.hora_inicial, "hora_final": self.hora_final, "duracion": self.duracion, "trafico":None}

    def enviar_a_db(self):
        pass

if __name__ == "__main__":
    prueba = RastreoCaidas()
    while prueba.comprobar_caida() == False:
        print("todo bien")
    print("caida")
    print(prueba.marcas_de_tiempo())
    print(prueba.resumen())

else:
    pass

 
        