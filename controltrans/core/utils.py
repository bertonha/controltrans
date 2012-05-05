from BeautifulSoup import BeautifulStoneSoup

from controltrans.core.models import Cliente, Endereco, Fornecedor, \
                                     Transportadora


def field_text(field):
    if field is not None:
        return field.text
    return ''


def read_xml(filename):
    with open(filename, 'rt') as data:
        soup = BeautifulStoneSoup(data)
    return soup


def parse_endereco(soup):
    endereco = Endereco()
    endereco.rua = soup.xlgr.text
    endereco.numero = int(soup.nro.text)
    endereco.bairro = soup.xbairro.text
    endereco.cidade = soup.xmun.text
    endereco.uf = soup.uf.text
    endereco.cep = soup.cep.text
    endereco.save()
    return endereco


def parse_fornecedor(soup):
    xml = soup.emit
    try:
        fornecedor = Fornecedor.objects.get(cnpj=xml.cnpj.text)
    except Fornecedor.DoesNotExist:
        fornecedor = Fornecedor()
        fornecedor.nome = xml.xnome.text
        fornecedor.fantasia = xml.xfant.text
        fornecedor.cnpj = xml.cnpj.text
        fornecedor.ie = xml.ie.text
        fornecedor.fone = field_text(xml.fone)
        fornecedor.email = field_text(xml.email)
        fornecedor.endereco = parse_endereco(xml.enderemit)
        fornecedor.save()
    return fornecedor


def parse_client(soup):
    xml = soup.dest
    try:
        client = Cliente.objects.get(cnpj=xml.cnpj.text)
    except Cliente.DoesNotExist:
        client = Cliente()
        client.nome = xml.xnome.text
        client.fantasia = field_text(xml.xfant)
        client.cnpj = xml.cnpj.text
        client.ie = xml.ie.text
        client.fone = field_text(xml.fone)
        client.email = field_text(xml.email)
        client.endereco = parse_endereco(xml.enderdest)
        client.save()
    return client


def verify_carrier(soup):
    carrier = '637322284114'
    ie = soup.transporta.ie.text
    return carrier == ie
