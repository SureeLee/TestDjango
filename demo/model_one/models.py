from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField('名称',max_length=30) #把后台admin里的字段名替换成中文，方便看..
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    #model内部类
    class Meta:
        verbose_name = '出版商' #让后台admin的数据显示成中文
        verbose_name_plural = verbose_name #不加复数s
        
    def __str__(self): #覆盖父类的方法
        return self.name #显示这条数据的指定名字，否则默认返回XXObject
    
class Author(models.Model):
    name = models.CharField(max_length=30)

class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1,choices=((0,'男'),(1,'女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    