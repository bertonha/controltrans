from bs4 import BeautifulSoup

from controltrans.core.models import Cliente, Endereco, Fornecedor, \
                                     Transportadora


def field_text(field):
    if field is not None:
        return field.text
    return ''


def read_xml(filename):
    with open(filename, 'rt') as data:
        soup = BeautifulSoup(data, features='xml')
    return soup


def parse_endereco(soup):
    endereco = Endereco()
    endereco.rua = soup.xLgr.text
    endereco.numero = int(soup.nro.text)
    endereco.bairro = soup.xBairro.text
    endereco.cidade = soup.xMun.text
    endereco.uf = soup.UF.text
    endereco.cep = soup.CEP.text
    endereco.save()
    return endereco


def parse_fornecedor(soup):
    xml = soup.emit
    try:
        fornecedor = Fornecedor.objects.get(cnpj=xml.CNPJ.text)
    except Fornecedor.DoesNotExist:
        fornecedor = Fornecedor()
        fornecedor.nome = xml.xNome.text
        fornecedor.fantasia = xml.xFant.text
        fornecedor.cnpj = xml.CNPJ.text
        fornecedor.ie = xml.IE.text
        fornecedor.fone = field_text(xml.fone)
        fornecedor.email = field_text(xml.email)
        fornecedor.endereco = parse_endereco(xml.enderEmit)
        fornecedor.save()
    return fornecedor


def parse_client(soup):
    xml = soup.dest
    try:
        client = Cliente.objects.get(cnpj=xml.CNPJ.text)
    except Cliente.DoesNotExist:
        client = Cliente()
        client.nome = xml.xNome.text
        client.fantasia = field_text(xml.xFant)
        client.cnpj = xml.CNPJ.text
        client.ie = xml.IE.text
        client.fone = field_text(xml.fone)
        client.email = field_text(xml.email)
        client.endereco = parse_endereco(xml.enderDest)
        client.save()
    return client


def verify_carrier(soup):
    carrier = '637322284114'
    ie = soup.transporta.IE.text
    return carrier == ie
