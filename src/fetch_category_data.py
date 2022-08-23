import requests

search_string = 'men-formal-shirts'
host = 'https://www.myntra.com/gateway/v2/search/'

def get_headers():
    headers = {
        'content-type': 'application/json',
        'cookie': '_ga=GA1.2.1678700689.1660729809; ajs_anonymous_id=bc38f1bc-446c-48cd-ae66-8ecd32f9d3ca; ajs_user_id=c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB; bc=true; _d_id=d1b5def3-1a43-41b7-8851-07873644d628; mynt-eupv=1; _gcl_au=1.1.433464726.1660914224; tvc_VID=1; _fbp=fb.1.1660914224900.857102999; _gid=GA1.2.1310205691.1661142008; _cc_id=c28b639646f44757bd62a52750457111; __cab=cart.fsexp%3D; ftc=false; sc_tt=true; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; ilgim=true; user_uuid=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; oai=144652047; oaui=144652047:191149625; uidx=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; mynt-ulc=pincode%3A110085%7CaddressId%3A144652047; mynt-ulc-api=pincode%3A110085%7CaddressId%3A144652047; bm_sz=56A9340D1C4E7F4B715B3BE194DCF456~YAAQL13SF4NPUrSCAQAAKSxzyRBhhxPUQAXH2n6HBAKAC2Saq500KRloE5VJUhcIxquN5HlbahGTcA0Gy2nHvYCAO4zRRiGGYg4+zTmXNl37wKYp1ynQL7l2b2uVGGypDbH1r9Tdyy62gk+BDtmu4FnAb+Gb24v/FYBUARjPPqSqRcolaaOvxhmQkNk0aXBTCFC/hYImQJIlemrs1doKRpmzUgeU1sKmRo6FYdhJNOf3jAVhTrRT0iUkrSjfMK3nO1luI2A8vEgYZVe4kDx3v+rjpgnGNdqXxql3WaJT3NiUVZ8=~3552065~4403764; panoramaId_expiry=1661323554134; vw=400; vh=984; webVitals=true; _ma_session=%7B%22id%22%3A%228cc94ee4-21ee-4c92-9219-22aff4ed964f-d1b5def3-1a43-41b7-8851-07873644d628%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; mynt-loc-src=expiry%3A1661244050927%7Csource%3AUSER; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.desktop.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661244651%2C%22trackend%22%3A1661244711%7D; lt_timeout=1; lt_session=1; at=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1Jd05XVmxNelU0TFRWbFpEQXROR0ZpT1MxaVlUSXhMV05rTnpoaFpEZzROek5tTlMweE5qWXhNVFE1T0RNMk5URTJJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJME9ESTFNU3dpYm1sa2VDSTZJalU1T0dJMk5UWTNMVEZtWW1ZdE1URmxaQzA1TVRnNExUVmhPRGxsT1RsbVpUSm1OU0lzSW1saGRDSTZNVFkyTVRJME5EWTFNU3dpZFdsa2VDSTZJbVE0TjJJNU9XVTRMakE1WXpJdU5EZ3pZeTQ0TWpjd0xqZGlNV1ZtWXpNNU9HVTBOMGhEU2pOUVJVdHljM0FpZlEuSmRvX3hBMUloVVpqSHI0VTgzXzF6X2hMUklXaEI3ZWJpZWh3YWRxTEtoUnZjSC1wcHFFaXplcVZybDVDVjNITHlIQ1p3VnlENGhMRUhrNndZR2s4ZERzVkJoU05uSE5xdW1Id2pxS2Etd0w2RE82dE42OTEyMzB5WjVLdm1XR0U4QUcyMk4zWV9QazlNUm02cWtHMTZNb0NFLWwyNzVfdlBsbzBNVkwxVDU0; rt=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUppTURWbFpUTTFPQzAxWldRd0xUUmhZamt0WW1FeU1TMWpaRGM0WVdRNE9EY3paalV0TVRZMk1URTBPVGd6TmpVeE5pSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpRME5qVXhMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOVGN5TmpVeExDSnVhV1I0SWpvaU5UazRZalkxTmpjdE1XWmlaaTB4TVdWa0xUa3hPRGd0TldFNE9XVTVPV1psTW1ZMUlpd2lhV0YwSWpveE5qWXhNalEwTmpVeExDSjFhV1I0SWpvaVpEZzNZams1WlRndU1EbGpNaTQwT0ROakxqZ3lOekF1TjJJeFpXWmpNems0WlRRM1NFTktNMUJGUzNKemNDSjkuRlFUeW1odVJVaWFSZC1BMENnRXRtU1R4WnN1SUF1NGUyZHVjeFNNS3pXQmdSTnYxOUJubEZvU3JjYkZPZGd3ZHg1aVpFSnlIUjR1aTlya3VBSzlDVW5GN1BZaWM3ZE9rcDNwNlQ1WU5YWlBjd3ZuOW5VM1VFNTNnUU1CNm8xQlhWdHU2VkZKVk9GQmU0eUlUVlVac0lCZGI0WnNBWmQwOWZ6ZmJ0UHVzdk5F; AKA_A2=A; bm_mi=6EAD546B2F4F330E251274D19039653F~YAAQPl3SF1nXHLGCAQAAC8DlyRBP0vhxeCqOBbK+iuhm8D3ycvNUfszQQ1/ebdsLVSnkl6ddN2J2CWc3DQ0CP5kQqQRw64Sstb/5wCYNNvW46ustSYAmh6iuOnoH6B0h2PqT3tzi7UebZgxIgYMYaj9fHHAmz4sWyxdCnieQbCmifYVPC8z0d72PM4EGzYR7w+a7dPdPebV8DM84yX5mQGp9NJOFbqVsuzIufVmfkgJl/UPp/zLmrSKZeOCwaVL+UVF+Qn0RXzixEO9FOsATzzba4f/cqwvRuopI+hnPHEJaEVJVLolNCkijB+Fdsp+/DTc78EcXA1K6mZvpCwSM/TtLzX7qPRNMaLe55I8AAC7o~1; _abck=DD57C38A5F8F116708A48B6891EF6911~0~YAAQPl3SF5/XHLGCAQAAy8LlyQg6zF6mrKxS5uTUdWmjJG/pOGfEgokdTQCKDfXNJZZC4neEiv5tZuClRjzopdA1KNCK8MG/jWYCKa6O3pFoukfTPWciw0udpzt9264Off8b+B1VnxLdc+Uwk2FNqKqFSA9P2xSBEoER7DFNfVXSvCOhknsFroJtVMhJKE3AtSik5KFp1qrFfeZDxtq+47F53XUFf5eQ3YrOJtBBjAiRXg4MHliTT3vexbb1KcJ/y3K6e1ou3OlMMgk402GbEJSpM1A5QqirNs4zC5qWLL7kwHmQgPWhdTLZ/uBrbfa0vnXq98mw1ovHXajpi4/axdV3GecqGfjOYvygwn/peQejcrAvxFKnxpCKQyQ86PsAMEyY4LrspXHF29wNq7glaE+8o1TcL2Z5~-1~-1~1661248239; microsessid=688; ru=Qk1QUHRUMVBYcW8bEUAIdnxcC3obZxoDVAdbIhdeRFUQP1B9PCIPbQg1GgkRO0AwIzI2MDcyMzY1NDQkMg%3D%3D.95261449f92e59099afb53770bedde25; utrid=F0NRAnRcYFpEc2ZIFVdAMCMyNjA3MjM2NTQ0JDI%3D.a3c47e67b838bfc73a410a931339ff65; _xsrf=jFq3rwBJf9oRfEFCxiTIWseqcdbBZ7Rw; user_session=eshLPDbQnsLLfLnt6osAFw.iaaH8y2_0YwqkdouZtTenTLgLVXL5EGxPo1QO_d8qfBvqB88OgqnQ1UE-5jbbxReNTO6zjsQafpBCynq3dYyV3J3ZI7AwDzpZtNzeyYlCYz60LQwskIIEwurFbACNfnjJoYWL1UzxB3xLCkHXG2x8FLawgc0w3QQYATRcz7sdi2ZZedSIjEldpU9Pak62d4C6Va5K3oi_hq4UkGYNklDTOHJHAaXT6U63yMDVmmY4r1C_44gtU45PhRsrYW8v4X9Sgi5vQXPdH0vnDzXV1uIBGQwZjYWh-SVKgviIDSaDFzxmJMm5azPus8dXmOUxG0KXCDSTJuuURfB9f4WMsIRgHatCPhrG00iCM-17nY2bAzL-bm1CUcvs9MjJCPtSWD8gHYpIeosGC8HbnbNJFYd6dpkZJKaOdrOtC-mMjbZeFEJpVdUWo5iXjk2jXa8ifd9K39jvBKt6uzpCrFhXZDVyZLR9tZJ3BkH5NKLUqq33iKm3eEwZHQRhKg80sGGf4XD.1661244656387.86400000.4t0HgtoOkYptUoaF5n61IOMQ5r3hwvsZQXdjXNDGuKI; newUser=false; AMP_TOKEN=%24NOT_FOUND; ak_bmsc=3325E0963DC0B9E0007811FDDDE9343C~000000000000000000000000000000~YAAQPl3SF8/YHLGCAQAAeNPlyRA+LKfHVuXvtDAe9M8d1qvqpEyVlZ1QgB36Tfo7XE9Aljsz3YEJqAeE6yvfbZlOUuSxIUZk8BicbwG/dzUHLplwC0M+e3jluAejkv0NRsBIOPkTTRB/mbXO57iWU+Uh8lZ4dkPtDHN4yWMsPUUqPS0d4jVlfeWLVZn4HmgpynApN4XAHxAgc8/JMMAkWYmz8X/JYViB9CykvwjuBR5A7mL325fup105ACUySLz2wN/7skG7clSNW3e4BMv1gFmW1gVJcu3q9lxvH3mk5rdz3OiiBjk6t2q3+fgiuzH7XjkoExsA6rhUZTgH9exubeyYvUDZEr7ikxSROI/xNp11hBsxtmtCBSkPnXj84JbWbljczKOz5uOtHx8KNxNshYVIFkHY27//4YayI+75/JmspSxoaqlLtNpIBvm3gViyLXn6Oddy5qbfIKBTZsY9I68d9PveBD52z3VxygDBYCFGhkFOlpm0y9UuU3OqQanuIWOTa9OkJZF+s5SrzVaTuKktTQ2ipp/JXfvln0hpPCsKMcuRRQ==; bm_sv=E3522F96AC976EC1C79016FDCCA607DF~YAAQPl3SF9DYHLGCAQAAeNPlyRCeawKmNakPur9RvyQNg1Ps2xloWrMZPu+1BOP0CqFyJZdeFrs2ohM1MpGGpk0TgvIq1TtNHCM8FWEyqx9xdWsVDG+t6dSyr38+678q/F6Si1gnYIb3ah/Sj7O3cS0HaDJ/sTxJQsIluYZx8xsoj0ZUZs0hBpmb7qNHQ4VGbVWHSlFj5mikKgSslhy+2DmAUAh4XvU69c6k0SYSYC5uCacXHt6AISr8I/dS9b5e~1; _gat=1; cto_bundle=-XNaaF93Y1BsNFFkJTJCbjAlMkZVYkQ0WEpjNVVIRExPV3UyR2pxR0hkNmliNmE1SUxyUVdZeXRGN2tNS0Q0MW9mdEclMkZ6QVNYa3Jjd1J4ZE0xeE9vJTJGT3ZzNDkzNGZTJTJCZUYxaTJNRFJ0OFo5dkNLdjgyQjdGSUVyeEUxY3olMkYwQjcxdndNTU1NRFBHanUxb3Q2ODZ1ak1hTW8lMkJaT282QSUzRCUzRA; ak_RT="z=1&dm=myntra.com&si=a62de590-c921-4ffc-a255-ae47b67219aa&ss=l75y68nw&sl=1&tt=8o1&rl=1&ld=8o5&nu=46zaonao&cl=144f"'
    }
    return headers

