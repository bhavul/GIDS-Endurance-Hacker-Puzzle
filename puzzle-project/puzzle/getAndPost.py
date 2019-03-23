import requests
import re

key = 'abcdefghijklmnopqrstuvwxyz'
name = "BHAVUL TEST THREE"
email = "ttttt@tttt.com"
contact = "7667676676"
urlSignup = "http://103.211.218.86/GIDS2017/"
urlNew = "http://103.211.218.86/GIDS2017/teesra.pt"

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


s = requests.session()
values = {'name':name,'email':email,'contact':contact}
r = s.post(urlSignup, data=values)
html = r.text
print html
if(re.search('So, you have 1 second to decrypt the random string <strong>(.*)</strong> and submit it', html) != None):
    match = re.search('So, you have 1 second to decrypt the random string <strong>(.*)</strong> and submit it', html)
    stringToDecrypt = match.group(1)
    print stringToDecrypt
    stringToPost = decrypt(9,stringToDecrypt)
    dataNew = {'answer':stringToPost}
    r2 = s.post(urlNew,data=dataNew)
    print r2.text
    print "done, mostly."
