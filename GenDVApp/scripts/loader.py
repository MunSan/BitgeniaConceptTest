import csv
from GenDVApp.models import Gene, Disease, Variant

def run():
    fileHandler = open('data/GenesTable.csv')
    Reader = csv.reader(fileHandler)
    Gene.objects.all().delete()
    Disease.objects.all().delete()
    Variant.objects.all().delete()

    for row in Reader:
        print("GenesTable.csv")
        print(row)
        g, created = Gene.objects.get_or_create(Symbol=row[3])
        d, created = Disease.objects.get_or_create(Name=row[4])
        v, created = Variant.objects.get_or_create(Code=row[5])
        gT = Gene(Chromosome=row[0], Start=row[1], End=row[2], 
            Symbol=row[3], Disease=row[4], Variant=row[5])
        gT.save()

    fileHandler = open('data/DiseaseTable.csv')
    Reader = csv.reader(fileHandler)
    for row in Reader:
        print("DiseasesTable.csv")
        print(row)
        g, created = Gene.objects.get_or_create(Symbol=row[2])
        d, created = Disease.objects.get_or_create(Name=row[0])
        dT = Disease(Name=row[0], Inheritance=row[1], Gene=row[2])
        dT.save()

    fileHandler = open('data/VariantTable.csv')
    Reader = csv.reader(fileHandler)
    for row in Reader:
        print("VariantTable.csv")
        print(row)
        g, created = Gene.objects.get_or_create(Symbol=row[5])
        v, created = Variant.objects.get_or_create(Code=row[2])
        vT = Variant(Chromosome=row[0], Position=row[1], Code=row[2], 
        Reference=row[3], Alternative=row[4], Gene=row[5])
        vT.save()