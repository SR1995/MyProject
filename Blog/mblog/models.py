from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
'''
	Article
'''
# choices

author_choices=[
	('admin','MZ'),
	('other','other'),
]

type_choices=[
	('C语言','C语言'),
	('Python','Python'),
	('Django','Django'),
	('数据结构','数据结构'),
	('算法','算法'),
]

class Article(models.Model):
	'''
		title
		content
		author
		type
		Browse number
		date
	'''
	
	title = models.CharField(max_length=50)
	content = RichTextField()
	author = models.CharField(max_length=20,choices=author_choices,default='MZ')
	type = models.CharField(max_length=30,choices=type_choices,default='C语言')
	Bnumber = models.IntegerField(default=0)
	date = models.DateField(auto_now=True)
	
	def __str__(self):
		return self.title