#Adamou walkao 18A878FS
#en collaboration avec plusieurs camarades de classe

#lien youtube
https://youtu.be/DHO2LziDn5U

from multiprocessing import Process, Pipe
from time import sleep
import os
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def worker(conn):

	print('worker - Initialisation du sommeil 1 seconde')
	sleep(1)

	a = os.getpid()
	b = 'processus woker, pid = ' + str(a)

	print(a)

	print('worker - envoi de donnée via le pipe')
	conn.send(b)

	print("worker - reception de donnée via le pipe")
	print('worker: ' + conn.recv())

	print('worker - fermeture de worker, fin de la connection')
	conn.close()
	print('worker - Done')

	
@app.get("/")
def main():

	a = os.getpid()
	b = 'processus main, pid = ' + str(a)

	print(a)

	print('Main - Initialisation, creation du pipe')
	main_connection, worker_connection = Pipe()

	print('Main - mise en place du processus')
	p = Process(target = worker, args = [worker_connection])

	print('Main - Initialisation du processus')
	p.start()

	print('Main - en attente de la reponse du processus fils')

	print('\n')
	print('Main - reception de donnée via le pipe')
	print('Main : ' + main_connection.recv())

	print('\n')
	print('Main - envoi de donnée via le pipe')
	main_connection.send(b)

	print('Main - fermeture du main, fin de la de connection')
	main_connection.close()

	print('Main - Done')
	print('\n\n')
	
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
	main()
