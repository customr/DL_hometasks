import re

class Tag:
	def __init__(self, name, content='', **data):
		self.name = name
		self.content = content
		self.data = data

	def __str__(self):
		return f'<{self.name}{" "*(len(self.data)>0) + " ".join([f"{item}={val}" for item, val in self.data.items()])}>{self.content}</{self.name}>'

	def __repr__(self):
		return f'{self.name}_{self.content}'


class Image(Tag):
	
	NAME = 'img'
	NAME_VARIABLES = ('src', 'img', 'image', 'picture')

	def __init__(self, content='', **data):
		self.data = data

		super().__init__(self.NAME, content, **data)

	def __str__(self):
		return super().__str__()

	def __repr__(self):
		return super().__repr__()


class Input(Tag):

	NAME = 'input'
	NAME_VARIABLES = ('inp', 'input')

	def __init__(self, content='', **data):
		self.data = data

		super().__init__(self.NAME, content, **data)

	def __str__(self):
		return super().__str__()

	def __repr__(self):
		return super().__repr__()


class Text(Tag):
	
	NAME = 'p'
	NAME_VARIABLES = ('text', 'txt', 'p')

	def __init__(self, content='', **data):
		self.data = data

		super().__init__(self.NAME, content, **data)

	def __str__(self):
		return super().__str__()

	def __repr__(self):
		return super().__repr__()

class Link(Tag):
	
	NAME = 'a'
	NAME_VARIABLES = ('href', 'a')

	def __init__(self, content='', **data):
		self.data = data

		super().__init__(self.NAME, content, **data)

	def __str__(self):
		return super().__str__()

	def __repr__(self):
		return super().__repr__()

class TagFactory:

	def __init__(self):
		self.tags = []

	def create_tag(self, name, content='', **data):
		assert isinstance(name, str), 'Tag name must be a string-like'

		name = name.lower()
		rname = re.match(r'(\D+)', name)
		
		if '' == name:
			self.tags.append(Tag('tag', content))
			return self.tags[-1]

		if rname:
			rname = rname.group(1)
		else:
			raise ValueError(f'Unknown name tag - "{name}"')

		for tag in TAGS:
			if rname in tag.NAME_VARIABLES:
				self.tags.append(tag(content, **data))
				return self.tags[-1]

		raise ValueError(f'Unknown name tag - "{name}"')

	def __str__(self):
		return str(self.tags)

TAGS = [Image, Input, Text, Link]

if __name__ == '__main__':
	factory = TagFactory()
	# elements = ('image', 'inp', 'a', 'a1', 'a2', 'a12', 'href', 'text', '')
	# for el in elements:
	# 	print(factory.create_tag(el))

	print(factory.create_tag('a', href='adfgadfgd', somedata=124))
