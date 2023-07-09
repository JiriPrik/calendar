# Config run parameters

# Config language
language = "de" # only cs, de,en
# Config calendar "ics" link
url = "https://outlook.office365.com/owa/calendar/87100d5ea2c046dfabaf2ebe442d4932@com-it.cz/681dd8e876a84cc99b38f55572f661ae12499017570400705145/calendar.ics"

# Config link to the widget
url_pocasi2 = "https://api.wo-cloud.com/content/widget/?geoObjectKey=10654806&language=cs&region=CZ&timeFormat=HH:mm&windUnit=kmh&systemOfMeasurement=metric&temperatureUnit=celsius"
url_pocasi = "https://api.wo-cloud.com/content/widget/?geoObjectKey=1796191&language=de&region=CZ&timeFormat=HH:mm&windUnit=kmh&systemOfMeasurement=metric&temperatureUnit=celsius"



width_pic = 800
height_pic = 480
row_pic = 7
cell_pic = 2
width_pic_line = 1
font = 'fonts/wsl.ttf'
first_row_pix = 60
en = { 0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday" }
cs = { 0:"Pondělí", 1:"Úterý", 2:"Středa", 3:"Čtvrtek", 4:"Pátek", 5:"Sobota", 6:"Neděle" }
de = { 0:"Montag", 1:"Dienstag", 2:"Mittwoch", 3:"Donnerstag", 4:"Freitag", 5:"Samstag", 6:"Sonntag" }

if language == "en":
    day_week = en
elif language == "cs":
    day_week = cs
elif language == "de":
    day_week = de