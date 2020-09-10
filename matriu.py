class matriu:
	
	"""
	Classe matriu, operacions sobre l'objecte matriu, l'operació es realitza afegint la segona matriu com a parametre
	Atributs de classe
	rows -> files de la matriu
	cols -> columnes de la matriu
	r -> llista bidimensional de int o float, del tipus -> [ [a12, a12, a13],[a21,a22,a33],[a31,a32,a33] ] 
	"""
	
	rows = 0
	cols = 0
	r = list()
	
	def __init__(self, r):
		"""
		Constructor de classe, complint que es bidimensional i de tipus int o float, en cas contrari llança excepció
		"""
		try:
			for l in r:
				if (not isinstance(l,list)):
					raise TypeError("Elements de grau 1 [1] han de ser llistes")
				else:
					for el in l:
						if (not isinstance(el, float) and not isinstance(el,int)):
							raise ValueError("Tots els elements de la matriu han de ser reals")
			self.r = r
			self.cols = len(self.r[0])
			self.rows = len(self.r)	
		except Exception as error:
			print("Error al crear la matriu: ", repr(error))
		
	
	#producte escalar de la matriu 
	def escalar(self,num):
		"""
		Producte escalar d'un nombre per la matriu, es realitza multiplicant la posició [row][col] * l'escalar
		"""
		l_aux = []
		for r in self.r:
			f = list(map(lambda x : x*num, r))
			l_aux.append(f)
		self.r = l_aux

	#suma matrius
	def suma_matriu(self,m):
		"""
		Suma de dos matrius, a la propia matriu li afegim la passada per parametre també d'objecte matriu, han de tindre la mateixa dimensió
		"""
		r_org = self.rows
		c_org = self.cols
		
		r_add = m.rows
		c_add = m.cols
		
		if (r_org == r_add and c_org == c_add):
			l_aux = []
			for i in range(len(self.r)):
				r_aux = []
				for j in range(len(self.r[i])):
					sm = self.r[i][j] + m.r[i][j]
					r_aux.append(sm)
				l_aux.append(r_aux)
			self.r = l_aux
		else:
			print("No és pot fer la suma de matrius, dimensions diferents")
	
	#resta matriu
	def resta_matriu(self,m):
		"""
		Resta de dos matrius, a la propia matriu li afegim la passada per parametre també d'objecte matriu, han de tindre la mateixa dimensió
		"""
		r_org = self.rows
		c_org = self.cols
		
		r_add = m.rows
		c_add = m.cols
		
		if (r_org == r_add and c_org == c_add):
			l_aux = []
			for i in range(len(self.r)):
				r_aux = []
				for j in range(len(self.r[i])):
					sm = self.r[i][j] - m.r[i][j]
					r_aux.append(sm)
				l_aux.append(r_aux)
			self.r = l_aux
		else:
			print("No és pot fer la suma de matrius, dimensions diferents")
	
	
	def multiplica_matriu(self,m):
		"""
		Multiplica dos matrius, a la propia matriu multipliquem la passada per parametre també d'objecte matriu, han de coincidir el nombre de files de la
		primera matriu amb el nombre de columnes de la segona matriu.
		"""
		r_org = self.rows
		c_org = self.cols
		
		r_add = m.rows
		c_add = m.cols
		
		
		#matriu auxiliar per a resultat, omplint en 0.
		l_aux = []
		for r in range(0,self.rows):
			r_aux = []
			for c in range(m.cols):
				r_aux.append(0)
			l_aux.append(r_aux)
		
		
		if (r_org == c_add):
			for i in range(0,self.rows):
				for j in range(0,m.cols):
					for k in range(0,m.rows):
						l_aux[i][j] += self.r[i][k] * m.r[k][j]
		else:
			print("No es pot fer la multiplicació, les files no coincideixen amb les columnes")
		
		self.r = l_aux
	
	#divisió matriu, considera matriu
	def divisio_matriu(self,m):
		"""
		Divisió de dos matrius, a la propia matriu dividem per la passada com a parametre, per a dividir una matriu, considerem que multipliquem per
		la matriu amb els elements inversors, en cas de 0 i no poder calcular la inversa, retornará la mateixa matriu sense fer la multiplicació
		"""
		r_org = self.rows
		c_org = self.cols
		
		r_add = m.rows
		c_add = m.cols
		
		error_op = False
		
		#calcular la matriu inversa de m
		for r in range(0,m.rows):
			for c in range(0,m.cols):
				try:
					m.r[r][c] = 1/m.r[r][c]
				except ZeroDivisionError:
					error_op = True
		
		if (not error_op):
			matriu.multiplica_matriu(self,m)
	
	#imprimir matriu
	def imprimir_matriu(self):
		"""
		Imprimeix la matriu per pantalla
		"""
		print("[")
		for row in self.r:
			print(" ", row)
		print("]")
	
	
		
		
	
	
