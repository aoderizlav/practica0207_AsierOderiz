import urllib.request
countries_pib = []

def open_url(url):
    file = urllib.request.urlopen(url)
    lines = []
    for line in file:
        lines.append(str(line.decode("utf-8")))
    claves = lines[0].split("\t")
    for line in lines[1:]:
        country = {}
        valores = line.split("\t")
        for id in range(len(claves)):
            country[claves[id]] = valores[id]
        countries_pib.append(country)

    print(countries_pib)
    return

lo = input(open_url('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'))
print(lo)