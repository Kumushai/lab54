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
    balance = models.IntegerField(verbose_name="Остаток", default=0)



    def __str__(self):
        return f"{self.pk} {self.title}: {self.category}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    product = models.ForeignKey("webapp.Product",
                                 on_delete=models.CASCADE,
                                 verbose_name="Продукт",
                                 related_name="products")

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"


class Order(models.Model):
    products = models.ManyToManyField('webapp.Product', through='OrderProduct')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderProduct(models.Model):
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order.pk}, Product: {self.product.title}"
