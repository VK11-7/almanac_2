import sys
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from io import BytesIO
import urllib
from datetime import datetime, timedelta
import streamlit as st

st.title('Daily Almanac')

today = datetime.today()
date1 = today.strftime("%d/%m/%Y")
tomorrow = today + timedelta(1)
date1 = tomorrow.strftime("%d/%m/%Y")

date1=urllib.parse.quote(date1)

page=requests.get('https://www.drikpanchang.com/panchang/day-panchang.html?geoname-id=1277333&date='+date1)
sheet_url = "https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/export?format=csv"
response = requests.get(sheet_url)
df = pd.read_csv(BytesIO(response.content))

soup=BeautifulSoup(page.text,'html.parser')

res = df.loc[df['Date'] == date1]

l12 = soup.find('div',class_='dpPHeaderRightContent')

a1 = {}
a1['Weekday'] = l12.span.text

l1 = soup.find('h2',class_='dpPageShortTitle')

a={}
a['Date'] = l1.text

Masa = res['Masa'].values[0]
print(Masa)

Kollamera = res['Kollam era'].values[0]
print(Kollamera)

l13 = soup.find('div',class_='dpPHeaderEventList')

c={}
c['Significance'] = l13.text.replace("\xa0","")

l2 = soup.find('div',class_='dpSunriseMoonriseCardWrapper').find_all('div',class_='dpTableCell')

d={}
for i,j in zip(range(0,len(l2), 4), range(1, len(l2),4)):
  if l2[i].text!='' and l2[i].text!=' ':
    temp = l2[i].text
    d[temp] = l2[j].text.replace("ⓘ","")
  else:
    d[temp] = d[temp] + " " + l2[j].text.replace("ⓘ","")

f={}
for i,j in zip(range(2,len(l2), 4), range(3, len(l2),4)):
  if l2[i].text!='' and l2[i].text!=' ':
    temp = l2[i].text
    f[temp] = l2[j].text.replace("ⓘ","")
  else:
    f[temp] = f[temp] + " " + l2[j].text.replace("ⓘ","")

l3 = soup.find('div',class_='dpCorePanchangCardWrapper').find_all('div',class_='dpTableCell')

e={}
for i,j in zip(range(0,len(l3), 4), range(1, len(l3),4)):
  if l3[i].text!='' and l3[i].text!=' ':
    temp = l3[i].text
    e[temp] = l3[j].text.replace("ⓘ","")
  else:
    e[temp] = e[temp] + " " + l3[j].text.replace("ⓘ","")

g={}
for i,j in zip(range(2,len(l3), 4), range(3, len(l3),4)):
  if l3[i].text!='' and l3[i].text!=' ':
    temp = l3[i].text
    g[temp] = l3[j].text.replace("ⓘ","")
  else:
    g[temp] = g[temp] + " " + l3[j].text.replace("ⓘ","")

l4 = soup.find('div',class_='dpLunarDateCardWrapper').find_all('div',class_='dpTableCell')

h={}
for i,j in zip(range(0,len(l4), 4), range(1, len(l4),4)):
  if l4[i].text!='' and l4[i].text!=' ':
    temp = l4[i].text
    h[temp] = l4[j].text.replace("ⓘ","")
  else:
    h[temp] = h[temp] + " " + l4[j].text.replace("ⓘ","")

k={}
for i,j in zip(range(2,len(l4), 4), range(3, len(l4),4)):
  if l4[i].text!='' and l4[i].text!=' ':
    temp = l4[i].text
    k[temp] = l4[j].text.replace("ⓘ","")
  else:
    k[temp] = k[temp] + " " + l4[j].text.replace("ⓘ","")

l5 = soup.find('div',class_='dpRashiNakshatraCardWrapper').find_all('div',class_='dpTableCell')

l={}
for i,j in zip(range(0,len(l5), 4), range(1, len(l5),4)):
  if l5[i].text!='' and l5[i].text!=' ':
    temp = l5[i].text
    l[temp] = l5[j].text.replace("ⓘ","")
  else:
    l[temp] = l[temp] + " " + l5[j].text.replace("ⓘ","")

