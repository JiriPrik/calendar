
from PIL import Image, ImageDraw, ImageFont
class Pimage:
    def __init__(self,im_fr, im_width, im_height, im_rows, im_cols, im_border, font, size_font):
        self.st_width = im_width
        self.st_height = im_height - im_fr
        self.st_rows = im_rows
        self.st_cols = im_cols
        self.st_bord = im_border
        self.st_field = im_rows * im_cols
        self.st_sz_font = size_font
        self.st_first_row = im_fr
        self.font24 = ImageFont.truetype(font, self.st_sz_font)
        self.font20 = ImageFont.truetype(font, 14)

    # ------spočítání matice / listu buněk ---------------
    def calc_list(self):
        # calculate coordinates  width - šířka, height - výška
        width_col = round(self.st_width / self.st_cols)
        height_row = round(self.st_height / self.st_rows)
        field = self.st_rows * self.st_cols
        field_list = []
        x = 0
        y = self.st_first_row
        for one_col in range(self.st_cols):
            for jedna in range(self.st_rows):
                tmp_x = x+width_col
                tmp_y = y+height_row
                if tmp_x > self.st_width:
                    tmp_x = self.st_width
                if tmp_y > self.st_height + self.st_first_row:
                    tmp_y = self.st_height
                field_list.append([x,y,tmp_x,tmp_y])
                y +=height_row
            x += width_col
            y = self.st_first_row
        # print(field_list)
        return field_list

    # ---------zakreslení řádků -------------
    def print_line_table(self, table_list, drw):
        drw.line((0,self.st_first_row, self.st_width, self.st_first_row), fill=0,width=self.st_bord)
        for one in range(len(table_list)):
            drw.line((table_list[one][0],table_list[one][3], table_list[one][2], table_list[one][3]), fill=0, width=self.st_bord)
            drw.line((table_list[one][2],table_list[one][1], table_list[one][2], table_list[one][3]), fill=0, width=self.st_bord)


    #  ---------zápis textu do buněk ----------
    def text_to_cell(self, drw, txt, sel_tbl, position):
        pos_row = sel_tbl[1] + position + ( position * self.st_sz_font)
        pos_txt_x = sel_tbl[0]+5
        drw.text((pos_txt_x, pos_row), txt, font=self.font24, fill=0)

    # ------------ Zvýraznění aktuálního dne ---------------
    def prin_line_today(self,drw, table_list,width_line):
        drw.line((table_list[0][0], table_list[0][1], table_list[0][0], table_list[0][3]), fill=0,width=width_line)

    #  ------------ Zápis počasí do prvního řádku-----------------------
    def print_weather_bmp(self,drw,bitmap,pos_x, pos_y):
        bmp = Image.open(bitmap)
        drw.paste(bmp,(pos_x,pos_y))

    def print_weather_txt(self,drw, txt, pos_x, pos_y):
        drw.text((pos_x, pos_y), txt, font=self.font20, fill=0)

    def print_weather_line(self,drw, pos_x1, pos_y1,pos_x2, pos_y2):
        drw.line((pos_x1, pos_y1, pos_x2, pos_y2), fill=0,width=1)