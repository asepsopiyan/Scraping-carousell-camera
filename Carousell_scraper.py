import requests
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/photography-6/'
contents = requests.get(url)

soup = BeautifulSoup(contents.text, 'html.parser')
recent_camera = soup.findAll('div','D_wx M_vb D_K')
recent_camera = recent_camera[0]

# datas = recent_camera.findAll('a', 'D_lw M_cq')
#
for d in recent_camera:
    try:
        title = d.find('p', 'D_hg M_gE D_fK M_bR D_hh M_gF D_hk M_gI D_hm M_gK D_hp M_gN D_hs M_gQ D_hc').text

        price = d.find('p', 'D_hg M_gE D_fK M_bR D_hh M_gF D_hk M_gI D_hm M_gK D_hp M_gN D_hr M_gP D_hb').text.split()
        price = price[1].strip('Rp')

        desc = d.find('p', 'D_hg M_gE D_fK M_bR D_hh M_gF D_hk M_gI D_hm M_gK D_hp M_gN D_hr M_gP D_hc').text

        image = d.find('img')['src']

    except AttributeError:
        continue


    print(image)
