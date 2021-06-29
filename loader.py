import csv
from GenDVApp.models import Gene, Disease, Variant

def run():
    fileHandler = open('data/GenesTable.csv')
    Reader = csv.reader(fileHandler)
    Gene.objects.all().delete()
    Disease.objects.all().delete()
    Variant.objects.all().delete()

    for row in Reader:
        g, created = Gene.objects.get_or_create(Chromosome=row[0], Start=row[1], End=row[2], 
            Symbol=row[3])
        g.save()

    fileHandler = open('data/DiseaseTable.csv')
    Reader = csv.reader(fileHandler)
    for row in Reader:
        d, created = Disease.objects.get_or_create(Name=row[0], Inheritance=row[1])
        d.Gene.set([Gene.objects.get(Symbol=row[2])])
        d.save()

    fileHandler = open('data/VariantTable.csv')
    Reader = csv.reader(fileHandler)
    for row in Reader:
        print("VariantTable.csv")
        print(row)
        v, created = Variant.objects.get_or_create(Chromosome=row[0], Position=row[1], Code=row[2], 
        Reference=row[3], Alternative=row[4], Gene=Gene.objects.get(Symbol=row[5]))
        v.save()

run()