from django.db import models


class Appliance(models.Model):
    """
    Appliance model representing an appliance in the system.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name='器具名')
    manufacture_name = models.CharField(max_length=255, verbose_name='メーカー名')
    model_number = models.CharField(max_length=255, verbose_name='型番')
    image = models.ImageField(upload_to='appliances/', verbose_name='器具画像')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    
    class Meta:
        verbose_name = '器具'
        verbose_name_plural = '器具一覧'


    def __str__(self):
        return self.name