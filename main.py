import PiImage
import Act_weather
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date,  timedelta
from icalendar import Calendar
import requests
from config import *

if debug == False:
    import epd7in5b_V2

calendar_file = 'calendar.ics'


# ------------- inicializace z objektů ----------------
test = PiImage.Pimage(first_row_pix, width_pic,height_pic,row_pic,cell_pic,width_pic_line,font, 14)

Bimage = Image.new('1', (width_pic, height_pic), 255)
Rimage = Image.new('1', (width_pic, height_pic), 255)
draw_black = ImageDraw.Draw(Bimage)
draw_red = ImageDraw.Draw(Rimage)

poccit = Act_weather.Act_weather()
poccit.data(url_weather)
print(poccit.st_data)

# --------------- načtení dat z kalendáře ------------
r = requests.get(url)

with open(calendar_file, "wb") as file:
    file.write(r.content)

with open(calendar_file, 'rb') as file:
    calendar_data = file.read()

calendar = Calendar.from_ical(calendar_data)

# ------------funkce -----------------
def den(posun,d):
    now = datetime.now()
    den = now + timedelta(days=posun)
    vystup_format = den.strftime('%d.%m.%Y')
    den_v_tydnu = day_week[den.weekday()]
    odeslat = den_v_tydnu + " " + vystup_format
    if d == 1:
        return den_v_tydnu
    else:
        return odeslat

def calndr_find(day_today):
    return_text = []
    for component in calendar.walk():
        if component.name == 'VEVENT':
            event_date = component.get('DTSTART').dt
            event_end = component.get('DTEND').dt
            if isinstance(event_date, datetime):
                event_date = event_date.date()

            if isinstance(event_end, datetime):
                event_end = event_end.date()

            if event_date <= day_today and event_end >= day_today:
                summary = component.get('SUMMARY')
                place = component.get("LOCATION")
                start_time = component.get('DTSTART').dt.ctime()
                str_time = str(start_time)
                if place == None:
                    return_text.append(str_time[11:16] + " : " + str(summary[0:40]))
                else:
                    return_text.append(str_time[11:16] + " : " + str(summary[0:40]) + " : " + str(place[0:15]))

    return return_text


# ------------ výpočet a vykreslení řádků a buněk do listu -----------
tbl_list = test.calc_list()
test.print_line_table(tbl_list, draw_black)

 # ------------ vypsání datumů a dnů do buněk ---------------

for d in range((row_pic*cell_pic)):
    if den(d,0).find("Sobota") != -1 or den(d,0).find("Neděle") != -1:
        test.text_to_cell(draw_red, den(d, 0), tbl_list[d], 0) #  Red - black
    elif den(d,0).find("Saturday") != -1 or den(d,0).find("Sunday") != -1:
        test.text_to_cell(draw_red, den(d, 0), tbl_list[d], 0) #  Red - black
    elif den(d,0).find("Samstag") != -1 or den(d,0).find("Sonntag") != -1:
        test.text_to_cell(draw_red, den(d, 0), tbl_list[d], 0) #  Red - black
    else:
        test.text_to_cell(draw_black,den(d,0),tbl_list[d],0)

# ------------ zapsání událostí do buněk --------------

for d in range((row_pic*cell_pic)):
    today = date.today() + timedelta(d)
    text_action = calndr_find(today)
    for p in range(len(text_action)):
        tmp = text_action[p]
        if len(tmp) > 66:
            tmp = tmp[0:66]
        if text_action != None:
            test.text_to_cell(draw_red,tmp,tbl_list[d],p+1) #  Red - black

# ----------označení aktuálního dne -----------------

test.prin_line_today(draw_red,tbl_list,3) #  Red - black

# -------------- POČASÍ --------------------------

# test.print_weather_txt(draw_black,"Počasí teď",3,2 )
test.print_weather_txt(draw_black,poccit.st_place,3,2 )
test.print_weather_txt(draw_black,poccit.st_temp_today,3,20 )
test.print_weather_txt(draw_black,poccit.st_wind,3,40 )
test.print_weather_line(draw_black,100,0,100,first_row_pix)

# x_den = den(0,1)
x_pah_obr = "pic_"+ language + "/" + poccit.st_data[0][0] + ".bmp"
x_tepl = poccit.st_data[1][0] + "°C /" + poccit.st_data[2][0] + "°C"
test.print_weather_txt(draw_black,"Dnes",105,2 )
test.print_weather_txt(draw_black,poccit.st_data[0][0],105,20 )
test.print_weather_txt(draw_black,x_tepl,105,40 )
test.print_weather_bmp(Rimage,x_pah_obr,210,10)
test.print_weather_line(draw_black,275,0,275,first_row_pix)


# x_den = den(1,1)
x_pah_obr = "pic_"+ language + "/" + poccit.st_data[0][1] + ".bmp"
x_tepl = poccit.st_data[1][1] + "°C /" + poccit.st_data[2][1] + "°C"
test.print_weather_txt(draw_black,"Zítra",280,2 )
test.print_weather_txt(draw_black,poccit.st_data[0][1],280,20 )
test.print_weather_txt(draw_black,x_tepl,280,40 )
test.print_weather_bmp(Rimage,x_pah_obr,385,10)
test.print_weather_line(draw_black,450,0,450,first_row_pix)


x_den = den(2,1)
x_pah_obr = "pic_"+ language + "/" + poccit.st_data[0][2] + ".bmp"
x_tepl = poccit.st_data[1][2] + "°C /" + poccit.st_data[2][2] + "°C"
test.print_weather_txt(draw_black,x_den,455,2 )
test.print_weather_txt(draw_black,poccit.st_data[0][2],455,20 )
test.print_weather_txt(draw_black,x_tepl,455,40 )
test.print_weather_bmp(Rimage,x_pah_obr,560,10)
test.print_weather_line(draw_black,625,0,625,first_row_pix)

x_den = den(3,1)
x_pah_obr = "pic_"+ language + "/" + poccit.st_data[0][3] + ".bmp"
x_tepl = poccit.st_data[1][3] + "°C /" + poccit.st_data[2][3] + "°C"
test.print_weather_txt(draw_black,x_den,630,2 )
test.print_weather_txt(draw_black,poccit.st_data[0][3],630,20 )
test.print_weather_txt(draw_black,x_tepl,630,40 )
test.print_weather_bmp(Rimage,x_pah_obr,735,10)

# test.print_weather_bmp(Bimage,"pic/zatazeno.bmp",600,10)

if debug == True:
    Bimage.show()
    Rimage.show()

# -------------vykreslení obrazu na vaweshare display ------------

if debug == False:
    epd = epd7in5b_V2.EPD()
    epd.init()
    epd.Clear()
    epd.display(epd.getbuffer(Bimage),epd.getbuffer(Rimage))
    epd.sleep()