m={}
for i,j in zip(range(2,len(l5), 4), range(3, len(l5),4)):
  if l5[i].text!='' and l5[i].text!=' ':
    temp = l5[i].text
    m[temp] = l5[j].text.replace("ⓘ","")
  else:
    m[temp] = m[temp] + " " + l5[j].text.replace("ⓘ","")

l6 = soup.find('div',class_='dpAyanaRituCardWrapper').find_all('div',class_='dpTableCell')

n={}
for i,j in zip(range(0,len(l6), 4), range(1, len(l6),4)):
  if l6[i].text!='' and l6[i].text!=' ':
    temp = l6[i].text
    n[temp] = l6[j].text.replace("ⓘ","")
  else:
    n[temp] = n[temp] + " " + l6[j].text.replace("ⓘ","")

o={}
for i,j in zip(range(2,len(l6), 4), range(3, len(l6),4)):
  if l6[i].text!='' and l6[i].text!=' ':
    temp = l6[i].text
    o[temp] = l6[j].text.replace("ⓘ","")
  else:
    o[temp] = o[temp] + " " + l6[j].text.replace("ⓘ","")

l7 = soup.find('div',class_='dpAuspiciousCardWrapper').find_all('div',class_='dpTableCell')

p={}
for i,j in zip(range(0,len(l7), 4), range(1, len(l7),4)):
  if l7[i].text!='' and l7[i].text!=' ':
    temp = l7[i].text
    p[temp] = l7[j].text.replace("ⓘ","")
  else:
    p[temp] = p[temp] + " " + l7[j].text.replace("ⓘ","")

q={}
for i,j in zip(range(2,len(l7), 4), range(3, len(l7),4)):
  if l7[i].text!='' and l7[i].text!=' ':
    temp = l7[i].text
    q[temp] = l7[j].text.replace("ⓘ","")
  else:
    q[temp] = q[temp] + " " + l7[j].text.replace("ⓘ","")

l8 = soup.find('div',class_='dpInauspiciousCardWrapper').find_all('div',class_='dpTableCell')

r={}
for i,j in zip(range(0,len(l8), 4), range(1, len(l8),4)):
  if l8[i].text!='' and l8[i].text!=' ':
    temp = l8[i].text
    r[temp] = l8[j].text.replace("ⓘ","")
  else:
    r[temp] = r[temp] + " " + l8[j].text.replace("ⓘ","")

s={}
for i,j in zip(range(2,len(l8), 4), range(3, len(l8),4)):
  if l8[i].text!='' and l8[i].text!=' ':
    temp = l8[i].text
    s[temp] = l8[j].text.replace("ⓘ","")
  else:
    s[temp] = s[temp] + " " + l8[j].text.replace("ⓘ","")

l9 = soup.find('div',class_='dpTamilYogaCardWrapper').find_all('div',class_='dpTableCell')

t={}
for i,j in zip(range(0,len(l9), 4), range(1, len(l9),4)):
  if l9[i].text!='' and l9[i].text!=' ':
    temp = l9[i].text
    t[temp] = l9[j].text.replace("ⓘ","")
  else:
    t[temp] = t[temp] + " " + l9[j].text.replace("ⓘ","")

u={}
for i,j in zip(range(2,len(l9), 4), range(3, len(l9),4)):
  if l9[i].text!='' and l9[i].text!=' ':
    temp = l9[i].text
    u[temp] = l9[j].text.replace("ⓘ","")
  else:
    u[temp] = u[temp] + " " + l9[j].text.replace("ⓘ","")

l10 = soup.find('div',class_='dpNivasaShoolaCardWrapper').find_all('div',class_='dpTableCell')

v={}
for i,j in zip(range(0,len(l10), 4), range(1, len(l10),4)):
  if l10[i].text!='' and l10[i].text!=' ':
    temp = l10[i].text
    v[temp] = l10[j].text.replace("ⓘ","")
  else:
    v[temp] = v[temp] + " " + l10[j].text.replace("ⓘ","")

w={}
for i,j in zip(range(2,len(l10), 4), range(3, len(l10),4)):
  if l10[i].text!='' and l10[i].text!=' ':
    temp = l10[i].text
    w[temp] = l10[j].text.replace("ⓘ","")
  else:
    w[temp] = w[temp] + " " + l10[j].text.replace("ⓘ","")

