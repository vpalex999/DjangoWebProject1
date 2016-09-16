from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"] # сортировка по полю
        verbose_name = "Категория" # шапка таблицы при отображении строк
        verbose_name_plural = "Категории товара" # имя таблицы
    




class Good(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    in_stock = models.BooleanField(default = True, db_index=True, verbose_name = "В наличии")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = 'Категория товара')

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s=s+" (нет в наличии)"
        return s

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else: return ""

# отображение в административном сайте:
    class Meta:
        ordering = ["name"] # сортировка по полю
        unique_together = ("category", "name") # уникальность поля
        verbose_name = "Товар" # шапка таблицы при отображении строк
        verbose_name_plural = "Товары" # имя таблицы


    