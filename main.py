import requests
from bs4 import BeautifulSoup

def get(url):
  url = url

  payload = "{\"currentPage\":1,\"maSinhVien\":\"2000748\",\"hoDem\":\"\",\"Ten\":\"\",\"ngaySinh\":\"\",\"maLopHoc\":\"\"}"
  headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'X-AjaxPro-Method': 'GetDanhSachSinhVien',
  }

  response = requests.request("POST", url, headers=headers, data=payload).text.replace('["",','').replace('"];/*','')
  return response

soup = BeautifulSoup(get("https://pdaotao.ctuet.edu.vn/ajaxpro/TraCuuThongTin,PMT.Web.PhongDaoTao.ashx"), 'html.parser')

link = BeautifulSoup("<td><a href='\"XemLichHoc.aspx?k=JAspUHFuGCNdt8Tyly30YA\"' target='\"_blank\"'>Xem lịch học</a></td>",'html.parser').find('a')['href']

url = "https://pdaotao.ctuet.edu.vn/XemLichHoc.aspx"

querystring = {"k":link[link.find('=')+1:len(link)-1]}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTTARGET\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__LASTFOCUS\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATE\"\r\n\r\n/wEPDwUKMTc5NTg2NTYyNg8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgJmD2QWAgIDD2QWBGYPZBYEZg8QZGQWAQIBZAIBDw8WAh4HVmlzaWJsZWhkZAICD2QWBAIDD2QWBmYPZBYCAgMPEGRkFgBkAgEPZBYGAgEPEGRkFgBkAgMPEGRkFgBkAgUPEGRkFgBkAgIPZBYEAgEPDxYEHgRUZXh0BQcyMDAwNzQ4HgdFbmFibGVkaGRkAgMPEA8WBh4NRGF0YVRleHRGaWVsZAUGVGVuRG90Hg5EYXRhVmFsdWVGaWVsZAUCSWQeC18hRGF0YUJvdW5kZ2QQFQMTLS0gQ2jhu41uIMSR4bujdCAtLQ8oMjAyMC0yMDIxKSBISzIPKDIwMjAtMjAyMSkgSEsxFQMCLTECMjYCMjUUKwMDZ2dnZGQCBg8WAh4JaW5uZXJodG1sBR9LaMO0bmcgdMOsbSB0aOG6pXkgZOG7ryBsaeG7h3UuZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBQUkY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJHJhZFNpbmhWaWVuBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkTG9wSG9jBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkTG9wSG9jBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkcmFkVHV5Q2hvbgUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJHJhZFR1eUNob24FJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciR2d1NlYXJjaFR5cGUPD2QCAmTvirPzXhDCMe0/TIlbbBe0TBVHwb6p0sUIcApjGg3ETg==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\r\n\r\n147CF116\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucPhieuKhaoSat1$RadioButtonList1\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$SearchType\"\r\n\r\nradSinhVien\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$cboHocKy3\"\r\n\r\n25\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ContentPlaceHolder$btnSearch\"\r\n\r\nXem lịch học\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtMaSV\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtMatKhau\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ctl00$ucRight1$txtEncodeMatKhau\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "a8a0d953-854d-6a6d-b1b6-3e441d878f46"
    }

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers, params=querystring)

raw = response.text

lichHoc = BeautifulSoup(raw,'html.parser').find_all(id='detailTbl')[0]

