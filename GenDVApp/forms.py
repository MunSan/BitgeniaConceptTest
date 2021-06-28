from django import forms
from .models import Gene, Disease, Variant

#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class GeneForm(forms.ModelForm):
    class Meta:
        model = Gene
        fields = ['Chromosome', 'Start', 'End','Symbol', 'Disease', 'Variant']
        labels = {
            'Chromosome':'Chromosome',
            'Start':'Start position',
            'End':'End position',
            'Symbol':'Gene symbol',
            'Disease': 'Diseases related to this gene',
            'Variant': 'Variants of this gene',
        }

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['Name', 'Inheritance', 'Gene']
        labels = {
            'Name': 'Disease name',
            'Inheritance': 'Mendelian inheritance mode',
            'Gene': 'Genes related to this disease',
        }

class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ['Chromosome', 'Position', 'Reference','Alternative', 'Code', 'Gene']
        labels = {
            'Chromosome': 'Chromosome',
            'Position': 'SNP Position',
            'Reference': 'Allele reference',
            'Alternative': 'Alternative allele',
            'Code': '\"rs\" code',
            'Gene': 'Gene'
        }
