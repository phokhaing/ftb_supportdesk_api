from django.db import models


class BranchModel(models.Model):
    code = models.CharField(max_length=9, null=False, unique=True)
    name_en = models.CharField(max_length=100, null=False, unique=True)
    name_kh = models.CharField(max_length=100, null=False, unique=True)
    address_en = models.TextField(blank=False, max_length=500)
    address_kh = models.TextField(blank=False, max_length=500)
    description = models.TextField(blank=True, max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ftb_branch'
        managed = True
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name_en
