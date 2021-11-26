from random import randint



def remplir(n):

	liste = []
	for i in range(n):
		A = []
		for j in range(n):
			x = randint(0, 9)
			A.append(x)

		liste.append(A)

	return liste


def produit(A, B):
	
	C = remplir(len(A))

	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(A[0])):
				C[i][j] += A[i][k] * B[k][j]

	return C






def main():

	T = remplir(3)
	L = remplir(3)

	tab = produit(T, L)

	print(T)
	print(L)
	print(tab)


if __name__ == '__main__':

	main()