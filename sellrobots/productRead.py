class Product:
    """information of a product"""
    def __init__(self, text):
        self.keywordSearchReturn = text['keywordSearchReturn']
        self.numberOfResults = self.keywordSearchReturn['numberOfResults']

        if self.numberOfResults == 0:
            return

        self.products = self.keywordSearchReturn['products'][0]
        self.sku = self.products.get('sku', 0)
        self.unitOfMeasure = self.products.get('unitOfMeasure', 0)
        self.displayName = self.products.get('displayName', 0)
        self.publishingModule = self.products.get('publishingModule', 0)
        self.packSize = self.products.get('packSize', 0)
        translatedMinimumOrderQuality = self.products.get('translatedMinimumOrderQuality', 0)
        self.translatedManufacturerPartNumber = self.products.get('translatedManufacturerPartNumber', 0)
        self.brandName = self.products.get('brandName', 0)
        self.translatedPrimaryCatalogPage = self.products.get('translatedPrimaryCatalogPage', 0)
        self.product_id = self.products.get('id', 0)

def getProductInfo(text):
    
    keywordSearchReturn = text['keywordSearchReturn']
    numberOfResults = keywordSearchReturn['numberOfResults']

    return keywordSearchReturn

    if numberOfResults == 0:
        return keywordSearchReturn.update({'products': 0})

    return keywordSearchReturn

    products = keywordSearchReturn['products']
    products['numberOfResults'] = numberOfResults
    return products
    products = self.keywordSearchReturn['products'][0]
    sku = self.products.get('sku', 0)
    unitOfMeasure = self.products.get('unitOfMeasure', 0)
    displayName = self.products.get('displayName', 0)
    publishingModule = self.products.get('publishingModule', 0)
    packSize = self.products.get('packSize', 0)
    translatedMinimumOrderQuality = self.products.get('translatedMinimumOrderQuality', 0)
    translatedManufacturerPartNumber = self.products.get('translatedManufacturerPartNumber', 0)
    brandName = self.products.get('brandName', 0)
    translatedPrimaryCatalogPage = self.products.get('translatedPrimaryCatalogPage', 0)
    product_id = self.products.get('id', 0)


def test():
    "completely test"
    print "welcome to test!"

class FarnellApiConf:
    """Farnell AII configure"""
    prefix = 'https://api.element14.com/catalog/products?'
    apiKey = 'callInfo.apiKey='
    dataFormat = 'callInfo.responseDataFormat='
    callback = 'callInfo.callback='
    term = 'term='
    store = 'storeInfo.id='
    sig = 'userInfo.signature='
    timestamp = 'userInfo.timestamp='
    billAccNum = 'userInfo.billAccNum='
    customerId = 'userInfo.customerId='
    contractId = 'userInfo.contractId='
    offset = 'resultsSettings.offset='
    numberOfResults = 'resultsSettings.numberOfResults='
    filters = 'resultsSettings.refinements.filters='
    resGroup = 'resultsSettings.responseGroup='
    xmlSchema = 'callInfo.omitXmlSchema='
    privateKey = 'pafnecce4mpnfkfqceeexzxd'

FarnellUrlConf = {
    'callInfo.apiKey=': 'fnecce4mpnfkfqceeexzxd',
    'callInfo.responseDataFormat':'json',
    'callInfo.callback':'',
    'term':'',
    'storeInfo.id':'uk.farnell.com',
#    'userInfo.signature':'',\
#    'userInfo.timestamp':'',\
    'userInfo.billAccNum':'',
    'userInfo.customerId':'',
    'userInfo.contractId':'',
    'resultsSettings.offset':'0',
    'resultsSettings.numberOfResults':'10',
    'resultsSettings.refinements.filters':'',
    'resultsSettings.responseGroup':'large',
    'callInfo.omitXmlSchema':'',
    'callInfo.apiKey':'pafnecce4mpnfkfqceeexzxd',
}

def getFarnellRequestUrl(termType, keyword, offset):
#    url = FarnellApiConf.prefix + FarnellApiConf.apiKey + FarnellApiConf.privateKey
#   url += '&' + FarnellApiConf.dataFormat + 'json'
#    if termType == 'keyword':
#        url += '&' + FarnellApiConf.term + 'any:' + keyword
#    url += '&' + FarnellApiConf.callback + ''
#    url += '&' + FarnellApiConf.store + 'uk.farnell.com'
#    url += '&' + FarnellApiConf.offset + '0'
#    url += '&' + FarnellApiConf.numberOfResults + '10'
#    url += '&' + FarnellApiConf.filters + ''
#    url += '&' + FarnellApiConf.resGroup + 'small'
#    url += '&' + FarnellApiConf.xmlSchema + ''
    if termType == 'keyword':
        FarnellUrlConf['term'] = 'any:' + keyword
    FarnellUrlConf['resultsSettings.offset'] = offset
    url = FarnellApiConf.prefix + '&'.join(["%s=%s" % (k, v) for k, v in FarnellUrlConf.items()])
    return url
