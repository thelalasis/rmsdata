from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

#单独建立的用户模型
class  user(models.Model):
  id = models.AutoField(primary_key = True)
  name =  models.CharField(max_length = 100)
  info = models.CharField(max_length = 200, default = "na")


#机型数据模型
class acmodel(models.Model):
    id = models.AutoField(primary_key = True)
    basic_acmodel = models.CharField("基本型号", max_length = 100)
    expanded_acmodel = models.CharField("扩展型号", max_length = 100)
    if_intra_ac = models.BooleanField(default = False)

    def __str__(self):
        return (self.basic_acmodel)

#事故数据模型
class accident(models.Model):
  id = models.AutoField(primary_key = True)
  title = models.CharField("标题", max_length=200)
  date = models.DateField("发生时间")
  content = models.TextField("事件描述")
  acmodel = models.ForeignKey(acmodel, on_delete = models.CASCADE)

  def __str__(self):
    return (self.title)

#术语定义部分内容
class term(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField("概词条念", max_length = 200)
    content = models.TextField("词条说明")
    acmodel = models.ForeignKey(acmodel, on_delete = models.CASCADE, limit_choices_to={'if_intra_ac': True})
    tag = TaggableManager("标签",blank=True)
    source = models.TextField("词条来源",blank=True)

    def __str__(self):
        return (self.title)
    
#数据来源说明模型    
class data_source(models.Model):
    id = models.AutoField(primary_key = True)
    #The title here represents the name of data source that has a series of data tables, each of them gathered in different time.
    title = models.CharField("title of data table", max_length = 200)
    slug = models.SlugField(max_length=200, unique=True)
    acmodel = models.ForeignKey(acmodel, on_delete = models.CASCADE)
    source_interpretation = models.CharField("Interpretation of the data source", max_length = 300)
                                 
    def __str__(self):
        return (self.title)

#历史数据表模型
class data_address(models.Model):                                                     
    id = models.AutoField(primary_key = True)
    title = models.CharField("download file address", max_length = 200)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField("发生时间")
    data_source = models.ForeignKey(data_source, on_delete = models.CASCADE)
                                                                    
    def __str__(self):
        #resolve the display problem 'Data_addresss' in admin's frontpage, but failed.
        return (self.title+'e')
