import threading
import random as ran
from datetime import datetime
import time

Mq = 1
Lq = 1
Tq = 1
Dq = 1

# Los strings para cada pelicula
M = "Minios"
L = "Lightyear"
T = "Thor"
D = "Doctor Strange"

# semaforos
common_zone_log_sem = threading.Semaphore(1)
M_log_sem = threading.Semaphore(1) 
L_log_sem = threading.Semaphore(1) 
T_log_sem = threading.Semaphore(1) 
D_log_sem = threading.Semaphore(1) 
exit_log_sem = threading.Semaphore(1)

# minios
q1 = threading.Semaphore(1)
M_q_sem = threading.Semaphore(0)
M_pelicula_sem = threading.Semaphore(1)

# laigyer 
q2 = threading.Semaphore(1)
L_q_sem = threading.Semaphore(0)
L_pelicula_sem = threading.Semaphore(1)

# tor
q3 = threading.Semaphore(1)
T_q_sem = threading.Semaphore(0)
T_pelicula_sem = threading.Semaphore(1)

# doctor estrench 
q4 = threading.Semaphore(1)
D_q_sem = threading.Semaphore(0)
D_pelicula_sem = threading.Semaphore(1)


"""
class cliente
Es la clase para cada cliente, recibe el nombre y la pelicula que verá
Ademas contiene las siguientes funciones:
def log_entry: Escribe en el archivo patio central, la persona, el tiempo de ingreso , la pelicula que verá, y el tiempo de la salida de la fila.
def log_pelicula: Escribe en el archivo de la pelicula ingresado, la persona, el tiempo que estuvo en la fila, y el tiempo que dejo la fila
def log_exit: Escribe en el archivo de salida.txt, la persona y el tiempo de salida del cine.
"""

class cliente:
    def __init__(self,nombre, pelicula):
        self.nombre = nombre
        self.pelicula = pelicula
        self.entry_time = 0
        self.exit_time = 0

    def log_entry(self, nombreArchivo,common_zone_log_sem):
        common_zone_log_sem.acquire()

        filezc = open(nombreArchivo, 'a+')
        filezc.write(
            str(self.nombre) + ", " + str(self.entry_time) + ", " + str(
                self.pelicula) + ", " + str(self.exit_time) + "\n")
        filezc.close()
        common_zone_log_sem.release()

    def log_pelicula(self, nombreArchivo, pelicula_log_sem ):
        pelicula_log_sem.acquire()

        file_pelicula = open(nombreArchivo, 'a+')
        file_pelicula.write(str(self.nombre) + ', ' + str(self.start_time) + ', ' + str(
                        self.exit_time) + '\n')
        file_pelicula.close()
        pelicula_log_sem.release()
    
    def log_exit(self, nombreArchivo, exit_log_sem):
        exit_log_sem.acquire()

        file_pelicula = open(nombreArchivo, 'a+')
        file_pelicula.write(str(self.nombre) + ', ' + str(self.start_time) + '\n')
        file_pelicula.close()
        exit_log_sem.release()


"""
class Minios
Es la clase para minions, recibe capacidad de la fila, duracion de la pelicula y la capacidad de la sala.
Ademas contiene las siguientes funciones:
def start_M_thread: Crea el Thread para la pelicula.
def run_M: Corre la pelicula. 
"""

class Minios:
    attendees = []

    def __init__(self, q_cap, dur, pelicula_cap):
        self.pelicula_capacitiy = pelicula_cap
        self.queue_capacitiy = q_cap
        self.duration = dur

    def start_M_thread(self):
        t_M = threading.Thread(target = self.run_M)
        t_M.start()

    def run_M(self):
        while True:
            if len(self.attendees) >= self.pelicula_capacitiy:
                M_pelicula_sem.acquire()
                start_time = datetime.now().time()
                
                time.sleep(self.duration)

                for i in range(0,self.pelicula_capacitiy):

                    self.attendees[0].exit_time = start_time
                    self.attendees[0].log_pelicula('Minios.txt', M_log_sem)

                    self.attendees[0].start_time = datetime.now().time()
                    self.attendees[0].log_exit('Salida.txt', exit_log_sem)
                    del self.attendees[0]

                M_pelicula_sem.release()


"""
class Lightyear
Es la clase para Lightyear, recibe capacidad de la fila, duracion de la pelicula y la capacidad de la sala.
Ademas contiene las siguientes funciones:
def start_M_thread: Crea el Thread para la pelicula.
def run_M: Corre la pelicula. 
"""

