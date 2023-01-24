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
    r = requests.get(site + "/assets/filemanager/dialog.php", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if 'Responsive FileManager' in r.text:
      print(site + "/assets/filemanager/dialog.php -> Vuln")
      ff.write(site + "/assets/filemanager/dialog.php\n")
    else:
      c = requests.get(site + "/asset/filemanager/dialog.php", verify=False, timeout=10)
      if 'Responsive FileManager' in c.text:
        print(site + "/asset/filemanager/dialog.php -> Vuln")
        ff.write(site + "/asset/filemanager/dialog.php\n")
      else:
        b = requests.get(site + "/filemanager/dialog.php", verify=False, timeout=10)
        if 'Responsive FileManager' in b.text:
          print(site + "/filemanager/dialog.php -> Vuln")
          ff.write(site + "/filemanager/dialog.php\n")
        else:
          k = requests.get(site + "/assets/admin/js/filemanager/", verify=False, timeout=10)
          if 'Responsive FileManager' in k.text:
            print(site + "/assets/admin/js/filemanager/ -> Vuln")
            ff.write(site + "/assets/admin/js/filemanager/\n")
          else:
              rx = requests.get(site + "/media/filemanager/dialog.php", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if 'Responsive FileManager' in rx.text:
      print(site + "/media/filemanager/dialog.php -> Vuln")
      ff.write(site + "/media/filemanager/dialog.php\n")
    else:
        fx = requests.get(site + "/assets/plugins/filemanager/dialog.php", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if 'Responsive FileManager' in fx.text:
      print(site + "/assets/plugins/filemanager/dialog.php -> Vuln")
      ff.write(site + "/assets/plugins/filemanager/dialog.php\n")
    else:
        z = requests.get(site + "/assets/admin/js/tinymce/plugins/filemanager/dialog.php", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if 'Responsive FileManager' in z.text:
      print(site + "/assets/admin/js/tinymce/plugins/filemanager/dialog.php -> Vuln")
      ff.write(site + "/assets/admin/js/tinymce/plugins/filemanager/dialog.php\n")
    else:
            print(site + " -> Not Vuln")
  except:
    print(site + " -> Unknow Error")
    
tod = Pool(200)
tod.map(check, op)
tod.close()
tod.join()
