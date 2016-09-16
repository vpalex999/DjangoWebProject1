from django.db import models


# Таблица закладок верхнего меню TAB
class bookmarks(models.Model):
    nametab=models.CharField('Раздел TAB', max_length = 30, unique = True)
   
    def __str__(self):
        return self.nametab
    # отображение в административном сайте:
    class Meta:
        ordering = ["id"]  # сортировка по полю id
        verbose_name = "Название Раздела" # шапка таблицы при отображении строк
        verbose_name_plural = "Верхнее меню TAB - разделы закладок" # имя таблицы

    

# Таблица подменю закладок TAB. Содержит топики и привязку к TAB закладкам, разделам
class bookmarksubmenu(models.Model):
    namesub = models.CharField('Название подменю', max_length=30, unique = True) # хранит название топика(подменю)
    nametabsubmenu = models.ForeignKey(bookmarks, null = True, blank = True, on_delete=models.SET_NULL, verbose_name='Раздел:') # топик может быть привязан к закладке TAB (хранит ключ выбранной закладки nametab таблицы bookmarks
    
    def __str__(self):
        return self.namesub 


    # отображение в административном сайте:
    class Meta:
        ordering = ["nametabsubmenu"]  # сортировка по полю id
        verbose_name = "Топики подменю" # Топики подменю
        verbose_name_plural = "Подменю" # имя таблицы