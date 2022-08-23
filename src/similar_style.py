import requests
import curlify

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body
        ))

def get_similar_style(image_name):
    image_path = '/Users/300074702/Projects/hack/resources/' + image_name
    files = {
        # 'file': open('"/Users/300074702/Projects/hack/resources/img_1.png"', 'rb'),
        # 'file': (image_path, open(image_path, 'rb'), 'multipart/form-data', {'Expires': '0'}),
        'file': '@"/Users/300074702/Projects/hack/resources/' + image_name + '"',
    }

    print("sending")
    resp = requests.post('https://www.myntra.com/gateway/v2/visualsearch/image', params=params, cookies=cookies,
                      headers=headers, files=files)
    # req = requests.Request('POST', url='https://www.myntra.com/gateway/v2/visualsearch/image', params=params,
    #                         cookies=cookies, headers=headers, files=files)
    # resp = requests.post('https://www.myntra.com/gateway/v2/visualsearch/image', params=params,
    #                   cookies=cookies, headers=headers, files=files)
    # prepared = req.prepare()
    # print(prepared.headers)
    # pretty_print_POST(prepared)
    # s = requests.Session()
    # resp = s.send(prepared)
    print("resp: " + str(resp))
    # print(resp.request.body)
    print(curlify.to_curl(resp.request))
    print(resp.json())

def get_similar_2(image_name):
    import subprocess

    process = subprocess.Popen('./src/cmd.sh', stdout=subprocess.PIPE)
    output, error = process.communicate()


