class s0():
	def __init__(self, s):
		self.s = s
		self.l = 0
	def __eq__(self, target):
		return all([self.l==target.l, self.s==target.s])

class w():
	def __init__(self, l, W0, T=None, G=[]):
		if type(G)==list and type(l)==int and l>=0 and l==W0.l+1:
			pass
		else:
			raise ValueError('At least one of them wrong: level l; representative element W0; tag T; generation rule G')
		self.l = l
		self.W0 = W0
		self.T = T
		self.G = G
		# To simplify, here we set:
		self.W = self.G
	def __eq__(self, target):
		return all([self.l==target.l, self.W0==target.W0, self.T==target.T, self.G==target.G, self.W==target.W])

class s():
	def __init__(self, l, words):
		if type(words)==list and all(list(map(lambda x: x[0]==l and type(x)==list and len(x)==3, words))):
			self.s = words
		else:
			raise ValueError(f'Cannot form a list of words at level {l}!')
		self.l = l
	def __eq__(self, target):
		return all([self.l==target.l, self.s==target.s])

class DAHSF():
	def __init__(self, pairs=[]):
		self.ids = []
		self.words = []
		try:
			for ID, word in pairs:
				assert all([type(ID)==list, len(ID)==3, type(ID[0])==int, type(word)==w, word.l==ID[0]])
				assert ID not in self.ids; assert word not in self.words
				self.ids.append(ID); self.words.append(word)
		except:
			raise TypeError('Not pairwise (ID triple, word) or Repetitive!')
	def __call__(self, target):
		if type(target)==list:
			return self.words[self.ids.index(target)]
		elif type(target)==w:
			return self.ids[self.words.index(target)]
		else:
			raise TypeError
	def levels(self):
		assert self.ids!=[] and self.words!=[]
		return sorted(self.ids, reverse=True)[0][0]
	def receptor_grows(self, l):
		receptor = []
		for coordinate in self.ids:
			if coordinate[0]==l:
				word = self(coordinate)
				for probe in map(lambda x: x.s, word.W):
					receptor.append([probe, coordinate])
		receptor.sort(key=lambda x: len(x[0]), reverse=True)
		return receptor
	def generator_grows(self, l):
		generator = []
		for coordinate in self.ids:
			if coordinate[0]==l:
				word = self(coordinate)
				generator.append([word.W0.s, list(map(lambda x: x.s, word.W))])
		return generator
	def W(self, W0):
		for idx, ID in enumerate(self.ids):
			if ID[-1]==W0:
				return list(map(lambda x: x.s, self.words[idx].W))
	def W0(self, Wi):
		for idx, word in enumerate(self.words):
			if Wi in map(lambda x: x.s, word.W):
				return word.W0.s
	def tags(self, l):
		TAGS = set()
		for coordinate in self.ids:
			if coordinate[0]==l:
				TAGS.add(coordinate[1])
		return TAGS
	def get_tag(self, Wi):
		for idx, word in enumerate(self.words):
			if Wi in map(lambda x: x.s, word.W):
				return word.T
	def refresh_changes(self, changes):
		from copy import deepcopy
		levels = list(map(lambda x: x[0], self.ids))
		levels.append(levels[-1]+1)
		for level in range(int(*changes) + 1, levels[-1]):
			changes[level] = []
			for index, coordinate in enumerate(self.ids):
				if coordinate[0]!=level:
					continue
				for change in changes[level-1]:
					old_ID = deepcopy(coordinate)
					while change[0] in coordinate[2]:
						idx = coordinate[2].index(change[0])
						coordinate[2][idx] = change[1]
					for W in self.words[index].W:
						while change[0] in W.s:
							idx = W.s.index(change[0])
							W.s[idx] = change[1]
					# in this example self.W = self.G
					changes[level].append((old_ID, coordinate, self.words[index]))
					del old_ID
	def modify_tag(self, ID, T):
		# check if ID valid
		W = self(ID)
		from copy import deepcopy
		old_ID = deepcopy(ID)
		# get the index
		idx = self.ids.index(ID)
		# modify the target itself
		W.T = T
		ID[1] = T
		# modify database
		self.ids[idx] = ID
		self.words[idx] = W
		# refresh state spaces with greater levels
		changes = {ID[0]: [(old_ID, ID)]}
		del old_ID, W
		self.refresh_changes(changes)
	def change_representative_element(self, old_ID, new_representative_element):
		# check if ID valid
		W = self(old_ID)
		assert new_representative_element in list(map(lambda x: x.s, W.W))
		# get the index
		idx = self.ids.index(old_ID)
		# generate new ID
		new_ID = old_ID[:-1]
		new_ID.append(new_representative_element)
		# modify database
		self.ids[idx] = new_ID
		W.W0.s = new_representative_element
		self.words[idx] = W
		# refresh state spaces with greater levels
		changes = {new_ID[0]: [(old_ID, new_ID)]}
		del W
		self.refresh_changes(changes)
	# in this example self.W = self.G
	def add_generation_rule(self, ID, generation_rule):
		# check if ID valid
		W = self(ID)
		# add generation rule
		W.G.append(generation_rule)
	def delete_generation_rule(self, ID, generation_rule):
		# check if ID valid
		W = self(ID)
		# delete generation rule
		for item in W.G:
			if generation_rule==item:
				W.G.remove(item)
				break
	def insert(self, word):
		assert type(word)==w
		ID = [word.l, word.T, word.W0.s]
		assert ID not in self.ids; assert word not in self.words
		self.ids.append(ID); self.words.append(word)
	def remove(self, ID):
		# check if ID valid
		W = self(ID)
		# remove it
		self.ids.remove(ID); self.words.remove(W)
		changes = {ID[0]: [ID]}
		del ID, W
		# refresh state spaces with greater levels
		from copy import deepcopy
		levels = list(map(lambda x: x[0], self.ids))
		levels.append(levels[-1]+1)
		for level in range(int(*changes) + 1, levels[-1]):
			changes[level] = []
			index = 0
			while index<len(self.words):
				word = self.words[index]
				if word.l==level:
					for change in changes[level-1]:
						if any(map(lambda w: change in w.s, word.W)):
							changes[level].append(self.ids[index])
							del self.ids[index]; del self.words[index]
							index -= 1
							break
				index += 1
