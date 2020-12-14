
import requests
from lxml import etree
import time
import re
import json

if __name__ == '__main__':
    request_url = 'https://androidinvest.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        # 'cookie': 'TADCID=lFYI0DERinXfYEmnABQCjnFE8vTET66GHuEzPi7KfV8b4UVKRLzjVxaYOn1adUw2CIZPvoyOFfFPurjtG3vGyKDt0TVGhZvuJTk; TAUnique=%1%enc%3AE%2F6xEZjZtWNOQXRHBKil6M9tgeI3H2DEAPrVKjVZJJBQcF0be502LA%3D%3D; ServerPool=A; TASSK=enc%3AAJQGaKP8Lkoh%2B%2FeEo854qPNrqBhgwwSfMqoqKQCtaRPTKw2lfZpXE6tMhx8t%2BXb%2Bt8gjQMv0oaLB3VMRzNENNBjppMB43%2B5qS1WhsAW75gL2PaAT2cLBfH6fdezhaBgh9A%3D%3D; PMC=V2*MS.88*MD.20200729*LD.20200729; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CCOVIDMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CListMCSess%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPACMCSess%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CCOVIDMCPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CSPACMCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7C; TART=%1%enc%3ATkF0RwSopeiWS3dpZFWg9QuC%2FfzXPK4kHYKYdbTywp2Cyx09aj2C4hl0c3U3%2Fsl6oY993vi%2BhV0%3D; PAC=AEiKpmJ2XQ3SiQvATcEIUsqLpeV9dmeoQsZDLVGmIMfB3HaRx3oaemaci1AD1MHWiMojWXKO_SqZkWAlEen4pTdeNE-B9UzdNMtHy8CiCaCs9hwiICjVQndxcv0SwT4eG4OSGB0fMZpFgaKcadACzcql1e4E1h3EeuysSSeO1cLLF88j9xBisms02fw-JrBbKDc3ZasllrFs3TQloBtUo5Knfhr1CuVUmfoaSjkHQbRE; __gads=ID=a79e578453a3cb6a:T=1595997568:S=ALNI_MZ6XTVVNqoJ5MoOjhiYPmb3TFgnTQ; health_notice_dismissed=1; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; TATravelInfo=V2*AY.2020*AM.8*AD.20*DY.2020*DM.8*DD.21*A.2*MG.-1*HP.2*FL.3*DSM.1595997900109*RS.1; TAReturnTo=%1%%2FAttractions-g261667-Activities-a_allAttractions.true-Torquay_Victoria.html; __vt=_xGUFOqPEYqPIbCWABQCq4R_VSrMTACwWFvfTfL3vw75pqzIB0P3Xxn3sJJgqjJl9aNGVeLUKHai-qjzX-gBOQa-koRo5_SKcSUkCn7sQWuTtxlq-rU3-9dR15Sw4e70-rDSkZ5ninTRAhXWDR6RfKtZ; TASession=%1%V2ID.5176877FD2AF5EE647E573CC917B86F8*SQ.141*PR.40185%7CRegistrationController*LS.PageMoniker*GR.39*TCPAR.87*TBR.90*EXEX.55*ABTR.58*PHTB.51*FS.18*CPU.43*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.en*FA.1*DF.0*IR.1*OD.null*TRA.false*LD.261667*EAU._; TAUD=LA-1595997402902-1*RDD-1-2020_07_29*HDD-399955-2020_08_09.2020_08_10*ARDD-497712-2020_08_20.2020_08_21*LD-2229617-2020.8.20.2020.8.21*LG-2229619-2.1.F.; roybatty=TNI1625!AHQbkUBtLPiawzOZ%2F7wpoXPAb2KjT95PENvPSl2v8%2Br%2B0Ptj7HniSqoStYsk1qBfPAR0wiTFs8yyR5624A5xb%2FTnCr9eJQz6wZn3Ofl7ouVJQjmJzNWalHJ0NwZvdHZ6uEbV4goWrkWpEnvqLC9xRI812GF3AdPFaeRTnKF6hPoD%2C1'
    }
    parser = etree.HTMLParser()
    page = requests.get(url=request_url, headers=headers)
    html = page.content
    # html_doc = html.text.encode('utf-8')
    html_doc=str(html,'utf-8')
    tree = etree.HTML(html_doc)
    javascript = tree.xpath(
        '//div[@class="container"]//script[@type="text/javascript"]')
    # ss = javascript[0].text
    josndata = re.search('showSectorMap\((.+)\); }\)\(\);', javascript[0].text)
    if josndata:
        found = josndata.group(1)
        chartNestedData = eval(found)
        json_object = json.dumps(chartNestedData, indent=4,ensure_ascii=False)
        with open("StockDataset/chartNestedData.json", "w") as outfile:
            outfile.write(json_object)
    print('a')