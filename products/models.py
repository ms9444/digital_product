from django.db import models
from django.utils.translation import gettext_lazy as _  #gettext برای view lazy برای مدل #


class Category(models.Model):
    # self = when model forginley itself this option is set
    # null>true = its mean field in table can be null
    # blanc>true = its mean field in Form can be null,no validation Error
    # on_delete = how biheiver when fild is delete- cascade= we delete with other specification like Comments

    parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    # upload_to> where avatar save
    avatar = models.ImageField(verbose_name=_('avatar'), blank=True, upload_to='category/')
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    # auto_now_add>take now date time in form
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    update_time = models.TimeField(_('update_time'), auto_now=True)

    # table option
    class Meta:
        db_table = 'Category'
        verbose_name = _('category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), blank=True, upload_to='product/')
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    update_time = models.TimeField(_('update_time'), auto_now=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%y/%m/%d/')
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    update_time = models.TimeField(_('update_time'), auto_now=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')

