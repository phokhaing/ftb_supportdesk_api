from django.db import models


class PositionModel(models.Model):
    name_en = models.CharField(max_length=100, null=False, unique=True)
    name_kh = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(blank=True, max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ftb_position'
        managed = True
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name_en
