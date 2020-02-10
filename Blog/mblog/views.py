from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import copy
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

def index(request):
	'''
		主页
	'''
	if request.method == 'GET':
	
		get_typeANumber_Article_All()
		ArticleList = Article.objects.filter(type='C语言')
		page_number = get_page_number(type)
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':page_number,'tp_list':tp_list})
	
	
def type_search(request,type):
	'''
		查找相应类型的文章
	'''
	if request.method == 'GET':
		ArticleList = Article.objects.filter(type=type)
		page_number = get_page_number(type)
		
		get_typeANumber_Article_All()
		
		return render(request,'Blog/index.html',{'ArticleList':ArticleList,'page_number':page_number,'tp_list':tp_list})
	
def show_Article(request,type,ArticleName):	
	'''
		显示文章详细
	'''
	if request.method == 'GET':
		ArticleList = Article.objects.filter(type=type)
		page_number = get_page_number(type)
		article=Article.objects.filter(type=type,title=ArticleName).first()
		get_typeANumber_Article_All()
		print(article)
		return render(request,'Blog/Article.html',{'article':article,'tp_list':tp_list,'ArticleList':ArticleList})