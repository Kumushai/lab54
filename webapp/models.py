from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True)
    description = models.TextField(max_length=2000, verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return f"{self.title}: {self.pk}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.TextField(max_length=2000, verbose_name="Описание", null=True, blank=True)
    category = models.ForeignKey("webapp.Category",
                                 on_delete=models.RESTRICT,
                                 verbose_name="Категория",
                                 related_name="products")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    image = models.CharField(max_length=500, verbose_name="Ссылка на картинку")
    balance = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Остаток", default=0)



    def __str__(self):
        return f"{self.pk} {self.title}: {self.category}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

