import time
from random import randint
import matplotlib.pyplot as pyplot


def remplir(tab, n):
	
	for i in range(n):
		
		x = randint(1, 50)
		tab.append(x)




def minimum(tab):

	start = time.time()

	mini = tab[0]
	for j in range(len(tab)):

		if tab[j] < mini:
			mini = tab[j]

	end = time.time()

	t = end - start

	return mini, t





def main():


	taill = [1000, 2000, 3000, 4000, 5000]
	temp = []

	for k in range(len(taill)):

		tab = []

		N = taill[k]

		remplir(tab, N)

		print('for N =', N)

		mini, tmp = minimum(tab)

		print('min element:', mini)

		print('time in sec:', tmp)

		print("\n\n")

		temp.append(tmp)

	print(taill)
	print(temp)

	pyplot.ylabel('taille', fontsize = 12)
	pyplot.xlabel('temp', fontsize = 12)

	pyplot.title('Taille vs temps')

	pyplot.plot(temp, taill, 'bo-')
	pyplot.show()

		
	
	


if __name__ == '__main__':
	
	main()