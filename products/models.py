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

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title


class File(models.Model):
    # class variable with upper case character => برای کوئری زدن بهتر است از عدد استفاده کنیم تا حروف
    File_AUDIO = 1
    File_VIDEO = 2
    File_PDF = 3
    File_TYPES = (
        (File_AUDIO, _('audio')),
        (File_VIDEO, _('video')),
        (File_PDF, _('pdf'))
    )

    product = models.ForeignKey('Product', verbose_name=_('product'),related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file_type = models.SmallIntegerField(verbose_name=_('file_type'), choices=File_TYPES, default=File_VIDEO, blank=True)      # choices, give us dropdownlist
    file = models.FileField(_('file'), upload_to='files/%y/%m/%d/')
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    update_time = models.TimeField(_('update_time'), auto_now=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title

