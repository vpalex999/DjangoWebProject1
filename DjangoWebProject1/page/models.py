from django.db import models

# Таблица Category с полями описывающими категории товара
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
# Таблица Good описывающая товар   
class Good(models.Model):
    name = models.CharField(max_length = 50, unique = True, verbose_name = 'Название')
    description = models.TextField(verbose_name = "Краткое описание")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(set):
        s=set.name
        if not self.in_stock:
            s=s+" (нет в наличии)"
        return s
    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else: return "-"
        