l11 = soup.find('div',class_='dpCalendarEpochCardWrapper').find_all('div',class_='dpTableCell')

x={}
for i,j in zip(range(0,len(l11), 4), range(1, len(l11),4)):
  if l11[i].text!='' and l11[i].text!=' ':
    temp = l11[i].text
    x[temp] = l11[j].text.replace("ⓘ","")
  else:
    x[temp] = x[temp] + " " + l11[j].text.replace("ⓘ","")

y={}
for i,j in zip(range(2,len(l11), 4), range(3, len(l11),4)):
  if l11[i].text!='' and l11[i].text!=' ':
    temp = l11[i].text
    y[temp] = l11[j].text.replace("ⓘ","")
  else:
    y[temp] = y[temp] + " " + l11[j].text.replace("ⓘ","")

Sudhakalainwomen = res['Sudhakala in women'].values[0]

Sudhakalainmen = res['Sudhakala in men'].values[0]

Vishakalainwomen = res['Vishakala in women'].values[0]

Vishakalainmen = res['Vishakala in men'].values[0]

Chakrabasedonvasara = res['Chakra based on vasara'].values[0]

Bodypartbasedonnakshatra = res['The Body of Kal Parusha by Nakshatra'].values[0]

Date=a['Date']
Weekday=a1['Weekday']
Sunrise=d['Sunrise']
Sunset=f['Sunset']
Moonrise=d['Moonrise']
Moonset=f['Moonset']
Samvatsara=h['Shaka Samvat']
Ayana=n['Drik Ayana']
Ritu=n['Drik Ritu']
Masa=Masa
Kollamera=Kollamera
Paksha=e['Paksha']
Tithi=e['Tithi']
Vasara=e['Weekday']
Nakshatra=g['Nakshatra']
Sunsign=l['Sunsign']
Moonsign=l['Moonsign']
Brahmamuhurta=p['Brahma Muhurta']
Pratahsandhya=q['Pratah Sandhya']
Abhijitmuhurta=p['Abhijit']
Saayamsandhya=q['Sayahna Sandhya']
Rahukalam=r['Rahu Kalam']
Yamaganda=s['Yamaganda']
Gulikaikaalam=r['Gulikai Kalam']
Significance=c['Significance']
Sudhakalainwomen=Sudhakalainwomen
Sudhakalainmen=Sudhakalainmen
Vishakalainwomen=Vishakalainwomen
Vishakalainmen=Vishakalainmen
Chakrabasedonvasara=Chakrabasedonvasara
Bodypartbasedonnakshatra=Bodypartbasedonnakshatra

message = """
Simply Ayurveda - Dainika Vaidya Almanac

✨ Suprabhatam ✨

{Date}
{Weekday}

☀️ Sunrise – {Sunrise}
🌇 Sunset – {Sunset}
🌒 Moonrise – {Moonrise}
🌃 Moonset – {Moonset}

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

msg = message.format(Date=Date, Weekday=Weekday, Sunrise=d['Sunrise'], Sunset=f['Sunset'], Moonrise=d['Moonrise'], Moonset=f['Moonset'], Samvatsara=h['Shaka Samvat'], Ayana=n['Drik Ayana'], Ritu=n['Drik Ritu'], Masa=Masa, Kollamera=Kollamera, Paksha=e['Paksha'], Tithi=e['Tithi'], Vasara=e['Weekday'], Nakshatra=g['Nakshatra'], Sunsign=l['Sunsign'], Moonsign=l['Moonsign'], Brahmamuhurta=p['Brahma Muhurta'], Pratahsandhya=q['Pratah Sandhya'], Abhijitmuhurta=p['Abhijit'], Saayamsandhya=q['Sayahna Sandhya'], Rahukalam=r['Rahu Kalam'], Yamaganda=s['Yamaganda'], Gulikaikaalam=r['Gulikai Kalam'], Significance=c['Significance'], Sudhakalainwomen=Sudhakalainwomen, Sudhakalainmen=Sudhakalainmen, Vishakalainwomen=Vishakalainwomen, Vishakalainmen=Vishakalainmen, Chakrabasedonvasara=Chakrabasedonvasara, Bodypartbasedonnakshatra=Bodypartbasedonnakshatra)

st.text(msg)
