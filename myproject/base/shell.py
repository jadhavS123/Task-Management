# >python manage.py shell
# 7 objects imported automatically (use -v 2 for details).

# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64Type "help", "coType "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from base.models import Article
# >>>
# >>>
# >>> # CREATE
# >>>
# >>> a = Article(name = 'Rajat', desc = 'Senior Django Trainer')
# >>> a.save()
# >>>
# >>>
# >>> Article.objects.create(name = 'Saranya', desc = 'Data Analysis Trainer')
# <Article: Article object (6)>
# >>> 
# >>> 
# >>> 
# >>> # READ
# >>> 
# >>> # Extract the data, # Display the data
# >>> 
# >>> # 1) GET
# >>> 
# >>> a = Article.objects.get(id = 2)
# >>> a.id  
# 2
# >>> a.name
# 'Karnataka'
# >>> a.desc
# 'This is my home state.'
# >>>
# >>> # The data we fetch from db is complex data not a pure python data(dict).
# >>> 
# >>> 
# >>> 
# >>> # 2) ALL
# >>> 
# >>> a = Article.objects.all()
# >>> 
# >>> # To display the data you can use for loop or else indexing
# >>> 
# >>> a.id 
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'QuerySet' object has no attribute 'id'
# >>> a[0].id
# 1
# >>> a[1].name 
# 'Karnataka'
# >>> a[5].desc
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\saksh\OneDrive\Desktop\Django Batch\Django_batch_E10\Class\Article_Project\myenv\Lib\site-packages\django\db\models\query.py", line 436, in __getitem__
#     return qs._result_cache[0]
#            ~~~~~~~~~~~~~~~~^^^
# IndexError: list index out of range
# >>> 
# >>> 
# >>> for i in a:
# ...     print(i.title)
# ... 
# Traceback (most recent call last):
#   File "<console>", line 2, in <module>
# AttributeError: 'Article' object has no attribute 'title'
# >>> for i in a:
# ...     print(i.name)
# ... 
# India
# Karnataka
# Sakshi
# Rajat
# Saranya
# >>>
# >>> for i in a:
# ...     print(i.desc)
# ... 
# This is my country
# This is my home state.
# django trainer of Test yantra
# Senior Django Trainer
# Data Analysis Trainer
# >>> for i in a:
# ...     print(i.id, i.title, i.desc)
# ... 
# Traceback (most recent call last):
#   File "<console>", line 2, in <module>
# AttributeError: 'Article' object has no attribute 'title'
# >>> for i in a:
# ...     print(i.id, i.name, i.desc) 
# ... 
# 1 India This is my country
# 2 Karnataka This is my home state.
# 4 Sakshi django trainer of Test yantra
# 5 Rajat Senior Django Trainer
# 6 Saranya Data Analysis Trainer
# >>>
# >>> 
# >>> 
# >>> Article.objects.create(name = 'Saranya', desc = 'Python Trainer')       
# <Article: Article object (7)>
# >>>
# >>> 
# >>> # 3) FILTER
# >>> 
# >>> a = Article.objects.filter(name = 'Saranya')
# >>> a
# <QuerySet [<Article: Article object (6)>, <Article: Article object (7)>]>
# >>> for i in a:
# ...     print(i.id, i.name, i.desc)
# ... 
# 6 Saranya Data Analysis Trainer
# 7 Saranya Python Trainer
# >>>
# >>> 
# >>> 
# >>> 
# >>> # UPDATE Operation --- We can update only one record at a time.
# >>> 
# >>> # 2 steps --- Extract the data and Update the data
# >>> 
# >>> 
# >>> 
# >>> a = Article.objects.get(id = 7)
# >>> a.name = 'Sayantika'
# >>> a.save()
# >>> 
# >>> 
# >>> # Must and should you have to save the data then only data will be updated.
# >>> 
# >>> 
# >>> a = Article.objects.get(id = 7)
# >>> a.name = 'Saranya'  
# >>> a.save()
# >>> 
# >>> 
# >>> # DELETE
# >>> # 2 steps --- Extract the data and Delete the data
# >>> 
# >>> # Deleting single record
# >>> 
# >>> a = Article.objects.get(id = 4)
# >>> a.delete()
# (1, {'base.Article': 1})
# >>> 
# >>> 
# >>> # Deleting Duplicate Records
# >>> 
# >>> a = Article.objects.filter(name = 'Saranya')\
# ...
# ... 
# >>> a = Article.objects.filter(name = 'Saranya') 
# >>> a.delete()
# (2, {'base.Article': 2})
# >>>
# >>> 
# >>> # Deleting all the records
# >>> 
# >>> a = Article.objects.all()                   
# >>> a.delete()
# (3, {'base.Article': 3})