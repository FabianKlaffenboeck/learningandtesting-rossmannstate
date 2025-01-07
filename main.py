import requests


def get_header():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.rossmann-fotowelt.de/',
        'Content-Type': 'multipart/form-data; boundary=---------------------------29458574158622721754198924050',
        'Origin': 'https://www.rossmann-fotowelt.de',
        'Connection': 'keep-alive',
        # 'Cookie': 'OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+07+2025+12%3A42%3A16+GMT%2B0100+(Central+European+Standard+Time)&version=202403.2.0&browserGpcFlag=0&isIABGlobal=false&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CRM001%3A1&hosts=&genVendors=V12%3A1%2CV14%3A1%2CV10%3A1%2CV2%3A1%2CV27%3A1%2C&AwaitingReconsent=false&geolocation=%3B; OptanonAlertBoxClosed=2025-01-02T15:32:22.909Z; typo3=2428fe979dbe0426d2f669712f0ed32d; fe_typo_user=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoiODRkYWUwMTA0NzAxMDI1MTM4ZTcyYmE1MzdjNmEyYTQiLCJ0aW1lIjoiMjAyNS0wMS0wN1QxMjozOTowOCswMTowMCIsInNjb3BlIjp7ImRvbWFpbiI6Ind3dy5yb3NzbWFubi1mb3Rvd2VsdC5kZSIsImhvc3RPbmx5Ijp0cnVlLCJwYXRoIjoiLyJ9fQ.cck7oOzYIicnhJt_nqFKCy_tokLyioJgvNRgVM0UZL4; cip-epp=!6F54BeuU3V/3S3Hn4NzkrW44X+ce/Ua8TXUMlq67gQaO4o2CwOusMROlDlImmPG9tRs0WU33Yli/Lg==; TS015755b1=01728cf7ec2702e87495678cdb805c9f9da3af8edc7c5102312352a8546b661f7c2eecc0ac9f8f0069b7feae703f541bb041043177c01d921023fe4dff4746b7766996a1484ff437ea97c5b3b246d319342aaeb5ebb0b5e981a87e67da5578d52433dc40cc; TS0ff8479c027=0868f2544eab20005c3a70270c370df8fdfb43f703d7f9672c31f62aba54266f8aa29bba8571442508d4b600be113000a6977d24f6bf8baf7f1433099c0180e94c8bd4391742e580372565ad978b929c03cec304634bc46870a268e9a78c3202',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    return headers


def get_cookies():
    cookies = {
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Jan+07+2025+12%3A42%3A16+GMT%2B0100+(Central+European+Standard+Time)&version=202403.2.0&browserGpcFlag=0&isIABGlobal=false&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CRM001%3A1&hosts=&genVendors=V12%3A1%2CV14%3A1%2CV10%3A1%2CV2%3A1%2CV27%3A1%2C&AwaitingReconsent=false&geolocation=%3B',
        'OptanonAlertBoxClosed': '2025-01-02T15:32:22.909Z',
        'typo3': '2428fe979dbe0426d2f669712f0ed32d',
        'fe_typo_user': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoiODRkYWUwMTA0NzAxMDI1MTM4ZTcyYmE1MzdjNmEyYTQiLCJ0aW1lIjoiMjAyNS0wMS0wN1QxMjozOTowOCswMTowMCIsInNjb3BlIjp7ImRvbWFpbiI6Ind3dy5yb3NzbWFubi1mb3Rvd2VsdC5kZSIsImhvc3RPbmx5Ijp0cnVlLCJwYXRoIjoiLyJ9fQ.cck7oOzYIicnhJt_nqFKCy_tokLyioJgvNRgVM0UZL4',
        'cip-epp': '!6F54BeuU3V/3S3Hn4NzkrW44X+ce/Ua8TXUMlq67gQaO4o2CwOusMROlDlImmPG9tRs0WU33Yli/Lg==',
        'TS015755b1': '01728cf7ec2702e87495678cdb805c9f9da3af8edc7c5102312352a8546b661f7c2eecc0ac9f8f0069b7feae703f541bb041043177c01d921023fe4dff4746b7766996a1484ff437ea97c5b3b246d319342aaeb5ebb0b5e981a87e67da5578d52433dc40cc',
        'TS0ff8479c027': '0868f2544eab20005c3a70270c370df8fdfb43f703d7f9672c31f62aba54266f8aa29bba8571442508d4b600be113000a6977d24f6bf8baf7f1433099c0180e94c8bd4391742e580372565ad978b929c03cec304634bc46870a268e9a78c3202',
    }
    return cookies


def get_data(job_number, store_number):
    data = '-----------------------------29458574158622721754198924050\r\nContent-Disposition: form-data; name="bagid"\r\n\r\n' + str(
        job_number) + '\r\n-----------------------------29458574158622721754198924050\r\nContent-Disposition: form-data; name="outletid"\r\n\r\n' + str(
        store_number) + '\r\n-----------------------------29458574158622721754198924050\r\nContent-Disposition: form-data; name="ajax"\r\n\r\naimeos-frontend-api\r\n-----------------------------29458574158622721754198924050\r\nContent-Disposition: form-data; name="action"\r\n\r\nbagTracking\r\n-----------------------------29458574158622721754198924050--\r\n'
    return data


if __name__ == '__main__':
    response = requests.post('https://www.rossmann-fotowelt.de/',
                             cookies=get_cookies(),
                             headers=get_header(),
                             data=get_data(888621, 3678))
    print(response.text)