class Lightyear:
    attendees = []

    def __init__(self, q_cap, dur, pelicula_cap):
        self.pelicula_capacitiy = pelicula_cap
        self.queue_capacitiy = q_cap
        self.duration = dur

    def start_L_thread(self):
        t_L = threading.Thread(target=self.run_L)
        t_L.start()

    def run_L(self):
        while True:
            if len(self.attendees) >= self.pelicula_capacitiy:
                L_pelicula_sem.acquire()
                start_time = datetime.now().time()

                time.sleep(self.duration)

                for i in range(0, self.pelicula_capacitiy):

                    self.attendees[0].exit_time = start_time
                    self.attendees[0].log_pelicula('Lightyear.txt', L_log_sem)

                    self.attendees[0].start_time = datetime.now().time()
                    self.attendees[0].log_exit('Salida.txt', exit_log_sem)

                    del self.attendees[0]

                L_pelicula_sem.release()


"""
class Thor
Es la clase para Thor, recibe capacidad de la fila, duracion de la pelicula y la capacidad de la sala.
Ademas contiene las siguientes funciones:
def start_M_thread: Crea el Thread para la pelicula.
def run_M: Corre la pelicula. 
"""

class Thor:
    attendees = []

    def __init__(self, q_cap, dur, pelicula_cap):
        self.pelicula_capacitiy = pelicula_cap
        self.queue_capacitiy = q_cap
        self.duration = dur

    def start_T_thread(self):
        t_T = threading.Thread(target=self.run_T)
        t_T.start()

    def run_T(self):
        while True:
            if len(self.attendees) >= self.pelicula_capacitiy:
                T_pelicula_sem.acquire()
                start_time = datetime.now().time()

                time.sleep(self.duration)

                for i in range(0, self.pelicula_capacitiy):

                    self.attendees[0].exit_time = start_time
                    self.attendees[0].log_pelicula('Thor.txt', T_log_sem)

                    self.attendees[0].start_time = datetime.now().time()
                    self.attendees[0].log_exit('Salida.txt', exit_log_sem)

                    del self.attendees[0]
                T_pelicula_sem.release()


"""
class DoctorStrange
Es la clase para DoctorStrange, recibe capacidad de la fila, duracion de la pelicula y la capacidad de la sala.
Ademas contiene las siguientes funciones:
def start_M_thread: Crea el Thread para la pelicula.
def run_M: Corre la pelicula. 
"""

class DoctorStrange:
    attendees = []

    def __init__(self, q_cap, dur, pelicula_cap):
        self.pelicula_capacitiy = pelicula_cap
        self.queue_capacitiy = q_cap
        self.duration = dur

    def start_D_thread(self):
        t_D = threading.Thread(target=self.run_D)
        t_D.start()

    def run_D(self):
        while True:
            if len(self.attendees) >= self.pelicula_capacitiy:
                D_pelicula_sem.acquire()
                start_time = datetime.now().time()

                time.sleep(self.duration)

                for i in range(0, self.pelicula_capacitiy):

                    self.attendees[0].exit_time = start_time
                    self.attendees[0].log_pelicula('Doctor Strange.txt', D_log_sem)

                    self.attendees[0].start_time = datetime.now().time()
                    self.attendees[0].log_exit('Salida.txt', exit_log_sem)

                    del self.attendees[0]
                D_pelicula_sem.release()


"""
class PatioCentral
Es la clase para la patio central.
Ademas contiene las funciones:
def start_common_zone_thread: para empezar las colas de cada una de las peliculas.
def queue_people: Conteo de las veces que sale un pelicula, ademas de meter a las personas a la fila de espera antes de la pelicula..
def send_to_pelicula_queue: Manda a las personas a la queue de la pelicula correspondiente.
"""

