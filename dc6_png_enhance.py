
import glob
import os
import requests
import shutil
import subprocess
import time

# deep ai image superresolution model API
url = 'https://api.deepai.org/api/torch-srgan'
# this is a trial key. with a free sign-up you get your own key
# if you run out of the trial, this will appear in the response
# {'status': "Looks like you're enjoying our API. Want to keep using it? 
# Sign up to get an API Key that's as unique as you are. It's free! https://deepai.org/"}
headers={"api-key":"quickstart-QUdJIGlzIGNvbWluZy4uLi4K"}


def dl_hd_img(filename):
  files = {'image': open(filename, 'rb')}
  time.sleep(5)
  rr = requests.post(url, files=files, headers=headers)
  if rr.status_code == 200:
    
    urlimg = rr.json()['output_url']

    respimg = requests.get(urlimg, stream=True)
    filen_out = './png-hd/' + os.path.basename(filename.replace('.png', '-hd.png'))
    with open(filen_out, 'wb') as out_file:
      shutil.copyfileobj(respimg.raw, out_file)
    del respimg

  return rr.status_code


files_dc6 = glob.glob('dc6/*dc6')

for filen in files_dc6:
  print(f' \n\n-------------- starting {filen}')
  cmd = '.\\dc6con.exe ' + filen
  subprocess.run(cmd, shell=True, check=True)

  cmd = 'convert ' + filen.replace('.dc6', '.pcx').replace('.DC6', '.pcx') + ' ' + filen.replace('.dc6', '.png').replace('.DC6', '.png')
  subprocess.run(cmd, shell=True, check=True)


files_png = glob.glob('dc6/*.png')
files_png = [f for f in files_png if '-hd.png' not in f]
for i, filen in enumerate(files_png):
  print(f' \n\n ------- {i} ------- starting {filen}')
  statuscode = dl_hd_img(filen)
  
  if statuscode != 200:
    break
