from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import *
from .utils import *


def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def load_xml(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            soup = read_xml(request.FILES['file'])
            fornecedor = parse_fornecedor(soup)
            cliente = parse_client(soup)
            return render_to_response('confirme.html',
                                      {'fornecedor': FornecedorForm(instance=fornecedor),
                                       'cliente': ClienteForm(instance=cliente)})
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