class PatioCentral:
    MiniosQ = []
    LightyearQ = []
    ThorQ = []
    DoctorStrangeQ = []

    def __init__(self):
        self.M = Minios(15,5,12)
        self.M.start_M_thread()
        self.L = Lightyear(8,3,2)
        self.L.start_L_thread()
        self.T = Thor(15, 7, 5)
        self.T.start_T_thread()
        self.D = DoctorStrange(5, 2, 1)
        self.D.start_D_thread()

    def start_common_zone_thread(self):
        t_M = threading.Thread(target = self.send_to_M_queue)
        t_L = threading.Thread(target = self.send_to_L_queue)
        t_T = threading.Thread(target = self.send_to_T_queue)
        t_D = threading.Thread(target = self.send_to_D_queue)
        t_M.start()
        t_L.start()
        t_T.start()
        t_D.start()

    def queue_people(self, cliente: cliente):
        cliente.entry_time = datetime.now().time()
        
        if cliente.pelicula == M:
            self.MiniosQ.append(cliente)
            global Mq
            if Mq:
                M_q_sem.release()
                Mq = 0

        elif cliente.pelicula == L:
            self.LightyearQ.append(cliente)
            global Lq
            if Lq:
                L_q_sem.release()
                Lq = 0

        elif cliente.pelicula == T:
            self.ThorQ.append(cliente)
            global Tq
            if Tq:
                T_q_sem.release()
                Tq = 0

        elif cliente.pelicula == D:
            self.DoctorStrangeQ.append(cliente)
            global Dq
            if Dq:
                D_q_sem.release()
                Dq = 0
        else:
            print(" xd ")

    def send_to_M_queue(self ):

        while True:
            if len(self.MiniosQ) == 0:
                global Mq
                Mq = 1
                M_q_sem.acquire()

            if len(self.MiniosQ) > 0:
                q1.acquire()

                if len(self.M.attendees) == self.M.queue_capacitiy:
                    q1.release()

                else:
                    self.MiniosQ[0].exit_time = datetime.now().time()

                    self.MiniosQ[0].log_entry('PatioCentral.txt', common_zone_log_sem)

                    self.MiniosQ[0].start_time = datetime.now().time()
                    self.M.attendees.append(self.MiniosQ[0])
                    del self.MiniosQ[0]
                    q1.release()
                    time.sleep(1)

    def send_to_L_queue(self):

        while True:
            if len(self.LightyearQ) == 0:
                global Lq
                Lq = 1
                L_q_sem.acquire()

            if len(self.LightyearQ) > 0:
                q2.acquire()

                if len(self.L.attendees) == self.L.queue_capacitiy:
                    q2.release()

                else:
                    self.LightyearQ[0].exit_time = datetime.now().time()

                    self.LightyearQ[0].log_entry('PatioCentral.txt', common_zone_log_sem)

                    self.LightyearQ[0].start_time = datetime.now().time()
                    self.L.attendees.append(self.LightyearQ[0])
                    del self.LightyearQ[0]
                    q2.release()
                    time.sleep(1)

    def send_to_T_queue(self):

        while True:
            if len(self.ThorQ) == 0:
                global Tq
                Tq = 1
                T_q_sem.acquire()

            if len(self.ThorQ) > 0:
                q3.acquire()
                if len(self.T.attendees) == self.T.queue_capacitiy:
                    q3.release()
                else:
                    self.ThorQ[0].exit_time = datetime.now().time()

                    self.ThorQ[0].log_entry('PatioCentral.txt', common_zone_log_sem)

                    self.ThorQ[0].start_time = datetime.now().time()
                    self.T.attendees.append(self.ThorQ[0])
                    del self.ThorQ[0]
                    q3.release()
                    time.sleep(1)


    def send_to_D_queue(self):

        while True:
            if len(self.DoctorStrangeQ) == 0:
                global Dq
                Dq = 1
                D_q_sem.acquire()

            if len(self.DoctorStrangeQ) > 0:
                q4.acquire()
                if len(self.D.attendees) == self.D.queue_capacitiy:
                    q4.release()
                else:
                    self.DoctorStrangeQ[0].exit_time = datetime.now().time()

                    self.DoctorStrangeQ[0].log_entry('PatioCentral.txt' ,common_zone_log_sem)
                    self.DoctorStrangeQ[0].start_time = datetime.now().time()
                    self.D.attendees.append(self.DoctorStrangeQ[0])
                    del self.DoctorStrangeQ[0]
                    q4.release()
                    time.sleep(1)

if __name__ == '__main__':

    #Lista para los clientes

    clientes_list = []

    #Se genera el patio central con su respectivo Thread
    pt = PatioCentral()
    pt.start_common_zone_thread()

    peliculas = [M, L, T, D]

    for i in range(100):
        ## NO OLVIDAR CAMBIAR EL NOMBRE DE WEON A PERSONAS xd
        clientes_list.append(cliente("cliente "+str(i+1), peliculas[ran.randint(0,3)]))

    for c in clientes_list:
        t = threading.Thread(target = pt.queue_people, args=(c,))
        t.start()
