from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import copy
from django.views.generic import TemplateView

# Create your views here.
'''
	Views
	index
	type_search
	show_Article
	
	Value
	page_number  
	type_list
	type_dict
	tp_list
	
	Fun 
	get_typeANumber_Article_All
	get_page_number
'''

def get_typeANumber_Article_All():
	
	'''
			获取各类文章的数目
	'''
	
	global page_number
	global type_list 
	global type_dict 
	global tp_list 
	i=0
	for tp in type_list:
		#if type_dict['number']==len(Article.objects.filter(type=tp)):
		tp_list[i]['number'] = len(Article.objects.filter(type=tp))
		i+=1
		
def get_page_number(type):
	
	'''
		获取分页数目
	'''
	
	global page_number
	ArticleList = Article.objects.filter(type=type)
	if len(ArticleList)>5:
		for var in range(len(ArticleList)/5):
			page_number.append(var+1)
	else:
		if len(page_number) == 0:
			page_number.append(1)
	return page_number
	

'''
	page_number 分页
	type_list	文章类型
	type_dict	临时文章变量
	tp_list		每种文章类型的数量
'''

page_number=[]
type_list = ['C语言','Python','Django','数据结构','算法',]
type_dict = {'type':'','number':''}
tp_list =[
	{'type':'C语言','number':''},
	{'type':'Python','number':''},
	{'type':'Django','number':''},
	{'type':'数据结构','number':''},
	{'type':'算法','number':''},
	]

class MyBase(TemplateView):
	page_number=[]
	type_list = ['C语言','Python','Django','数据结构','算法',]
	type_dict = {'type':'','number':''}
	tp_list =[
		{'type':'C语言','number':''},
		{'type':'Python','number':''},
		{'type':'Django','number':''},
		{'type':'数据结构','number':''},
		{'type':'算法','number':''},
		]
	
	def get_page_number(type):
		
		'''
			获取分页数目
			contains 模糊匹配  like %xxx%
		'''
		
		
		ArticleList = Article.objects.filter(type=type)
		if len(ArticleList)>5:
			for var in range(len(ArticleList)/5):
				self.page_number.append(var+1)
		else:
			if len(page_number) == 0:
				self.page_number.append(1)
		return page_number
		
	def get_typeANumber_Article_All():
		
		'''
				获取各类文章的数目
		''' 
		
		for tp in self.type_list:
			#if type_dict['number']==len(Article.objects.filter(type=tp)):
			#self.tp_list[i]['number'] = len(Article.objects.filter(type=tp))
			tp['number'] = len(Article.objects.filter(type=tp))
			

class index(MyBase):
	'''
		主页
		在类的方法中调用另一个方法 带self 与不带self是否有区别
	'''	
	def get(self,request, *args, **kwargs):
		get_typeANumber_Article_All()
		ArticleList = Article.objects.filter(type='C语言')
		self.page_number = get_page_number(type)
		print(self.page_number)
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':self.page_number,'tp_list':tp_list})
	def post(self,request, *args, **kwargs):
		pass

'''def index(request):
	
		主页
	
	if request.method == 'GET':
	
		get_typeANumber_Article_All()
		ArticleList = Article.objects.filter(type='C语言')
		page_number = get_page_number(type)
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':page_number,'tp_list':tp_list})'''
	
class Type_search(MyBase):
	'''
		查找相应类型的文章
		get 方法的kwargs参数 存放 get请求的参数
	'''
	def get(self,request,*args,**kwargs):
		
		get_typeANumber_Article_All()
		ArticleList = Article.objects.filter(type=kwargs['type'])
		self.page_number = get_page_number(kwargs['type'])
		get_typeANumber_Article_All()
		
		return  render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':self.page_number,'tp_list':tp_list})
		
	def post(slef,request,*args,**kwargs):
		pass


'''def type_search(request,type):
	
		查找相应类型的文章
	
	if request.method == 'GET':
		ArticleList = Article.objects.filter(type=type)
		self.page_number = get_page_number(type)
		
		get_typeANumber_Article_All()
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':self.page_number,'tp_list':self.tp_list})'''

class Show_Article(MyBase):
	'''
		显示文章详细
	'''
	def get(self,request,*args,**kwargs):
		get_typeANumber_Article_All()
		ArticleList = Article.objects.filter(type=kwargs['type'])
		self.page_number = get_page_number(kwargs['type'])
		article=Article.objects.filter(type=kwargs['type'],title=kwargs['ArticleName']).first()
		
		return render(request,'Blog/Article.html',{'article':article,'tp_list':tp_list})
	def post(self,request,*args,**kwargs):
		pass

'''def show_Article(request,type,ArticleName):	
	
		显示文章详细
	
	if request.method == 'GET':
		ArticleList = Article.objects.filter(type=type)
		page_number = get_page_number(type)
		article=Article.objects.filter(type=type,title=ArticleName).first()
		get_typeANumber_Article_All()
		print(article)
		return render(request,'Blog/Article.html',{'article':article,'tp_list':tp_list})'''
		
class serach(MyBase):
	'''
		搜索文章
		因为无法通过get_page_number方法获取分页  现在要么重写该方法 要么使该方法可以使用
		疑问  get 方法 按理说是可以接受到前端的get请求的参数的  但这里没有收到  目前使用request.GET.get(option)
		Show_Article类中get方法获取到了url上的参数   难道get请求的参数不是url上的参数 
	'''
	def get(self,request,*args,**kwargs):
		get_typeANumber_Article_All()
		print(request.GET.get('Article'))
		ArticleList = Article.objects.filter(title__contains=request.GET.get('Article'))
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'tp_list':tp_list})
		
