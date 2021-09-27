from django.db import models

# Create your models here.
class Conversion(models.Model):
    from_currency_code = models.CharField("From Code", max_length=100, blank=True, null=True)
    to_currency_code = models.CharField("To Code", max_length=100, blank=True, null=True)
    from_currency_name = models.CharField("From name", max_length=100, blank=True, null=True)
    to_currency_name = models.CharField("To Name", max_length=100, blank=True, null=True)
    exchange_rate = models.DecimalField("Exchange Rate",max_digits=15, decimal_places=8)
    updated_at = models.DateTimeField("Updated At",auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, blank=True, null=True)
    

    class Meta:
        verbose_name = 'Conversion'
        verbose_name_plural = 'Conversion'

    def __str__(self):
        return self.from_currency_code
