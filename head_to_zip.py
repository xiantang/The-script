
def to_python_zip(text):
    items = text.split('\n')
    head_zip={}

    for item in items:
        if 'Cookie' in item:
            item=item.replace('Cookie:','')
            head_zip['Cookie']=item
        elif item.startswith(":"):
            item=item.replace(':','',1)
            key=item.split(':')
            head_zip[':'+key[0]]=key[1]
        else:
            key=item.split(':')
            head_zip[key[0]]=key[1]
    print(head_zip)
if __name__ == '__main__':
    request_Head = ''':authority:www.google.ca
:method:GET
:path:/xjs/_/js/k=xjs.s.zh_CN.RatPuRYNpgk.O/m=aa,abd,async,dvl,foot,fpe,ipv6,lu,m,mu,sf,sonic,spch,tl,vs,d3l,tnv,mrn,exdp,udlg,me,kptm,iud,iuci,shrb,dgm,qtf,tcc,atn/am=wCL0eMEByP8PAopEKwgsQJpgGBo/exm=sx,sb,cdos,cr,elog,hsm,jsa,r,d,csi/rt=j/d=1/ed=1/t=zcms/rs=ACT90oFUZZAh1baiB5gB9X__zAAB6iaufw?xjs=s1
:scheme:https
accept:*/*
accept-encoding:gzip, deflate, br
accept-language:zh,en-US;q=0.9,en;q=0.8
cookie:1P_JAR=2018-02-21-11; DV=k_FBxNmnkCIVYCnKbBlF6KJvO3mCGxY; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTUxOTIxMzA2MjY3NDAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6Mjk5MDA4NDc3IGxvbmdpdHVkZV9lNzoxMjE2MzU4NTUzfSByYWRpdXM6MTI0MDA=; NID=124=IFqIMdsjN2qpy2mn1bLf7If1nga5a_V_kVat4N9np8URiXLtHLv2_gLMFSUEbdDBz4Lz0sp1OaGwfeVPuehngEGPKKjdId6bKviZ7XVyfHqmvhm8tPVGcuOFHm4LL-QS
referer:https://www.google.ca/
user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
x-client-data:CLO1yQEIkbbJAQiitskBCKmdygEIqKPKAQ=='''
    to_python_zip(request_Head)

