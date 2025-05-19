from django.db import models


class Button(models.Model):
    """
    ボタンのモデル
    """
    name = models.CharField(max_length=255, verbose_name='ボタン名')
    appliance = models.ForeignKey(
        'appliances.Appliance',
        on_delete=models.CASCADE,
        related_name='buttons',
        verbose_name='器具'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    class Meta:
        verbose_name = 'ボタン'
        verbose_name_plural = 'ボタン一覧'

    def __str__(self):
        return self.name


class Angle(models.Model):
    """
    ボタンの角度のモデル
    """
    button = models.ForeignKey(Button, on_delete=models.CASCADE, related_name='angles', verbose_name='ボタン')
    joint_id = models.IntegerField(verbose_name='関節ID')
    degree = models.IntegerField(verbose_name='角度')
    speed = models.IntegerField(verbose_name='速度')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    class Meta:
        verbose_name = 'ボタンの角度'
        verbose_name_plural = 'ボタンの角度一覧'

    def __str__(self):
        return f'{self.button.name} - {self.joint_id}'