def postman():
    import requests

    url = "https://www.myntra.com/gateway/v2/visualsearch/image?page=1&rows=5"

    payload={}
    files=[
        ('file',('img_1.png',open('/Users/saumyamishra/myntra-hackerRamp/resources/img_1.png','rb'),'image/png'))
    ]
    headers = {
        'authority': 'www.myntra.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en;q=0.9',
        'cookie': '_ga=GA1.2.1678700689.1660729809; ajs_anonymous_id=bc38f1bc-446c-48cd-ae66-8ecd32f9d3ca; ajs_user_id=c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB; bc=true; _d_id=d1b5def3-1a43-41b7-8851-07873644d628; mynt-eupv=1; _gcl_au=1.1.433464726.1660914224; tvc_VID=1; _fbp=fb.1.1660914224900.857102999; _gid=GA1.2.1310205691.1661142008; _cc_id=c28b639646f44757bd62a52750457111; __cab=cart.fsexp%3D; ftc=false; sc_tt=true; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; ilgim=true; user_uuid=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; oai=144652047; oaui=144652047:191149625; uidx=d87b99e8.09c2.483c.8270.7b1efc398e47HCJ3PEKrsp; mynt-ulc=pincode%3A110085%7CaddressId%3A144652047; mynt-ulc-api=pincode%3A110085%7CaddressId%3A144652047; panoramaId_expiry=1661323554134; vw=400; vh=984; webVitals=true; bm_sz=F7B4392037DC1CF4B9DD5D8D4229FA2D~YAAQ3P3UFzMITciCAQAAlxJuyxCMOXGJa3J/bq/CNDNJZeF9g1jJaI/Oz6P9qF6h3utbLKd7YrpF3w5c2rPnMBff6ZEgNTzVr5tUs+GY+09FoCVziu6LVPtlwOMVryBCx2MA6M8U/CSkVoF1sE3cUcRDBCg+V+dFFmDxKDXQIPKVwC/KbTfp0W7s/GPvnpjN4mCPGYyg7ZlAVQFpSd/eAsR90wFVnIYA2fbsG9IGrJc/O1Zl4LvbDdgKxlhsW7emWThg9KeO+cNdWo8Se9RREEIaXfH02TnmvqY5+wHvJ91DFps=~4337717~3294274; bm_mi=E238F47663AB21AE168AC0090C0E5B1C~YAAQ3P3UF8IITciCAQAAchduyxCgIK24OYkST/EQ9f+HfNb9HzFWfY8ziQwt0ndOlkPDfz6nmdn9H6y4XqoduI3h+OKIs5q/nxYXv+f8elJcmAPzKiybmD7dZFOpI6tNkTYD5fmI8klKDsRveCswixI6lBCoQBmsVCmzSKtvoQkTgHcLkytUDHIsfM5g/m8bJEDNTRdoNBrTXgRXrLq43dIcZPsXFStr8ozkyhdovKHc4RBpoUKoefxt7ziXx1cDTW7CYo1YI2CqGIbJLphEw5vuDPJ+GnkkKKnpPXYzu7xm47EKovAJg7WNs5DXQtuxrBYPtrqaLodtAceBoZlJAfDN4EaIkmQOPAqLriiHQP5RqE+oj7dvzHGlceD6pmAu+A93rQZhbZ6aPTkxe03PAFS18xGyLs3J/44XjcFkwOhXrqFWn7/wKbB34uWfLQ9s6Xn8zBqPDF4QoQB63VfuCwnVhA==~1; ak_bmsc=BB220FA0E75DA72730129649FCEEA8F5~000000000000000000000000000000~YAAQ3P3UFyAKTciCAQAAxyNuyxDWwjH0qHKrchQ/zA7AFvQ0h+A2X8CWyk93o2CANA/rIPWJGYc7AnfxwzaG/IFi+C24ro9ua5Uw/cRb6UqcPWGxKn7m48mKBfsEA8pcfHFEiHK49cXpOn3dVa/QjiUqGL3YHpGJVMrAEpVrhmHv1tsxuHJm+p++IYjkPJdTTPgwS157cdvNozrezPjIWXaeIRk98mLW3GT3Ecvr3esLn3J/OI0cH0bC3a0zQ7MbkoauqbJ71YVSCMlJzqoB6y9cxhueZCnnkOixY1fKa6v/9sj+ZItC5L94y5b7nJkNFA2VL2/c4DkQwOx8Rl9c8HdcZvs3CkHctEwAtNihaUnkysnIJGjuylqDpKD8N/mGhbsrMbVcIoWcUbXg4LgdTh2vfLMkGgNMgQ3J+axawU+f9yqDVvzZcwaq1ha4lBg7lfz4EJQGtM8U+fxqYbEkjCwY+Dkf4GhQZNiA899NhLc2k5MeWaZ5uEfix5K8eQe19qkVCCrrqMzd6bMD0hVBeNSll+jrSou9Bdvm2IxnJTT2BWh7nSTugzy7j0WkLOJaNrf/Xy/K0WcpJYp2kg6WxMGrMfIHM+ZC4bIh+wwQDNY/3FVVi25wIcYkCF2F9eYZHwdiUITfpw4eZY30utsbO6tvjb4oWo5swPUlwz9ebiBF; cto_bundle=sMclUF93Y1BsNFFkJTJCbjAlMkZVYkQ0WEpjNVVIQ2hEZERUaE11ZGQ3V285UThsZzRBMVI2WENmekluODRHWGp2S054UnFXSjF4WWEwSEpBb2FvdmNrSkloeW9iRzNKVWpFd3g3c0RIbjJsUDB2eHE2M3FrZlRncDFHRnFEMkNHbnNOMmRmdG1iOHJqeVZrc1M2UmpCczFmTzAybUZ3JTNEJTNE; mynt-loc-src=expiry%3A1661271816362%7Csource%3AUSER; ismd=1; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.web.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled%3Bpdp.autoapply.newusercoupon%3Ddisabled; _pv=default; microsessid=292; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661274135%2C%22trackend%22%3A1661274195%7D; lt_timeout=1; lt_session=1; at=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1Jd05XVmxNelU0TFRWbFpEQXROR0ZpT1MxaVlUSXhMV05rTnpoaFpEZzROek5tTlMweE5qWXhNVFE1T0RNMk5URTJJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJM056Y3pOU3dpYm1sa2VDSTZJalU1T0dJMk5UWTNMVEZtWW1ZdE1URmxaQzA1TVRnNExUVmhPRGxsT1RsbVpUSm1OU0lzSW1saGRDSTZNVFkyTVRJM05ERXpOU3dpZFdsa2VDSTZJbVE0TjJJNU9XVTRMakE1WXpJdU5EZ3pZeTQ0TWpjd0xqZGlNV1ZtWXpNNU9HVTBOMGhEU2pOUVJVdHljM0FpZlEuYnF1Z25qWWVqTE53MWdfV19JX3FOZW1PYllveXU1QWItZUlKRHZMN2tfbUtRVHNWem9lZ1lHVWgyYjBFczNwX0paMk1TODVkR1pIaG92OHVQLXlWcENtY1FJdmxEUzVYSXFNeW41bUNjaU1TZWhBLTdvVEFSZzU4N1dNZjJueVZ6d0MzeGxCYXVmcXFSaDJFZXViQ3A2d1Q5YUNxTE1OZWxFZWg3NkJab3Zj; rt=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUppTURWbFpUTTFPQzAxWldRd0xUUmhZamt0WW1FeU1TMWpaRGM0WVdRNE9EY3paalV0TVRZMk1URTBPVGd6TmpVeE5pSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpjME1UTTFMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOakF5TVRNMUxDSnVhV1I0SWpvaU5UazRZalkxTmpjdE1XWmlaaTB4TVdWa0xUa3hPRGd0TldFNE9XVTVPV1psTW1ZMUlpd2lhV0YwSWpveE5qWXhNamMwTVRNMUxDSjFhV1I0SWpvaVpEZzNZams1WlRndU1EbGpNaTQwT0ROakxqZ3lOekF1TjJJeFpXWmpNems0WlRRM1NFTktNMUJGUzNKemNDSjkuT0tneW1BZkpXTklRS19DVmZudV9xdUZaZGM3MDBGVlAza2lwMGVIdjU4a1pHd0lOSllZQmZQeVhkaVh4bzlHR0Q2MGJyLW5lQzctZzUwSkVWcDFEbTAxSEtrZVhUN0w1Mm92U3V6ZjQ4a0w0RjIxN2Z0clpDZXlnUFVmN05RNV9Fbm5hMGt1RElzQ2pBMW5DdFdSb3JLLTNmOUZBZ2ZVWHFNM2FxTFA4cElN; AKA_A2=A; AMP_TOKEN=%24RETRIEVING; _ma_session=%7B%22id%22%3A%228b03de00-131e-4177-8807-b3c15ce05b4b-d1b5def3-1a43-41b7-8851-07873644d628%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; _abck=DD57C38A5F8F116708A48B6891EF6911~0~YAAQdV3SF0j+5LSCAQAAJ6Gnywi8QH9adWy0tfdrpws9bDEoPbXvgX4lF8r9e57+/2bP6wizGGXPsd70OsL/IyPp0c8lz3yjvuV3D6XuEiuRaGNb/QvRc20k38SmeL1e1ry5QVMCw0rddkWxcKBRvo4l+pMr4TLaCUIsE/AW8VyrSGf3H1pfPo+Q8QlVRXBb/Igy3CFroYO6MGel0t7W4Y/FIzYFGG7GdWTbXXEndsh3FD0LfbLO3k8j44DdQLEwzP1THbzlnudBa1xGpsoMDYIMpDit22e3KuaJIa+oEWeJXegfJIx1IYC3Q+nSwkmBnycOMPmwLSI5LV6im0NZTZMnV+DCsLhjDPm5p8r/i3Y871c3kfYt4hiJ/ai4a/hAVEm1odGX+xivlO82szwp1q1fr71wa4Pd~-1~-1~1661277681; dp=m; ru=Jg4RWwoST3dfAk4ofGoJQ0UrS2FzTUQGQgUGCQwMfn4DNGxOCwMPDHE2IlFXOUAwIzQyNzQwNTk5NzgkMg%3D%3D.0b0906a1e39f1d6879698caa39969a8e; utrid=uuid-16609142220069; _xsrf=lxcDdcELFaiBrZ9UeeehYrn6SOWQF0kl; user_session=5sPhx7g7sxZC4_Ld7Viz2Q.Aa3IvxiAvRq2p6LLb0ufOJ2n-uAXhIO-oxxH488YrbP20dfd7pdNvYgYDmcXQst1AmrU-ww-wuFublPMXQnBx5MavT8Wu6j12xTJCaCYCaQx_fX5sz4jXgtdyF7QHNWoTusDlTGyvlW6CCd9bG-5jcUi8TXt_KNmVBZOsFRt436wBm8zQ-b-Zie60dwc0VS0gwtTpnSVt5l6NB302bC3OZAec4UJO-0Gt8mHUQK4FddhPsE6Wv9KJwOizJN8lki8sjzrS9RoYCJoYRutbe2RaEn_daGvlzhg0XDsw-wOLXLWbE3tCTc22kRdj1Mxr2OTptTwx_QcKCR8KRL_SdO459pXozjMFWBZxE3Tz2ygoYV5xiZ6Y8y2R2_3XDrMtvw4cxPFUzhx52M8Z0XCCJLzGeDsh-7NrwBFKT4xJDC45E7TcB_U-zOBd97ldlfx37DGw1Mwl6xrMtBM8cV49sJ0yXH4BlQTd59-PLwhvgYpErZgsKnihF0Ea8sdkCacn1Ye.1661274135930.86400000.2IKTAlkgcv1ZmsICNj_urQzZ1kHv7Ktb28LBaWyTSgM; bm_sv=268868EE94488D10D7425FA9BCF45E3F~YAAQdV3SF0z+5LSCAQAA2aGnyxAs62ncwQLwEobdWH4yG4/7wy/7YnFE1084qAWRWiZC9ONyaVWw9Xeo6CNQoqXNwXSfGzbfqCzaiZv5O+rXaGTsB7PvdqnQUutdkcJsGxiIn3zNDpzquY8IvOWaTjUnfxsC7vzmWAiWtpSm9Cki7hGE8jo1wtq2NoY3zddszVz4BsalpZA6MehGI7hF6b0fS7jxLBeVaJQfex3YSXdk1zbpIyyWQV3G/4kNhWCkaA==~1; ak_RT="z=1&dm=myntra.com&si=a62de590-c921-4ffc-a255-ae47b67219aa&ss=l76dhcon&sl=0&tt=0&rl=1"; _abck=DD57C38A5F8F116708A48B6891EF6911~-1~YAAQ7v3UF7+7xrWCAQAAkFGoywi4DEQqwMqpvYZ5trvjJHtIxXGoLnvCeSO+dcUG8feiSU/VbwcqoG7A8rqmbNzDOuPW0ScaMPMF9xkbVDIAbFwJ+YlvyRLBNfeY4K/SpAdBtAXsCq2ebhdp3sv9r68ejcpPsNntGYjjde8I/j7pGY70ok9P1LaIxCcbq+q5lr8C903Vki0pecO85zOoXcqQOl26RMOd+6CVAU9fw/JpAkzed24E+rPvmOGjcDJ0Ln26RjzkXtpvg7NJ3yI61+HaNK7ZM0NnKUGV26pz6VVEut0hHEv/a9qZao0WDF9ZGqYRhSoDbbLf20cSAdzih3Muwdltp761oaKi4bUb5Ot+yPOx96v5Pub34cvF7ldhDGEjF/KHVhlzVzfvPw/uc32LdR2sILvE~0~-1~1661277681; ak_bmsc=BB220FA0E75DA72730129649FCEEA8F5~000000000000000000000000000000~YAAQ7v3UF8C7xrWCAQAAkFGoyxAuFx2Y0rgOgNo2UHY6CvecIcb9TYFIjTWLbbzNX37a25KGAIdvMLV+qBFnAdifr/0foWuzPyWqACPmX7Uo0C6a7lTLKThoV2Ys81Kky9qCJrNXXvSo3yQu5nF01VPmB3tyGz/mo8y4cBkfQoPfeaT2EOJliE/vMDLeOUlolDWMdByH+DfQrfFn9QEX9o6iHTf22/Cv7jU1z9iQQ7tlztKLo8WIJt5V/mTpGyI8rm2sgDpny9aF6FIL0LCYJMzddtpIoCG9Qwcy8RoFemzLw+tsdJpbAP9CwbNHQuPvUzA6+lFfXB5rX9lLS1CsL1ptkVGCDogOe+njYBWQBK1fG4WgyFr7uRf4mpRkwa2qDn8hLGc/DrB+hdGmDmiIVUj+Xbhtw5BNozPqqqz96DmegRWMHrBIKP0oY3KZIDY08mhy3rp5QM2HFT8RlURVuFRz/oyVoZtd27yZccdMk7Y1gFzuiW8PD+YiS2EbZVar2Qf0GXef0mFa0IM9BeAB95HUVtMY/S1mf0rACTJp0tpoedypcHNnxFH5v5opp02ucVMTLBfvx3d6TwiOW0AVomSeiUFo1qd6o4Eg90VN/Nx37WI7Wzf166erAgMBVT7dZWSCsM7m+nt5onTiG/f6NaUWKhW18zDgPerT6AOeCgRCgea7; bm_sv=268868EE94488D10D7425FA9BCF45E3F~YAAQ7v3UF8G7xrWCAQAAkFGoyxCY7zQCk+buz3BHUd00Kxr5ZE74ao7TNqKUQGsXGNTPVNssRlkbEMSFe0/QOldeLA87N4j85kdAhKOkoZoLtuVkcH+nVYI5aGmuKHby5K+SaAAJaGgBqU0LYd8HsaNCexGMLdhyRI+ZlMtqjg74jOat46B9HQjaN+CJc1Kg0dybdE6L+PH+/U7G8Ah2IIfNhJG5q0icDYm5QvsF4NTle6yjVHlTFOyp7/FTL37ByQ==~1'
    }

    print("SENDING...")
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def postman_http(image_path):
    import http.client
    import mimetypes
    from codecs import encode

    conn = http.client.HTTPSConnection("www.myntra.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('img_1.png')))

    fileType = mimetypes.guess_type(image_path)[0] or 'application/octet-stream'
    dataList.append(encode('Content-Type: {}'.format(fileType)))
    dataList.append(encode(''))

    with open(image_path, 'rb') as f:
        dataList.append(f.read())
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'authority': 'www.myntra.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en;q=0.9',
        'cookie': '_ga=GA1.2.1385274995.1657119821; ajs_user_id=c68c2a72.0210.4e29.a315.9670da4cc8e8gP0MwYxAzB; ajs_anonymous_id=cdab7aad-e59c-4eaf-9858-0c6cdd4dd8a9; _d_id=13055444-563c-4538-bf92-d51733410002; mynt-eupv=1; _gcl_au=1.1.429627758.1658247312; tvc_VID=1; _fbp=fb.1.1658247313922.859470584; _cc_id=13df44067fe935753c3404ed5b3d3307; G_ENABLED_IDPS=google; ilgim=true; user_uuid=bac56e77.7a1f.4a90.a20f.6e4ec0f2104dR5cTTDexpX; sc_tt=true; _gcl_aw=GCL.1658337901.Cj0KCQjwz96WBhC8ARIsAATR252ZTFjGlAclGTNaVjkDeoYZNp_1kaMoL1ENJz_pFbXvvIth1ZNdibMaApoAEALw_wcB; _gac_UA-1752831-18=1.1658337901.Cj0KCQjwz96WBhC8ARIsAATR252ZTFjGlAclGTNaVjkDeoYZNp_1kaMoL1ENJz_pFbXvvIth1ZNdibMaApoAEALw_wcB; uidx=bac56e77.7a1f.4a90.a20f.6e4ec0f2104dR5cTTDexpX; webVitals=true; panoramaId_expiry=1661509522147; panoramaId=3a5d610bbe6c138d75752041a19f16d539380a96f291236cae0be0a548697eed; vw=400; __cab=cart.fsexp%3D; oee_expiry_hide=121013252683866570003; mynt-ulc=pincode:560103|addressId:380421695; oai=380421695; oaui=380421695:2; mws=false; _abck=0C56CDB4BFD536A9C6B6FBFDC53D8E18~0~YAAQdmPUF6ZWWbWCAQAAZd8Fuwg0/xr+qgPbULuTj6L1l+XNcK+yrbpliWdu6/Qm9rCm+9R+h8CHTAg++87+Q52aVmJwmpo6DBaOVwhT7e3F7LQ48bUKf/bx1OV47xNXt38elCANWag7ld1dyhwvUSx6XsUiLlQP2gEI+7Glm5HFnDGSM5SMcePjUdveTru+Id879dhinX2iyHpkPcL2fPnPWcn4ppg802L5oesAp2RF3dhSt1CdmAEPw1KfODnSdUofymEvZ0i4jXUKu21qi1kgCUOSSICSll47iJ9Z6yRHNAuWhIn0IK/ZjHzan5xMyYKqwfCitGe0fU48z+x7JdFtARnD32c3cgaN0QVmJO1naE38a4W5R0bYEdEHVB2XncZb0mtu/EwWQywRZx6iHzJXP+9d1ilw~-1~-1~-1; _gid=GA1.2.1818588783.1661165731; mynt-ulc-api=pincode%3A560002; __insp_wid=617845923; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cubXludHJhLmNvbS8xMzIzNzQwMA%3D%3D; __insp_targlpt=QnV5IEFub3VrIFdvbWVuIEJsYWNrICYgV2hpdGUgUHJpbnRlZCBTdHJhaWdodCBLdXJ0YSAtIEt1cnRhcyBmb3IgV29tZW4gMTMyMzc0MDAgfCBNeW50cmE%3D; __insp_norec_sess=true; __insp_slim=1661258747253; vh=823; ismd=1; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bpdp.web.savedAddress%3Denabled%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.payment.dope%3Ducretryfirst%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled%3Bpayments.iconrevamp%3Ddisabled%3BMyntra_icon_all_Pages%3Ddisabled%3Bpdp.autoapply.newusercoupon%3Ddisabled; _pv=default; microsessid=661; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661289003%2C%22trackend%22%3A1661289063%7D; lt_timeout=1; lt_session=1; at=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUpoY0hCT1lXMWxJam9pYlhsdWRISmhJaXdpYVhOeklqb2lTVVJGUVNJc0luUnZhMlZ1WDNSNWNHVWlPaUpoZENJc0luTjBiM0psU1dRaU9pSXlNamszSWl3aWJITnBaQ0k2SW1FNE9EQTJPVE01TFRsbU16VXRORGhtWkMxaE5HRmtMVEkwTnpnNE1UTXhaakJrWkMweE5qVTRNalEzTXpNM05EUTBJaXdpY0NJNklqSXlPVGNpTENKamFXUjRJam9pYlhsdWRISmhMVEF5WkRka1pXTTFMVGhoTURBdE5HTTNOQzA1WTJZM0xUbGtOakprWW1WaE5XVTJNU0lzSW5OMVlsOTBlWEJsSWpvd0xDSnpZMjl3WlNJNklrSkJVMGxESUZCUFVsUkJUQ0lzSW1WNGNDSTZNVFkyTVRJNU1qWXdNeXdpYm1sa2VDSTZJbVkzTlRrNU1UTTFMVEEzTjJRdE1URmxaQzA1Tm1aaUxUQXdNR1F6WVdZeU9HVTBNU0lzSW1saGRDSTZNVFkyTVRJNE9UQXdNeXdpZFdsa2VDSTZJbUpoWXpVMlpUYzNMamRoTVdZdU5HRTVNQzVoTWpCbUxqWmxOR1ZqTUdZeU1UQTBaRkkxWTFSVVJHVjRjRmdpZlEuazFsd3htblNuTEZVOGdlcHlOVjRrM3pPOUFWMjkybTE4VENLRXdwdlJNdEFpdmhzWk5BTV9RaTFYc29xOFhTQlozR1VJa1R1QXVpWTFwb0pxZVlRa1UzNERseGhMeWpUMHItZzhraXJ2MlJXVkU1bmhDSUxmUU85Z0FCTWtNOWVRa1hTYXEzWUVWbzRXRDdHdl9JdVlDSnhVbjJRV2laMGR6UFg3R3Exb0NN; rt=ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqSWlmUS5leUp5ZEdsM0lqb3lNek15T0RBd01Dd2lZWEJ3VG1GdFpTSTZJbTE1Ym5SeVlTSXNJbWx6Y3lJNklrbEVSVUVpTENKMGIydGxibDkwZVhCbElqb2ljblFpTENKemRHOXlaVWxrSWpvaU1qSTVOeUlzSW14emFXUWlPaUpoT0Rnd05qa3pPUzA1WmpNMUxUUTRabVF0WVRSaFpDMHlORGM0T0RFek1XWXdaR1F0TVRZMU9ESTBOek16TnpRME5DSXNJbkFpT2lJeU1qazNJaXdpZEc5dUlqb3hOall4TWpnNU1EQXpMQ0p5ZEhRaU9qRXNJbU5wWkhnaU9pSnRlVzUwY21FdE1ESmtOMlJsWXpVdE9HRXdNQzAwWXpjMExUbGpaamN0T1dRMk1tUmlaV0UxWlRZeElpd2ljM1ZpWDNSNWNHVWlPakFzSW5OamIzQmxJam9pUWtGVFNVTWdVRTlTVkVGTUlpd2laWGh3SWpveE5qZzBOakUzTURBekxDSnVhV1I0SWpvaVpqYzFPVGt4TXpVdE1EYzNaQzB4TVdWa0xUazJabUl0TURBd1pETmhaakk0WlRReElpd2lhV0YwSWpveE5qWXhNamc1TURBekxDSjFhV1I0SWpvaVltRmpOVFpsTnpjdU4yRXhaaTQwWVRrd0xtRXlNR1l1Tm1VMFpXTXdaakl4TURSa1VqVmpWRlJFWlhod1dDSjkubFJVMVAtU1ZlY2tRZkkzSGdZd1hoUkI0bl94SndtNEVaRndTTGNXdFYtNm5icFBoU2FVZnVnRHI4eGtSTnpFZkFETG5MTVdtUWk2bEVBME9Uc29rLVZqSXFXYUwyZkxKTUdkNVQydTBoejBvdW5pQ2Mxd2VaX2ZvZmVJVXczUzFsUmIyVFN4MkNLN1Jtb1Z1emFNMjhXeThFcE53UUVWVV9BdjdxOGNVOFNj; AKA_A2=A; _ma_session=%7B%22id%22%3A%22229c9ead-7a9c-4518-8f9c-4ff89c3d0cd3-13055444-563c-4538-bf92-d51733410002%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; ru=Wy1LZkFGGhFLWClVG1RSQGdBZwlCSSt8QlNsL1QKQgpraWRYF1wyHzoRAk0%2BZkAwIzE4NzAxNDYwMzgkMg%3D%3D.2b5027049fd95df5b5722f849eafc51c; _xsrf=dqeqQAtdRxdCHOZyAMCtchTou2tWN6JM; user_session=igbhz_QBQwYaLysHqiHyUA.c75khuUriLLN9K5ER907IalcgZtqIfQ8kh5w6IR_Dbaqm_BVYjkJKWfBSimRq0XG5Bggw7NCFqSJFyOZdtxchFS2TBxOk46UZQ1a46eCRJNXxqRzdB-E865l3t6sq_UIr56yT4M8bf1bKB02tmZXvWIIORbqxecXhyxEzJJBqoHZEfdY0JOu8Ik4v08KQ3L8m_n90husNRznGnbdDhL_NBaWRmk3drIOrj1QVcjIVmoV_NY5q3D1YL6WVHa7kzjWI-zxU9ZUeUtP6mgy97FSlSt9JLEwuY3s_L-4wLkdfcS8decmxjmd45eeOebaZhFsP_CbPN8lg4BeMQphkcRMn7rqhhw00Teo59NlxhI5oiYs392IbnY5Z0j9pjw16zRMEysN1ROiHsflHiulYIF9cQjZm0fmc3oYgSfXk7g6-rOKWBnIoXkn04aLflZWv8JQIU0okuMzqzp60hBQ4d86g5m43ORtov9VNbt9QU9nqOOnBVKfYede7MlRZbQoF6EJXQgkQj1hNo_loctQ6HIeLAgULTtaklR_9Z5p_VimpOQ.1661289003624.86400000.ZdUlJ3GiSTiDs6QDfeeDRRbxS0BG8-vRo13DzjwSPRM; mynt-loc-src=expiry%3A1661290444479%7Csource%3AIP; dp=d; utrid=cxdWDBoRTVQYZXgHAkFAMCMyOTM0NzAxMDgxJDI%3D.a98e52eb3b14ba92464fc6632af45bfc; newUser=false; AMP_TOKEN=%24NOT_FOUND; _gat=1; cto_bundle=GQpSNV9iSW9xcFJNZHRITmFxM05SMnJQZiUyRkNZT0gxeUwyT1AxSHJuWlYyRHhmQUhaclg4NjRXZ3EwVGZic2ZteE1BcFRLQkxVJTJGMmIlMkY3Y2w1RlpDbGxSV3h3RVRaQzNSSWFnZ3l1YmFPWU9jblZWWGFlU2YlMkJwaHk3cHpYV0ZiZjc5TEdXVkRESWZRQWpMVjRNQ1NaSGUwQVJSQSUzRCUzRA; ak_RT="z=1&dm=myntra.com&si=fea9b785-42d8-44ee-9f6a-032ebe6ced3c&ss=l76okutu&sl=1&tt=27f&rl=1&ld=27h&nu=h3ahwncf&cl=i1z',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    print("Sent")
    conn.request("POST", "/gateway/v2/visualsearch/image?page=1&rows=5", payload, headers)
    res = conn.getresponse()
    data = res.read()
    #print(res.status)
    #print(data.decode("utf-8"))
    return data.decode("utf-8")