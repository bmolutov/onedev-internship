from django.db import models

from custom_auth.models import CustomUser


class Order(models.Model):
    SENT = 'Отправлен'
    REFUSAL = 'Отказ'
    SOON = 'Скоро свяжемся'
    ACCEPTED = 'Принят в работу'
    STATUSES = (
        (SENT, SENT),
        (REFUSAL, REFUSAL),
        (SOON, SOON),
        (ACCEPTED, ACCEPTED)
    )

    title = models.CharField(
        max_length=256
    )
    description = models.TextField(
        max_length=4096,
        null=True,
        blank=True
    )
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=STATUSES,
        default=SENT,
        max_length=32
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
