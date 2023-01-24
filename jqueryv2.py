### 0xSHALL
### SeoBarBar
### Usage: python file.py list.txt
import requests
import sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]

def check(site):
  try:
    r = requests.get(site + "/upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in r.text:
      print(site + "/upload/server/php/ -> Vuln")
      ff.write(site + "/upload/server/php/\n")
    else:
      c = requests.get(site + "/admin/server/php/", verify=False, timeout=10)
      if '{"files":[{"name":"' in c.text:
        print(site + "/admin/server/php/ -> Vuln")
        ff.write(site + "/admin/server/php/\n")
      else:
        b = requests.get(site + "/fileupload/server/php/", verify=False, timeout=10)
        if '{"files":[{"name":"' in b.text:
          print(site + "/fileupload/server/php/ -> Vuln")
          ff.write(site + "/fileupload/server/php/\n")
        else:
          k = requests.get(site + "/server/php/", verify=False, timeout=10)
          if '{"files":[{"name":"' in k.text:
            print(site + "/server/php/ -> Vuln")
            ff.write(site + "/server/php/\n")
          else:
              rx = requests.get(site + "/admin/tools/assets/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in rx.text:
      print(site + "/admin/tools/assets/jquery-file-upload/server/php/ -> Vuln")
      ff.write(site + "/admin/tools/assets/jquery-file-upload/server/php/\n")
    else:
        fx = requests.get(site + "/assets/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in fx.text:
      print(site + "/assets/jquery-file-upload/server/php/ -> Vuln")
      ff.write(site + "/assets/jquery-file-upload/server/php/\n")
    else:
        z = requests.get(site + "/assets/plugins/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in z.text:
      print(site + "/assets/plugins/jquery-file-upload/server/php/ -> Vuln")
      ff.write(site + "/assets/plugins/jquery-file-upload/server/php/\n")
    else:
            print(site + " -> Not Vuln")
  except:
    print(site + " -> Unknow Error")
    
tod = Pool(200)
tod.map(check, op)
tod.close()
tod.join()
