from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description', 'avatar']


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id', 'file_type', 'title', 'file']

    # for how display file_type, as int or as string, we  add choice attribute in model verbose_name(string)
    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)       # this is Queryset for file relation with this obj and with related_name change the name from file_set to file
    pk = serializers.SerializerMethodField()  # this  Queryset for adding field to obj

    class Meta:
        model = Product
        fields = ['title', 'description', 'avatar', 'categories', 'files', "pk"]

    def get_pk(self, obj):
        return obj.id