def get_query_params():
    params = {
        'p': '1',
        'rows': '4',
        'o': '0',
        'plaEnabled': 'false'
    }
    return params

def get_url():
    return host + search_string

def get_category_data():
    print("sending req")
    # resp = requests.get(get_url(), params=get_query_params(), headers=get_headers())
    cookies = {
        '_ga': 'GA1.2.1678700689.1660729809',
        'ajs_anonymous_id': 'bc38f1bc-446c-48cd-ae66-8ecd32f9d3ca',
        'ajs_user_id': 'c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB',
        'bc': 'true',
        '_d_id': 'd1b5def3-1a43-41b7-8851-07873644d628',
        'mynt-eupv': '1',
        '_gcl_au': '1.1.433464726.1660914224',
        'tvc_VID': '1',
        '_fbp': 'fb.1.1660914224900.857102999',
        '_gid': 'GA1.2.1310205691.1661142008',
        '_cc_id': 'c28b639646f44757bd62a52750457111',
        '__cab': 'cart.fsexp%3D',
        'ftc': 'false',
        'sc_tt': 'true',
        'G_ENABLED_IDPS': 'google',
        'G_AUTHUSER_H': '0',
        'ilgim': 'true',
        'user_uuid': 'd87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp',
        'oai': '144652047',
        'oaui': '144652047:191149625',
        'uidx': 'd87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp',
        'mynt-ulc': 'pincode%3A110085%7CaddressId%3A144652047',
        'mynt-ulc-api': 'pincode%3A110085%7CaddressId%3A144652047',
        'bm_sz': '56A9340D1C4E7F4B715B3BE194DCF456~YAAQL13SF4NPUrSCAQAAKSxzyRBhhxPUQAXH2n6HBAKAC2Saq500KRloE5VJUhcIxquN5HlbahGTcA0Gy2nHvYCAO4zRRiGGYg4+zTmXNl37wKYp1ynQL7l2b2uVGGypDbH1r9Tdyy62gk+BDtmu4FnAb+Gb24v/FYBUARjPPqSqRcolaaOvxhmQkNk0aXBTCFC/hYImQJIlemrs1doKRpmzUgeU1sKmRo6FYdhJNOf3jAVhTrRT0iUkrSjfMK3nO1luI2A8vEgYZVe4kDx3v+rjpgnGNdqXxql3WaJT3NiUVZ8=~3552065~4403764',
        'panoramaId_expiry': '1661323554134',
        'vw': '400',
        'vh': '984',
        'webVitals': 'true',
        '_ma_session': '%7B%22id%22%3A%228cc94ee4-21ee-4c92-9219-22aff4ed964f-d1b5def3-1a43-41b7-8851-07873644d628%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
        'mynt-loc-src': 'expiry%3A1661244050927%7Csource%3AUSER',
        '_mxab_': 'checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.desktop.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled',
        '_pv': 'default',
        'dp': 'd',
        'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661244651%2C%22trackend%22%3A1661244711%7D',
        'lt_timeout': '1',
        'lt_session': '1',
        'at': 'ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1Jd05XVmxNelU0TFRWbFpEQXROR0ZpT1MxaVlUSXhMV05rTnpoaFpEZzROek5tTlMweE5qWXhNVFE1T0RNMk5URTJJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJME9ESTFNU3dpYm1sa2VDSTZJalU1T0dJMk5UWTNMVEZtWW1ZdE1URmxaQzA1TVRnNExUVmhPRGxsT1RsbVpUSm1OU0lzSW1saGRDSTZNVFkyTVRJME5EWTFNU3dpZFdsa2VDSTZJbVE0TjJJNU9XVTRMakE1WXpJdU5EZ3pZeTQ0TWpjd0xqZGlNV1ZtWXpNNU9HVTBOMGhEU2pOUVJVdHljM0FpZlEuSmRvX3hBMUloVVpqSHI0VTgzXzF6X2hMUklXaEI3ZWJpZWh3YWRxTEtoUnZjSC1wcHFFaXplcVZybDVDVjNITHlIQ1p3VnlENGhMRUhrNndZR2s4ZERzVkJoU05uSE5xdW1Id2pxS2Etd0w2RE82dE42OTEyMzB5WjVLdm1XR0U4QUcyMk4zWV9QazlNUm02cWtHMTZNb0NFLWwyNzVfdlBsbzBNVkwxVDU0',
        'rt': 'ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUppTURWbFpUTTFPQzAxWldRd0xUUmhZamt0WW1FeU1TMWpaRGM0WVdRNE9EY3paalV0TVRZMk1URTBPVGd6TmpVeE5pSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpRME5qVXhMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOVGN5TmpVeExDSnVhV1I0SWpvaU5UazRZalkxTmpjdE1XWmlaaTB4TVdWa0xUa3hPRGd0TldFNE9XVTVPV1psTW1ZMUlpd2lhV0YwSWpveE5qWXhNalEwTmpVeExDSjFhV1I0SWpvaVpEZzNZams1WlRndU1EbGpNaTQwT0ROakxqZ3lOekF1TjJJeFpXWmpNems0WlRRM1NFTktNMUJGUzNKemNDSjkuRlFUeW1odVJVaWFSZC1BMENnRXRtU1R4WnN1SUF1NGUyZHVjeFNNS3pXQmdSTnYxOUJubEZvU3JjYkZPZGd3ZHg1aVpFSnlIUjR1aTlya3VBSzlDVW5GN1BZaWM3ZE9rcDNwNlQ1WU5YWlBjd3ZuOW5VM1VFNTNnUU1CNm8xQlhWdHU2VkZKVk9GQmU0eUlUVlVac0lCZGI0WnNBWmQwOWZ6ZmJ0UHVzdk5F',
        'AKA_A2': 'A',
        'bm_mi': '6EAD546B2F4F330E251274D19039653F~YAAQPl3SF1nXHLGCAQAAC8DlyRBP0vhxeCqOBbK+iuhm8D3ycvNUfszQQ1/ebdsLVSnkl6ddN2J2CWc3DQ0CP5kQqQRw64Sstb/5wCYNNvW46ustSYAmh6iuOnoH6B0h2PqT3tzi7UebZgxIgYMYaj9fHHAmz4sWyxdCnieQbCmifYVPC8z0d72PM4EGzYR7w+a7dPdPebV8DM84yX5mQGp9NJOFbqVsuzIufVmfkgJl/UPp/zLmrSKZeOCwaVL+UVF+Qn0RXzixEO9FOsATzzba4f/cqwvRuopI+hnPHEJaEVJVLolNCkijB+Fdsp+/DTc78EcXA1K6mZvpCwSM/TtLzX7qPRNMaLe55I8AAC7o~1',
        '_abck': 'DD57C38A5F8F116708A48B6891EF6911~0~YAAQPl3SF5/XHLGCAQAAy8LlyQg6zF6mrKxS5uTUdWmjJG/pOGfEgokdTQCKDfXNJZZC4neEiv5tZuClRjzopdA1KNCK8MG/jWYCKa6O3pFoukfTPWciw0udpzt9264Off8b+B1VnxLdc+Uwk2FNqKqFSA9P2xSBEoER7DFNfVXSvCOhknsFroJtVMhJKE3AtSik5KFp1qrFfeZDxtq+47F53XUFf5eQ3YrOJtBBjAiRXg4MHliTT3vexbb1KcJ/y3K6e1ou3OlMMgk402GbEJSpM1A5QqirNs4zC5qWLL7kwHmQgPWhdTLZ/uBrbfa0vnXq98mw1ovHXajpi4/axdV3GecqGfjOYvygwn/peQejcrAvxFKnxpCKQyQ86PsAMEyY4LrspXHF29wNq7glaE+8o1TcL2Z5~-1~-1~1661248239',
        'microsessid': '688',
        'ru': 'Qk1QUHRUMVBYcW8bEUAIdnxcC3obZxoDVAdbIhdeRFUQP1B9PCIPbQg1GgkRO0AwIzI2MDcyMzY1NDQkMg%3D%3D.95261449f92e59099afb53770bedde25',
        'utrid': 'F0NRAnRcYFpEc2ZIFVdAMCMyNjA3MjM2NTQ0JDI%3D.a3c47e67b838bfc73a410a931339ff65',
        '_xsrf': 'jFq3rwBJf9oRfEFCxiTIWseqcdbBZ7Rw',
        'user_session': 'eshLPDbQnsLLfLnt6osAFw.iaaH8y2_0YwqkdouZtTenTLgLVXL5EGxPo1QO_d8qfBvqB88OgqnQ1UE-5jbbxReNTO6zjsQafpBCynq3dYyV3J3ZI7AwDzpZtNzeyYlCYz60LQwskIIEwurFbACNfnjJoYWL1UzxB3xLCkHXG2x8FLawgc0w3QQYATRcz7sdi2ZZedSIjEldpU9Pak62d4C6Va5K3oi_hq4UkGYNklDTOHJHAaXT6U63yMDVmmY4r1C_44gtU45PhRsrYW8v4X9Sgi5vQXPdH0vnDzXV1uIBGQwZjYWh-SVKgviIDSaDFzxmJMm5azPus8dXmOUxG0KXCDSTJuuURfB9f4WMsIRgHatCPhrG00iCM-17nY2bAzL-bm1CUcvs9MjJCPtSWD8gHYpIeosGC8HbnbNJFYd6dpkZJKaOdrOtC-mMjbZeFEJpVdUWo5iXjk2jXa8ifd9K39jvBKt6uzpCrFhXZDVyZLR9tZJ3BkH5NKLUqq33iKm3eEwZHQRhKg80sGGf4XD.1661244656387.86400000.4t0HgtoOkYptUoaF5n61IOMQ5r3hwvsZQXdjXNDGuKI',
        'newUser': 'false',
        'AMP_TOKEN': '%24NOT_FOUND',
        'ak_bmsc': '3325E0963DC0B9E0007811FDDDE9343C~000000000000000000000000000000~YAAQPl3SF8/YHLGCAQAAeNPlyRA+LKfHVuXvtDAe9M8d1qvqpEyVlZ1QgB36Tfo7XE9Aljsz3YEJqAeE6yvfbZlOUuSxIUZk8BicbwG/dzUHLplwC0M+e3jluAejkv0NRsBIOPkTTRB/mbXO57iWU+Uh8lZ4dkPtDHN4yWMsPUUqPS0d4jVlfeWLVZn4HmgpynApN4XAHxAgc8/JMMAkWYmz8X/JYViB9CykvwjuBR5A7mL325fup105ACUySLz2wN/7skG7clSNW3e4BMv1gFmW1gVJcu3q9lxvH3mk5rdz3OiiBjk6t2q3+fgiuzH7XjkoExsA6rhUZTgH9exubeyYvUDZEr7ikxSROI/xNp11hBsxtmtCBSkPnXj84JbWbljczKOz5uOtHx8KNxNshYVIFkHY27//4YayI+75/JmspSxoaqlLtNpIBvm3gViyLXn6Oddy5qbfIKBTZsY9I68d9PveBD52z3VxygDBYCFGhkFOlpm0y9UuU3OqQanuIWOTa9OkJZF+s5SrzVaTuKktTQ2ipp/JXfvln0hpPCsKMcuRRQ==',
        'bm_sv': 'E3522F96AC976EC1C79016FDCCA607DF~YAAQPl3SF9DYHLGCAQAAeNPlyRCeawKmNakPur9RvyQNg1Ps2xloWrMZPu+1BOP0CqFyJZdeFrs2ohM1MpGGpk0TgvIq1TtNHCM8FWEyqx9xdWsVDG+t6dSyr38+678q/F6Si1gnYIb3ah/Sj7O3cS0HaDJ/sTxJQsIluYZx8xsoj0ZUZs0hBpmb7qNHQ4VGbVWHSlFj5mikKgSslhy+2DmAUAh4XvU69c6k0SYSYC5uCacXHt6AISr8I/dS9b5e~1',
        '_gat': '1',
        'cto_bundle': '-XNaaF93Y1BsNFFkJTJCbjAlMkZVYkQ0WEpjNVVIRExPV3UyR2pxR0hkNmliNmE1SUxyUVdZeXRGN2tNS0Q0MW9mdEclMkZ6QVNYa3Jjd1J4ZE0xeE9vJTJGT3ZzNDkzNGZTJTJCZUYxaTJNRFJ0OFo5dkNLdjgyQjdGSUVyeEUxY3olMkYwQjcxdndNTU1NRFBHanUxb3Q2ODZ1ak1hTW8lMkJaT282QSUzRCUzRA',
        'ak_RT': '"z=1&dm=myntra.com&si=a62de590-c921-4ffc-a255-ae47b67219aa&ss=l75y68nw&sl=1&tt=8o1&rl=1&ld=8o5&nu=46zaonao&cl=144f"',
        '_abck': 'DD57C38A5F8F116708A48B6891EF6911~-1~YAAQL13SF5GSX7SCAQAAbQj/yQhzn8cLdei+7a8GtxeoguS/8lgfC6e9Ba45TKq7iN3zU+guH83X3EgOfLB+Arn6MIcI5OTDbnzPTTgx1OSY5tNdOKtnaPBQ/lg5l1wD52yqkX0CXfeYVXaBBvuZf4qz6dC4+A8sNgsfZB/8lyE/xMn+GSEPicPjKHxpkkFnJR+krE4K9yg7OKsgl3izGipxGCrvO0Exqm4We0BmU4KHgJ5U0k7xGgS4arULYA58Szqfcl4Y009AgniW4DzytP3G/24b2IRoVpA2t/UvcL3EuqvA2kA6GXToSg5np+UdtsUnY4Dli0UQ6XBk9ActeVsXv/IchSItJs16NpnR4H9dnDr/L48XcnnOywgdxeHDjgt3pBegivdz7uQLCK9nPsf1yYeFLztx~0~-1~1661248239',
        'ak_bmsc': '3325E0963DC0B9E0007811FDDDE9343C~000000000000000000000000000000~YAAQL13SF5KSX7SCAQAAbQj/yRAK3iu0DbbAadrlTfgYfzaAuUmQ8dWSdGRNRRhFH7ssm5aT6WMCMNgqllbYXeK+B5qXSLdnwCZ5q8mfDpEypaMFLfLD2yqttVbezC7PuPkUqxaeOJRswx71r1nQBCDw09FSi/jjVrtVGcMmGFpbZOiH8oh53bbbvkOfzNucHF/ACPGFuFBopDadzLQ9w7zucwtw1fl+VmjhVqIB/Os1+Wvvi0MFW4FaecFcJKt53lEjmMI7jgKmCzkVb+oJmwOPM5TKgjHNFOVvojphZYuCz/4dlgafu87RrEopBvN4BQKmFOR1H2VAqDn6u9FqFT/hnPifE6n0qkgtMHgiWV1Hze4gwSoC1VJwaS5doIeu4sJ2uUrBD6JnBHnUgvD26ArwX+QqQ7ftSJY4B95+YXW5zJwXofBZc2EpSok2VEERZdh8Tna/RmHRUjjHhbT+x/T0PVH54BsPfR6Qzv6ceLvM8m/nysuUXLTUvZzzGmVPT/5XMmmpJalZRM0bus3RrXeKjxBZTaENVdmzpzLsvADeY3qwWPLI',
        'bm_sv': 'E3522F96AC976EC1C79016FDCCA607DF~YAAQL13SF5OSX7SCAQAAbQj/yRA0gzxjuWbfnX0nyHSXUsubxig9XrT7WMgidCemaRTUSF4XdQQlMouA0bvvVWKtM9SEQqySUO3awAvVZPB2s1YasEPSiDndpnj9kfuTJv/amxufJgJlnqOX6NP6DCoOucMzKy5BdhCOfbS3KmECx5iSkshXOOqXnrQSJmz6vJTh8qhCrAtNteDpX2V03nyjXElfqJA+Te43ldktIdLDm+7lQ8Yug1SCWp64HNrH~1',
        'bm_sz': '4C5D84297551CB84B088EFF399F06371~YAAQxP3UF634AciCAQAA3BHqyRDBBBlnRJGzzgvnNqiYtvVlTL16sMqrEiM/IDlwXG0k3ZDxbNevy4ki6RLw2IuKKeyKEmYo03fvr1e08kk7tnuLPXRMCZOf+dVy8zAHLFNYnIBDauvQvHhyy7pik/fDeG6f/RLg1y6vD4RNHzYe6ON+kqTJ+sDRJisi9EavrXuUefqOnXqbAGd4zE4EU75amRly5ckHHswp4xVjEROPN0yvxvPB6h9m6dTsDroiH6BBel61mRzNjAJ7zHwHX9ytWayc7TisQbqawbEhjOkrHh4=~3683906~3163446',
    }

    headers = {
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1678700689.1660729809; ajs_anonymous_id=bc38f1bc-446c-48cd-ae66-8ecd32f9d3ca; ajs_user_id=c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB; bc=true; _d_id=d1b5def3-1a43-41b7-8851-07873644d628; mynt-eupv=1; _gcl_au=1.1.433464726.1660914224; tvc_VID=1; _fbp=fb.1.1660914224900.857102999; _gid=GA1.2.1310205691.1661142008; _cc_id=c28b639646f44757bd62a52750457111; __cab=cart.fsexp%3D; ftc=false; sc_tt=true; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; ilgim=true; user_uuid=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; oai=144652047; oaui=144652047:191149625; uidx=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; mynt-ulc=pincode%3A110085%7CaddressId%3A144652047; mynt-ulc-api=pincode%3A110085%7CaddressId%3A144652047; bm_sz=56A9340D1C4E7F4B715B3BE194DCF456~YAAQL13SF4NPUrSCAQAAKSxzyRBhhxPUQAXH2n6HBAKAC2Saq500KRloE5VJUhcIxquN5HlbahGTcA0Gy2nHvYCAO4zRRiGGYg4+zTmXNl37wKYp1ynQL7l2b2uVGGypDbH1r9Tdyy62gk+BDtmu4FnAb+Gb24v/FYBUARjPPqSqRcolaaOvxhmQkNk0aXBTCFC/hYImQJIlemrs1doKRpmzUgeU1sKmRo6FYdhJNOf3jAVhTrRT0iUkrSjfMK3nO1luI2A8vEgYZVe4kDx3v+rjpgnGNdqXxql3WaJT3NiUVZ8=~3552065~4403764; panoramaId_expiry=1661323554134; vw=400; vh=984; webVitals=true; _ma_session=%7B%22id%22%3A%228cc94ee4-21ee-4c92-9219-22aff4ed964f-d1b5def3-1a43-41b7-8851-07873644d628%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; mynt-loc-src=expiry%3A1661244050927%7Csource%3AUSER; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.desktop.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661244651%2C%22trackend%22%3A1661244711%7D; lt_timeout=1; lt_session=1; at=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1Jd05XVmxNelU0TFRWbFpEQXROR0ZpT1MxaVlUSXhMV05rTnpoaFpEZzROek5tTlMweE5qWXhNVFE1T0RNMk5URTJJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJME9ESTFNU3dpYm1sa2VDSTZJalU1T0dJMk5UWTNMVEZtWW1ZdE1URmxaQzA1TVRnNExUVmhPRGxsT1RsbVpUSm1OU0lzSW1saGRDSTZNVFkyTVRJME5EWTFNU3dpZFdsa2VDSTZJbVE0TjJJNU9XVTRMakE1WXpJdU5EZ3pZeTQ0TWpjd0xqZGlNV1ZtWXpNNU9HVTBOMGhEU2pOUVJVdHljM0FpZlEuSmRvX3hBMUloVVpqSHI0VTgzXzF6X2hMUklXaEI3ZWJpZWh3YWRxTEtoUnZjSC1wcHFFaXplcVZybDVDVjNITHlIQ1p3VnlENGhMRUhrNndZR2s4ZERzVkJoU05uSE5xdW1Id2pxS2Etd0w2RE82dE42OTEyMzB5WjVLdm1XR0U4QUcyMk4zWV9QazlNUm02cWtHMTZNb0NFLWwyNzVfdlBsbzBNVkwxVDU0; rt=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUppTURWbFpUTTFPQzAxWldRd0xUUmhZamt0WW1FeU1TMWpaRGM0WVdRNE9EY3paalV0TVRZMk1URTBPVGd6TmpVeE5pSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpRME5qVXhMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOVGN5TmpVeExDSnVhV1I0SWpvaU5UazRZalkxTmpjdE1XWmlaaTB4TVdWa0xUa3hPRGd0TldFNE9XVTVPV1psTW1ZMUlpd2lhV0YwSWpveE5qWXhNalEwTmpVeExDSjFhV1I0SWpvaVpEZzNZams1WlRndU1EbGpNaTQwT0ROakxqZ3lOekF1TjJJeFpXWmpNems0WlRRM1NFTktNMUJGUzNKemNDSjkuRlFUeW1odVJVaWFSZC1BMENnRXRtU1R4WnN1SUF1NGUyZHVjeFNNS3pXQmdSTnYxOUJubEZvU3JjYkZPZGd3ZHg1aVpFSnlIUjR1aTlya3VBSzlDVW5GN1BZaWM3ZE9rcDNwNlQ1WU5YWlBjd3ZuOW5VM1VFNTNnUU1CNm8xQlhWdHU2VkZKVk9GQmU0eUlUVlVac0lCZGI0WnNBWmQwOWZ6ZmJ0UHVzdk5F; AKA_A2=A; bm_mi=6EAD546B2F4F330E251274D19039653F~YAAQPl3SF1nXHLGCAQAAC8DlyRBP0vhxeCqOBbK+iuhm8D3ycvNUfszQQ1/ebdsLVSnkl6ddN2J2CWc3DQ0CP5kQqQRw64Sstb/5wCYNNvW46ustSYAmh6iuOnoH6B0h2PqT3tzi7UebZgxIgYMYaj9fHHAmz4sWyxdCnieQbCmifYVPC8z0d72PM4EGzYR7w+a7dPdPebV8DM84yX5mQGp9NJOFbqVsuzIufVmfkgJl/UPp/zLmrSKZeOCwaVL+UVF+Qn0RXzixEO9FOsATzzba4f/cqwvRuopI+hnPHEJaEVJVLolNCkijB+Fdsp+/DTc78EcXA1K6mZvpCwSM/TtLzX7qPRNMaLe55I8AAC7o~1; _abck=DD57C38A5F8F116708A48B6891EF6911~0~YAAQPl3SF5/XHLGCAQAAy8LlyQg6zF6mrKxS5uTUdWmjJG/pOGfEgokdTQCKDfXNJZZC4neEiv5tZuClRjzopdA1KNCK8MG/jWYCKa6O3pFoukfTPWciw0udpzt9264Off8b+B1VnxLdc+Uwk2FNqKqFSA9P2xSBEoER7DFNfVXSvCOhknsFroJtVMhJKE3AtSik5KFp1qrFfeZDxtq+47F53XUFf5eQ3YrOJtBBjAiRXg4MHliTT3vexbb1KcJ/y3K6e1ou3OlMMgk402GbEJSpM1A5QqirNs4zC5qWLL7kwHmQgPWhdTLZ/uBrbfa0vnXq98mw1ovHXajpi4/axdV3GecqGfjOYvygwn/peQejcrAvxFKnxpCKQyQ86PsAMEyY4LrspXHF29wNq7glaE+8o1TcL2Z5~-1~-1~1661248239; microsessid=688; ru=Qk1QUHRUMVBYcW8bEUAIdnxcC3obZxoDVAdbIhdeRFUQP1B9PCIPbQg1GgkRO0AwIzI2MDcyMzY1NDQkMg%3D%3D.95261449f92e59099afb53770bedde25; utrid=F0NRAnRcYFpEc2ZIFVdAMCMyNjA3MjM2NTQ0JDI%3D.a3c47e67b838bfc73a410a931339ff65; _xsrf=jFq3rwBJf9oRfEFCxiTIWseqcdbBZ7Rw; user_session=eshLPDbQnsLLfLnt6osAFw.iaaH8y2_0YwqkdouZtTenTLgLVXL5EGxPo1QO_d8qfBvqB88OgqnQ1UE-5jbbxReNTO6zjsQafpBCynq3dYyV3J3ZI7AwDzpZtNzeyYlCYz60LQwskIIEwurFbACNfnjJoYWL1UzxB3xLCkHXG2x8FLawgc0w3QQYATRcz7sdi2ZZedSIjEldpU9Pak62d4C6Va5K3oi_hq4UkGYNklDTOHJHAaXT6U63yMDVmmY4r1C_44gtU45PhRsrYW8v4X9Sgi5vQXPdH0vnDzXV1uIBGQwZjYWh-SVKgviIDSaDFzxmJMm5azPus8dXmOUxG0KXCDSTJuuURfB9f4WMsIRgHatCPhrG00iCM-17nY2bAzL-bm1CUcvs9MjJCPtSWD8gHYpIeosGC8HbnbNJFYd6dpkZJKaOdrOtC-mMjbZeFEJpVdUWo5iXjk2jXa8ifd9K39jvBKt6uzpCrFhXZDVyZLR9tZJ3BkH5NKLUqq33iKm3eEwZHQRhKg80sGGf4XD.1661244656387.86400000.4t0HgtoOkYptUoaF5n61IOMQ5r3hwvsZQXdjXNDGuKI; newUser=false; AMP_TOKEN=%24NOT_FOUND; ak_bmsc=3325E0963DC0B9E0007811FDDDE9343C~000000000000000000000000000000~YAAQPl3SF8/YHLGCAQAAeNPlyRA+LKfHVuXvtDAe9M8d1qvqpEyVlZ1QgB36Tfo7XE9Aljsz3YEJqAeE6yvfbZlOUuSxIUZk8BicbwG/dzUHLplwC0M+e3jluAejkv0NRsBIOPkTTRB/mbXO57iWU+Uh8lZ4dkPtDHN4yWMsPUUqPS0d4jVlfeWLVZn4HmgpynApN4XAHxAgc8/JMMAkWYmz8X/JYViB9CykvwjuBR5A7mL325fup105ACUySLz2wN/7skG7clSNW3e4BMv1gFmW1gVJcu3q9lxvH3mk5rdz3OiiBjk6t2q3+fgiuzH7XjkoExsA6rhUZTgH9exubeyYvUDZEr7ikxSROI/xNp11hBsxtmtCBSkPnXj84JbWbljczKOz5uOtHx8KNxNshYVIFkHY27//4YayI+75/JmspSxoaqlLtNpIBvm3gViyLXn6Oddy5qbfIKBTZsY9I68d9PveBD52z3VxygDBYCFGhkFOlpm0y9UuU3OqQanuIWOTa9OkJZF+s5SrzVaTuKktTQ2ipp/JXfvln0hpPCsKMcuRRQ==; bm_sv=E3522F96AC976EC1C79016FDCCA607DF~YAAQPl3SF9DYHLGCAQAAeNPlyRCeawKmNakPur9RvyQNg1Ps2xloWrMZPu+1BOP0CqFyJZdeFrs2ohM1MpGGpk0TgvIq1TtNHCM8FWEyqx9xdWsVDG+t6dSyr38+678q/F6Si1gnYIb3ah/Sj7O3cS0HaDJ/sTxJQsIluYZx8xsoj0ZUZs0hBpmb7qNHQ4VGbVWHSlFj5mikKgSslhy+2DmAUAh4XvU69c6k0SYSYC5uCacXHt6AISr8I/dS9b5e~1; _gat=1; cto_bundle=-XNaaF93Y1BsNFFkJTJCbjAlMkZVYkQ0WEpjNVVIRExPV3UyR2pxR0hkNmliNmE1SUxyUVdZeXRGN2tNS0Q0MW9mdEclMkZ6QVNYa3Jjd1J4ZE0xeE9vJTJGT3ZzNDkzNGZTJTJCZUYxaTJNRFJ0OFo5dkNLdjgyQjdGSUVyeEUxY3olMkYwQjcxdndNTU1NRFBHanUxb3Q2ODZ1ak1hTW8lMkJaT282QSUzRCUzRA; ak_RT="z=1&dm=myntra.com&si=a62de590-c921-4ffc-a255-ae47b67219aa&ss=l75y68nw&sl=1&tt=8o1&rl=1&ld=8o5&nu=46zaonao&cl=144f"; _abck=DD57C38A5F8F116708A48B6891EF6911~-1~YAAQL13SF5GSX7SCAQAAbQj/yQhzn8cLdei+7a8GtxeoguS/8lgfC6e9Ba45TKq7iN3zU+guH83X3EgOfLB+Arn6MIcI5OTDbnzPTTgx1OSY5tNdOKtnaPBQ/lg5l1wD52yqkX0CXfeYVXaBBvuZf4qz6dC4+A8sNgsfZB/8lyE/xMn+GSEPicPjKHxpkkFnJR+krE4K9yg7OKsgl3izGipxGCrvO0Exqm4We0BmU4KHgJ5U0k7xGgS4arULYA58Szqfcl4Y009AgniW4DzytP3G/24b2IRoVpA2t/UvcL3EuqvA2kA6GXToSg5np+UdtsUnY4Dli0UQ6XBk9ActeVsXv/IchSItJs16NpnR4H9dnDr/L48XcnnOywgdxeHDjgt3pBegivdz7uQLCK9nPsf1yYeFLztx~0~-1~1661248239; ak_bmsc=3325E0963DC0B9E0007811FDDDE9343C~000000000000000000000000000000~YAAQL13SF5KSX7SCAQAAbQj/yRAK3iu0DbbAadrlTfgYfzaAuUmQ8dWSdGRNRRhFH7ssm5aT6WMCMNgqllbYXeK+B5qXSLdnwCZ5q8mfDpEypaMFLfLD2yqttVbezC7PuPkUqxaeOJRswx71r1nQBCDw09FSi/jjVrtVGcMmGFpbZOiH8oh53bbbvkOfzNucHF/ACPGFuFBopDadzLQ9w7zucwtw1fl+VmjhVqIB/Os1+Wvvi0MFW4FaecFcJKt53lEjmMI7jgKmCzkVb+oJmwOPM5TKgjHNFOVvojphZYuCz/4dlgafu87RrEopBvN4BQKmFOR1H2VAqDn6u9FqFT/hnPifE6n0qkgtMHgiWV1Hze4gwSoC1VJwaS5doIeu4sJ2uUrBD6JnBHnUgvD26ArwX+QqQ7ftSJY4B95+YXW5zJwXofBZc2EpSok2VEERZdh8Tna/RmHRUjjHhbT+x/T0PVH54BsPfR6Qzv6ceLvM8m/nysuUXLTUvZzzGmVPT/5XMmmpJalZRM0bus3RrXeKjxBZTaENVdmzpzLsvADeY3qwWPLI; bm_sv=E3522F96AC976EC1C79016FDCCA607DF~YAAQL13SF5OSX7SCAQAAbQj/yRA0gzxjuWbfnX0nyHSXUsubxig9XrT7WMgidCemaRTUSF4XdQQlMouA0bvvVWKtM9SEQqySUO3awAvVZPB2s1YasEPSiDndpnj9kfuTJv/amxufJgJlnqOX6NP6DCoOucMzKy5BdhCOfbS3KmECx5iSkshXOOqXnrQSJmz6vJTh8qhCrAtNteDpX2V03nyjXElfqJA+Te43ldktIdLDm+7lQ8Yug1SCWp64HNrH~1; bm_sz=4C5D84297551CB84B088EFF399F06371~YAAQxP3UF634AciCAQAA3BHqyRDBBBlnRJGzzgvnNqiYtvVlTL16sMqrEiM/IDlwXG0k3ZDxbNevy4ki6RLw2IuKKeyKEmYo03fvr1e08kk7tnuLPXRMCZOf+dVy8zAHLFNYnIBDauvQvHhyy7pik/fDeG6f/RLg1y6vD4RNHzYe6ON+kqTJ+sDRJisi9EavrXuUefqOnXqbAGd4zE4EU75amRly5ckHHswp4xVjEROPN0yvxvPB6h9m6dTsDroiH6BBel61mRzNjAJ7zHwHX9ytWayc7TisQbqawbEhjOkrHh4=~3683906~3163446',
    }

    params = {
        'p': '1',
        'rows': '50',
        'o': '0',
        'plaEnabled': 'false',
    }

    response = requests.get('https://www.myntra.com/gateway/v2/search/men-formal-shirts', params=params, cookies=cookies, headers=headers)
    print("response:")
    print(response.json())