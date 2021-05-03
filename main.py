import requests
from bs4 import BeautifulSoup

url = "https://pdaotao.ctuet.edu.vn/ajaxpro/TraCuuThongTin,PMT.Web.PhongDaoTao.ashx"

payload = "{\"currentPage\":1,\"maSinhVien\":\"2000748\",\"hoDem\":\"\",\"Ten\":\"\",\"ngaySinh\":\"\",\"maLopHoc\":\"\"}"
headers = {
  'Content-Type': 'text/plain; charset=UTF-8',
  'X-AjaxPro-Method': 'GetDanhSachSinhVien',
}

response = requests.request("POST", url, headers=headers, data=payload).text.replace('["",','').replace('"];/*','')

soup = BeautifulSoup(response, 'html.parser')

print(soup.find_all('td'))

# import requests

# url = "https://pdaotao.ctuet.edu.vn/XemLichHoc.aspx"

# querystring = {"k":"JAspUHFuGCNdt8Tyly30YA"}

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTTARGET\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__LASTFOCUS\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATE\"\r\n\r\n/wEPDwUKMTc5NTg2NTYyNg8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgJmD2QWAgIDD2QWBGYPZBYEZg8QZGQWAQIBZAIBDw8WAh4HVmlzaWJsZWhkZAICD2QWBAIDD2QWBmYPZBYCAgMPEGRkFgBkAgEPZBYGAgEPEGRkFgBkAgMPEGRkFgBkAgUPEGRkFgBkAgIPZBYEAgEPDxYEHgRUZXh0BQcyMDAwNzQ4HgdFbmFibGVkaGRkAgMPEA8WBh4NRGF0YVRleHRGaWVsZAUGVGVuRG90Hg5EYXRhVmFsdWVGaWVsZAUCSWQeC18hRGF0YUJvdW5kZ2QQFQMTLS0gQ2jhu41uIMSR4bujdCAtLQ8oMjAyMC0yMDIxKSBISzIPKDIwMjAtMjAyMSkgSEsxFQMCLTECMjYCMjUUKwMDZ2dnZGQCBg8WAh4JaW5uZXJodG1sBR9LaMO0bmcgdMOsbSB0aOG6pXkgZOG7ryBsaeG7h3UuZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBQUkY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJHJhZFNpbmhWaWVuBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkTG9wSG9jBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkTG9wSG9jBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkVHV5Q2hvbgUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJHJhZFR1eUNob24FJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciR2d1NlYXJjaFR5cGUPD2QCAmTvirPzXhDCMe0/TIlbbBe0TBVHwb6p0sUIcApjGg3ETg==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\r\n\r\n147CF116\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucPhieuKhaoSat1$RadioButtonList1\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$SearchType\"\r\n\r\nradSinhVien\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$cboHocKy3\"\r\n\r\n25\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$btnSearch\"\r\n\r\nXem lịch học\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtMaSV\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtMatKhau\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtEncodeMatKhau\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'postman-token': "a8a0d953-854d-6a6d-b1b6-3e441d878f46"
#     }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.text)