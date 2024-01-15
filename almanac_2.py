import sys
import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from io import BytesIO
import urllib
from datetime import datetime, timedelta


today = datetime.today()
date1 = today.strftime("%d/%m/%Y")
# tomorrow = today + timedelta(1)
# date1 = tomorrow.strftime("%d/%m/%Y")


date1=urllib.parse.quote(date1)

try:

    page=requests.get('https://www.drikpanchang.com/panchang/day-panchang.html?geoname-id=1277333&date='+date1)
    sheet_url = "https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/export?format=csv"
    response = requests.get(sheet_url)
    df = pd.read_csv(BytesIO(response.content))
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('ERROR FOR LINK:',url)
    print (error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
l1=soup.find_all('div',attrs={'class':'dpPHeaderRightContent'})
l2=soup.find_all('div',attrs={'class':'dpTableCell dpTableValue'})


res = df.loc[df['Date'] == date1]


g1=l1[0].text
q1 = g1.split()
Date=q1[0][0:2]+' '+q1[0][2:]+' '+q1[1][0:4]
Weekday=q1[1][4:]


g2=l2[0].text
Sunrise = g2


g3=l2[1].text
Sunset = g3


g4=l2[2].text
Moonrise = g4


g5=l2[3].text
Moonset = g5


g6=l2[16].text.split()
Samvatsara = g6[1]


g7=l2[38].text
Ayana = g7


g8=l2[34].text
Ritu = g8


Masa = res['Masa'].values[0]


Kollamera = res['Kollam era'].values[0]


g11=l2[14].text
Paksha = g11


g12=l2[4].text+' '+l2[6].text
Tithi = g12


g13=l2[12].text
Vasara = g13[:-1]


g14=l2[5].text+' '+l2[7].text
Nakshatra = g14


g15=l2[26].text
Sunsign = g15


g16=l2[22].text+' '+l2[24].text
Moonsign = g16


g17=l2[42].text
Brahmamuhurta = g17


g18=l2[43].text
Pratahsandhya = g18


g19=l2[44].text
Abhijitmuhurta = g19


g19=l2[47].text
Saayamsandhya = g19


g20=l2[54].text
Rahukalam = g20


g21=l2[55].text
Yamaganda = g21


g22=l2[58].text
Gulikaikaalam = g22


g23=l2[0].text.split()
Significance = g23[9:]
sig = ''
for i in Significance:
  sig = sig+i+' '
Significance = sig


Sudhakalainwomen = res['Sudhakala in women'].values[0]


Sudhakalainmen = res['Sudhakala in men'].values[0]


Vishakalainwomen = res['Vishakala in women'].values[0]


Vishakalainmen = res['Vishakala in men'].values[0]


Chakrabasedonvasara = res['Chakra based on vasara'].values[0]


Bodypartbasedonnakshatra = res['The Body of Kal Parusha by Nakshatra'].values[0]


message = """
Simply Ayurveda - Dainika Vaidya Almanac

✨ Suprabhatam ✨

{Date}
{Weekday}

☀️ Sunrise – {Sunrise} am
🌇 Sunset – {Sunset} pm
🌒 Moonrise – {Moonrise} pm
🌃 Moonset – {Moonset} am

Samvatsara – {Samvatsara}
Ayana - {Ayana}
Ritu – {Ritu}
Masa - {Masa}
Kollam era – {Kollamera}
Paksha – {Paksha}
Tithi – {Tithi}
Vasara – {Vasara}
Nakshatra – {Nakshatra}
Sunsign – {Sunsign}
Moonsign – {Moonsign}

✨ Auspicious hours -✨
🪷 Brahma muhurta – {Brahmamuhurta}
🌼 Pratah sandhya – {Pratahsandhya}
🌸 Abhijit muhurta – {Abhijitmuhurta}
🌼 Saayam sandhya – {Saayamsandhya}

🛑 Hours to be careful around
❌Rahu kalam – {Rahukalam}
‼️Yama ganda – {Yamaganda}
💊Gulikai Kaalam – {Gulikaikaalam}

Significance – {Significance}

🩺✡️ Medicoastrological significance -
Sudhakala in women – {Sudhakalainwomen}🚺
Sudhakala in men – {Sudhakalainmen}🚹
Vishakala in women – {Vishakalainwomen}🦳
Vishakala in men – {Vishakalainmen}🧔🏻‍♂
Chakra based on vasara – {Chakrabasedonvasara}

Body of Kala Purusha according to Nakshatra –

{Bodypartbasedonnakshatra}

Have we missed anything important?
Message Simply Ayurveda on WhatsApp. https://wa.me/message/DTX6RK5L6HE3B1
Subscribe to our YouTube channel - https://youtube.com/c/SimplyAyurveda
"""


msg = message.format(Date=Date, Weekday=Weekday, Sunrise=Sunrise, Sunset=Sunset, Moonrise=Moonrise, Moonset=Moonset, Samvatsara=Samvatsara, Ayana=Ayana, Ritu=Ritu, Masa=Masa, Kollamera=Kollamera, Paksha=Paksha, Tithi=Tithi, Vasara=Vasara, Nakshatra=Nakshatra, Sunsign=Sunsign, Moonsign=Moonsign, Brahmamuhurta=Brahmamuhurta, Pratahsandhya=Pratahsandhya, Abhijitmuhurta=Abhijitmuhurta, Saayamsandhya=Saayamsandhya, Rahukalam=Rahukalam, Yamaganda=Yamaganda, Gulikaikaalam=Gulikaikaalam, Significance=Significance, Sudhakalainwomen=Sudhakalainwomen, Sudhakalainmen=Sudhakalainmen, Vishakalainwomen=Vishakalainwomen, Vishakalainmen=Vishakalainmen, Chakrabasedonvasara=Chakrabasedonvasara, Bodypartbasedonnakshatra=Bodypartbasedonnakshatra)


print(msg)