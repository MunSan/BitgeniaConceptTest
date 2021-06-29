from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from .forms import GeneForm, DiseaseForm, VariantForm
from .models import Gene, Disease, Variant

#---------------- Gene Views ----------------
@login_required()
def CreateGeneView(request):
    if request.method == 'POST':
        form = GeneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/genes')
    else:
        form = GeneForm()
    context = {'form':form}
    return render(request, 'genes/create_gene.html', context)

@login_required()
def RetrieveGeneListView(request):
    dataset = Gene.objects.all()
    return render(request, 'genes/gene_list.html', {'dataset':dataset})

@login_required()
def RetrieveGeneDetailView(request,_id):
    try:
        data = Gene.objects.get(id=_id)
        queryD = Disease.objects.filter(Gene = data)
        queryD = [*queryD]
        queryV = Variant.objects.filter(Gene = data)
        queryV = [*queryV]
    except Gene.DoesNotExist:
        raise Http404('This gene does not exist')
    context = {'data':data, 'diseases':queryD, 'variants':queryV}

    return render(request, 'genes/gene_detail.html', context)

@login_required()
def UpdateGeneView(request,_id):
    try:
        old_data = get_object_or_404(Gene,id=_id)
    except Exception:
        raise Http404('This gene does not exist')

    if request.method == 'POST':
        form = GeneForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/genes/{id}')
    else:
        form = GeneForm(instance=old_data)
        context = {'form':form, 'genid':_id}
        return render(request, 'genes/update_gene.html', context)

@login_required()
def DeleteGeneView(request,_id):
    try:
        data = get_object_or_404(Gene,id=_id)
    except Exception:
        raise Http404('This gene does not exist')

    if request.method == 'POST':
        data.delete()
        return redirect('/genes')
    else:
        return render(request, 'genes/delete_gene.html')

#---------------- Disease Views ----------------
@login_required()
def CreateDiseaseView(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/diseases')
    else:
        form = DiseaseForm()
    context = {'form':form}
    return render(request, 'diseases/create_disease.html', context)

@login_required()
def RetrieveDiseaseListView(request):
    dataset = Disease.objects.all()
    return render(request, 'diseases/disease_list.html', {'dataset':dataset})

@login_required()
def RetrieveDiseaseDetailView(request,_id):
    try:
        data = Disease.objects.get(pk=_id)
        queryG = Gene.objects.filter(Disease = data)
        queryG = [*queryG]
    except Disease.DoesNotExist:
        raise Http404('This disease does not exist')
    context = {'data':data, 'genes':queryG}

    return render(request, 'diseases/disease_detail.html', context)

@login_required()
def UpdateDiseaseView(request,_id):
    try:
        old_data = get_object_or_404(Disease,id=_id)
    except Exception:
        raise Http404('This gene does not exist')

    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/diseases/{id}')
    else:
        form = DiseaseForm(instance=old_data)
        context = {'form':form, 'diseid':_id}
        return render(request, 'diseases/update_disease.html', context)

@login_required()
def DeleteDiseaseView(request,_id):
    try:
        data = get_object_or_404(Disease,id=_id)
    except Exception:
        raise Http404('This disease does not exist')

    if request.method == 'POST':
        data.delete()
        return redirect('/diseases')
    else:
        return render(request, 'diseases/delete_disease.html')

#---------------- Variant Views ----------------
@login_required()
def CreateVariantView(request):
    if request.method == 'POST':
        form = VariantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/variants')
    else:
        form = VariantForm()
    context = {'form':form}
    return render(request, 'variants/create_variant.html', context)

@login_required()
def RetrieveVariantListView(request):
    dataset = Variant.objects.all()
    return render(request, 'variants/variant_list.html', {'dataset':dataset})

@login_required()
def RetrieveVariantDetailView(request,_id):
    try:
        data = Variant.objects.get(pk=_id)
        queryG = Gene.objects.filter(Variant = data)
        queryG = [*queryG]
    except Variant.DoesNotExist:
        raise Http404('This variant does not exist')
    context = {'data':data, 'genes':queryG}

    return render(request, 'variants/variant_detail.html', context)

@login_required()
def UpdateVariantView(request,_id):
    try:
        old_data = get_object_or_404(Variant,id=_id)
    except Exception:
        raise Http404('This variant does not exist')

    if request.method == 'POST':
        form = VariantForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/variant/{id}')
    else:
        form = VariantForm(instance=old_data)
        context = {'form':form, 'varid':_id}
        return render(request, 'variants/update_variant.html', context)

@login_required()
def DeleteVariantView(request,_id):
    try:
        data = get_object_or_404(Variant,id=_id)
    except Exception:
        raise Http404('This variant does not exist')

    if request.method == 'POST':
        data.delete()
        return redirect('/variants')
    else:
        return render(request, 'variants/delete_variant.html')

# Hago otra vista para llamar a la template general.
# En esta vista voy a manejar los 3 formularios para llamarlos en el template.

@login_required()
def QueryView(request,_id):
    formGen = GeneForm(request.POST)
    formDis = DiseaseForm(request.POST)
    formVar = VariantForm(request.POST)

    if formGen.is_valid():
        try:
            data = get_object_or_404(Gene,id=_id)
        except Exception:
            raise Http404('This gene does not exist')

        if request.method == 'POST':
            form = GeneForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('/query')
        else:
            form = GeneForm(instance=data)
            context = {'form':form}
            return render(request, 'genes/gene_detail.html', context)
    elif formDis.is_valid():
        try:
            data = get_object_or_404(Disease,id=_id)
        except Exception:
            raise Http404('This disease does not exist')

        if request.method == 'POST':
            form = DiseaseForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('/query')
        else:
            form = DiseaseForm(instance=data)
            context = {'form':form}
            return render(request, 'diseases/disease_detail.html', context)
    elif formVar.is_valid():
        try:
            data = get_object_or_404(Gene,id=_id)
        except Exception:
            raise Http404('This variant does not exist')

        if request.method == 'POST':
            form = VariantForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('/query')
        else:
            form = VariantForm(instance=data)
            context = {'form':form}
            return render(request, 'variants/variant_detail.html', context)