def getSubject():
  tempBuoiSang = []
  tempBuoiChieu = []
  tempBuoiToi = []
  monBuoiSang = {}
  monBuoiChieu = {}
  monBuoiToi = {}
  phanLoaiTheoNgay = {}
  phanLoaiTheoThang = {'11':{}}
  for i in range(7):
    timMonBuoiSang = lichHoc.find_all('tr',recursive=False)[i+((i*2)+1)]
    timMonchieu = lichHoc.find_all('tr',recursive=False)[i+((i*2)+2)]
    timMontoi = lichHoc.find_all('tr',recursive=False)[i+((i*2)+3)]
    tempBuoiSang.append(timMonBuoiSang.find_all('tr'))
    tempBuoiChieu.append(timMonchieu.find_all('tr'))
    tempBuoiToi.append(timMontoi.find_all('tr'))

  monBuoiSang['thu2']=tempBuoiSang[0]
  for i in range(1,6):
    monBuoiSang['thu{}'.format(i+2)]=tempBuoiSang[i]
  monBuoiSang['chunhat']=tempBuoiSang[len(tempBuoiSang)-1]

  monBuoiChieu['thu2']=tempBuoiChieu[0]
  for i in range(1,6):
    monBuoiChieu['thu{}'.format(i+2)]=tempBuoiChieu[i]
  monBuoiChieu['chunhat']=tempBuoiChieu[len(tempBuoiChieu)-1]

  monBuoiToi['thu2']=tempBuoiToi[0]
  for i in range(1,6):
    monBuoiToi['thu{}'.format(i+2)]=tempBuoiToi[i]
  monBuoiToi['chunhat']=tempBuoiToi[len(tempBuoiToi)-1]

  for i in monBuoiSang['thu2']:
    temp=[]
    dateHandler = i.find_all('td')[5].text
    date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
    monHoc = ' '.join(i.find_all('td')[1].text.split())
    tietHoc = ' '.join(i.find_all('td')[2].text.split())
    giangVien = ' '.join(i.find_all('td')[3].text.split())
    phongHoc = ' '.join(i.find_all('td')[4].text.split())
    temp.append({'buoi':'sang','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
    phanLoaiTheoNgay[date]=temp
  for i in range(1,6):
    for j in monBuoiSang['thu{}'.format(i+2)]:
        temp=[]
        dateHandler = j.find_all('td')[5].text
        date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
        monHoc = ' '.join(j.find_all('td')[1].text.split())
        tietHoc = ' '.join(j.find_all('td')[2].text.split())
        giangVien = ' '.join(j.find_all('td')[3].text.split())
        phongHoc = ' '.join(j.find_all('td')[4].text.split())
        temp.append({'buoi':'sang','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
        phanLoaiTheoNgay[date]=temp
  for i in monBuoiSang['chunhat']:
      temp=[]
      dateHandler = i.find_all('td')[5].text
      date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
      monHoc = ' '.join(i.find_all('td')[1].text.split())
      tietHoc = ' '.join(i.find_all('td')[2].text.split())
      giangVien = ' '.join(i.find_all('td')[3].text.split())
      phongHoc = ' '.join(i.find_all('td')[4].text.split())
      temp.append({'buoi':'sang','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      phanLoaiTheoNgay[date]=temp  

  for i in monBuoiChieu['thu2']:
    temp=[]
    dateHandler = i.find_all('td')[5].text
    date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
    monHoc = ' '.join(i.find_all('td')[1].text.split())
    tietHoc = ' '.join(i.find_all('td')[2].text.split())
    giangVien = ' '.join(i.find_all('td')[3].text.split())
    phongHoc = ' '.join(i.find_all('td')[4].text.split())
    if date in list(phanLoaiTheoNgay.keys()):
      phanLoaiTheoNgay[date].append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
    else:
      temp.append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      phanLoaiTheoNgay[date]=temp

  for i in range(1,6):
    for j in monBuoiChieu['thu{}'.format(i+2)]:
      temp=[]
      dateHandler = j.find_all('td')[5].text
      date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
      monHoc = ' '.join(j.find_all('td')[1].text.split())
      tietHoc = ' '.join(j.find_all('td')[2].text.split())
      giangVien = ' '.join(j.find_all('td')[3].text.split())
      phongHoc = ' '.join(j.find_all('td')[4].text.split())
      if date in list(phanLoaiTheoNgay.keys()):
        phanLoaiTheoNgay[date].append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      else:
        temp.append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
        phanLoaiTheoNgay[date]=temp

  for i in monBuoiChieu['chunhat']:
    temp=[]
    dateHandler = i.find_all('td')[5].text
    date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
    monHoc = ' '.join(i.find_all('td')[1].text.split())
    tietHoc = ' '.join(i.find_all('td')[2].text.split())
    giangVien = ' '.join(i.find_all('td')[3].text.split())
    phongHoc = ' '.join(i.find_all('td')[4].text.split())
    if date in list(phanLoaiTheoNgay.keys()):
      phanLoaiTheoNgay[date].append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
    else:
      temp.append({'buoi':'chieu','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      phanLoaiTheoNgay[date]=temp


  for i in monBuoiToi['thu2']:
    temp=[]
    dateHandler = i.find_all('td')[5].text
    date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
    monHoc = ' '.join(i.find_all('td')[1].text.split())
    tietHoc = ' '.join(i.find_all('td')[2].text.split())
    giangVien = ' '.join(i.find_all('td')[3].text.split())
    phongHoc = ' '.join(i.find_all('td')[4].text.split())
    if date in list(phanLoaiTheoNgay.keys()):
      phanLoaiTheoNgay[date].append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
    else:
      temp.append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      phanLoaiTheoNgay[date]=temp

  for i in range(1,6):
    for j in monBuoiToi['thu{}'.format(i+2)]:
        dateHandler = j.find_all('td')[5].text
        date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
        monHoc = ' '.join(j.find_all('td')[1].text.split())
        tietHoc = ' '.join(j.find_all('td')[2].text.split())
        giangVien = ' '.join(j.find_all('td')[3].text.split())
        phongHoc = ' '.join(j.find_all('td')[4].text.split())
        if date in list(phanLoaiTheoNgay.keys()):
          phanLoaiTheoNgay[date].append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
        else:
          temp.append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
          phanLoaiTheoNgay[date]=temp

  for i in monBuoiToi['chunhat']:
    dateHandler = i.find_all('td')[5].text
    date = dateHandler[dateHandler.find(':')+1:dateHandler.find(' ')].strip('\n').strip('\r')
    monHoc = ' '.join(i.find_all('td')[1].text.split())
    tietHoc = ' '.join(i.find_all('td')[2].text.split())
    giangVien = ' '.join(i.find_all('td')[3].text.split())
    phongHoc = ' '.join(i.find_all('td')[4].text.split())
    if date in list(phanLoaiTheoNgay.keys()):
      phanLoaiTheoNgay[date].append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
    else:
      temp.append({'buoi':'toi','mon_hoc':monHoc[0:monHoc.find('(')-1],'tiet_hoc':tietHoc,'giang_vien':giangVien,'phong_hoc':phongHoc})
      phanLoaiTheoNgay[date]=temp

  for i in range(1,13):
    temp=[]
    if i < 10:
      for j in phanLoaiTheoNgay.keys():
        if('-0{}-'.format(i) in j):
          temp.append({j:phanLoaiTheoNgay[j]})
      phanLoaiTheoThang['0{}'.format(i)]=temp
    else:
      for j in phanLoaiTheoNgay.keys():
        if('-{}-'.format(i) in j):
          temp.append({j:phanLoaiTheoNgay[j]})
      phanLoaiTheoThang['{}'.format(i)]=temp

  return phanLoaiTheoThang

from flask import Flask,jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/LayLichHoc')
def hello_world():
    return jsonify({'data':getSubject()})

app.run()