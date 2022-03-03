# Mengimpor Library
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Menyiapkan URL
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-11-01&checkout=2021-11-02&adults=1&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&source=structured_search_input_header&search_type=autocomplete_click&federated_search_session_id=6654eed7-1239-4018-9f79-30b2edf5dfda&pagination_search=true'

# Membuat Object Page
page = requests.get(url)
page

# Menagambil Informasi Dengan Format .html Python
soup = BeautifulSoup(page.text, 'lxml')
soup

# Tutorial Pergi Ke Halaman 1,2,3,dst
hal_next = soup.find('a', {'aria-label':'Next'}).get('href')

# Tulis Alamat Link Lengkapnya
hal_next_lengkap = 'https://www.airbnb.com'+hal_next

url = hal_next_lengkap
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# Dengan Rating
dataku = pd.DataFrame({'Link':[''],
                      'Judul':[''],
                      'Harga':[''],
                      'Rating':[''],
                      'Deskripsi':['']})

# Tanpa Rating
dataku2 = pd.DataFrame({'Link':[''],
                      'Judul':[''],
                      'Harga':[''],
                      'Deskripsi':['']})

# Looping Dengan Rating
postings = soup.find_all('div', class_ = '_8ssblpx')
for post in postings:
    try:
        # LINK
        link = post.find('a', class_ = '_mm360j').get('href')
        link_lengkap = 'https://www.airbnb.com'+link
        # JUDUL
        judul = post.find('meta', {'itemprop':'name'}).get('content')
        # HARGA
        harga = post.find('span', class_ = '_tyxjp1').text
        # RATING
        rating = post.find('span', class_ = '_10fy1f8').text
        # DESKRIPSI
        deskripsi = post.find('div', class_ = '_3c0zz1').text
        dataku = dataku.append({'Link':link_lengkap,
                                'Judul':judul,
                                'Harga':harga,
                                'Rating':rating,
                                'Deskripsi':deskripsi}, ignore_index=True)
    except:
        pass
    
# Looping Tanpa Rating
for post in postings:
    # LINK
    link = post.find('a', class_ = '_mm360j').get('href')
    link_lengkap = 'https://www.airbnb.com'+link
    # JUDUL
    judul = post.find('meta', {'itemprop':'name'}).get('content')
    # HARGA
    harga = post.find('span', class_ = '_tyxjp1').text
    # DESKRIPSI
    deskripsi = post.find('div', class_ = '_3c0zz1').text
    dataku2 = dataku2.append({'Link':link_lengkap,
                              'Judul':judul,
                              'Harga':harga,
                              'Deskripsi':deskripsi}, ignore_index=True)

# Menggabungkan Semua Halaman Dengan Rating
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-11-01&checkout=2021-11-02&adults=1&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&source=structured_search_input_header&search_type=autocomplete_click&federated_search_session_id=6654eed7-1239-4018-9f79-30b2edf5dfda&pagination_search=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# Dengan Rating
dataku = pd.DataFrame({'Link':[''],
                      'Judul':[''],
                      'Harga':[''],
                      'Rating':[''],
                      'Deskripsi':['']})

while True:
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            # LINK
            link = post.find('a', class_ = '_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            # JUDUL
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            # HARGA
            harga = post.find('span', class_ = '_tyxjp1').text
            # RATING
            rating = post.find('span', class_ = '_10fy1f8').text
            # DESKRIPSI
            deskripsi = post.find('div', class_ = '_3c0zz1').text
            dataku = dataku.append({'Link':link_lengkap,
                                'Judul':judul,
                                'Harga':harga,
                                'Rating':rating,
                                'Deskripsi':deskripsi}, ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a', {'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
    except:
        print('Index Sudah Selesai Karna Berada Di Halaman Terakhir!!!')
        break
    
    # Mengupdate URL
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# Menggabungkan Semua Halaman Tanpa Rating
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-11-01&checkout=2021-11-02&adults=1&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&source=structured_search_input_header&search_type=autocomplete_click&federated_search_session_id=6654eed7-1239-4018-9f79-30b2edf5dfda&pagination_search=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# Dengan Rating
dataku2 = pd.DataFrame({'Link':[''],
                      'Judul':[''],
                      'Harga':[''],
                      'Deskripsi':['']})

while True:
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        # LINK
        link = post.find('a', class_ = '_mm360j').get('href')
        link_lengkap = 'https://www.airbnb.com'+link
        # JUDUL
        judul = post.find('meta', {'itemprop':'name'}).get('content')
        # HARGA
        harga = post.find('span', class_ = '_tyxjp1').text
        # DESKRIPSI
        deskripsi = post.find('div', class_ = '_3c0zz1').text
        dataku2 = dataku2.append({'Link':link_lengkap,
                                'Judul':judul,
                                'Harga':harga,
                                'Deskripsi':deskripsi}, ignore_index=True)
    
    try:
        hal_next = soup.find('a', {'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
    except:
        print('Index Sudah Selesai Karna Berada Di Halaman Terakhir!!!')
        break
    
    # Mengupdate URL
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml') 
    
# Menghilangkan Baris Pertama
dataku = dataku.iloc[1:]
dataku2 = dataku2.iloc[1:]

# Eksport Data To CSV
dataku.to_csv('Web_Scrap_Banyak_Halaman_Rating.csv', index=False)
dataku2.to_csv('Web_Scrap_Banyak_Halaman.csv', index=False)

data = pd.read_csv('Web_Scrap_Banyak_Halaman_Rating.csv')
data2 = pd.read_csv('Web_Scrap_Banyak_Halaman.csv')      