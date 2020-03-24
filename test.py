import pyxel
 
HEIGHT = 128
WIDTH = 128
PIC_H = 64
PIC_W = 64

BUTTOM_WIDTH=16
BUTTOM_HEIGHT=16
 
class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="揃えろ！")
        pyxel.load("./assets/my_resource.pyxres", True, False, False, False)
        self.img_border_1=decide_border()
        self.img_border_2=decide_border()
        self.img_border_3=decide_border()

        self.img_speed_1=decide_speed()
        self.img_speed_2=decide_speed()
        self.img_speed_3=decide_speed()

        self.init_flug=True

        pyxel.run(self.update, self.draw)
 

    def update(self):
        if self.init_flug:
            self.start_move_img()
            self.init_flug=False
        
        self.img_border_1+=self.img_speed_1
        self.img_border_2+=self.img_speed_2
        self.img_border_3+=self.img_speed_3
        if self.img_border_1>=PIC_H:
            self.img_border_1-=PIC_H
        if self.img_border_2>=PIC_H:
            self.img_border_2-=PIC_H
        if self.img_border_3>=PIC_H:
            self.img_border_3-=PIC_H

        #1,2,3ボタンで画像を止める処理
        if pyxel.btnp(pyxel.KEY_1):
            if self.img_speed_1 != 0:
                self.img_speed_1 = 0
            else:
                self.img_speed_1=decide_speed()
        
        if pyxel.btnp(pyxel.KEY_2):
            if self.img_speed_2 != 0:
                self.img_speed_2 = 0
            else:
                self.img_speed_2=decide_speed()

        if pyxel.btnp(pyxel.KEY_3):
            if self.img_speed_3 != 0:
                self.img_speed_3 = 0
            else:
                self.img_speed_3=decide_speed()

        #spaceボタンで、再び動かす処理
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.start_move_img()

        #アプリ終了操作
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def start_move_img(self):
        #画像を動かす処理
        self.img_speed_1=decide_speed()
        self.img_speed_2=decide_speed()
        self.img_speed_3=decide_speed()
 

    def draw(self):
        pyxel.cls(0)
        #背景の画像
        pyxel.blt(0, 0, 2, 0, 0, 128, 128)

        #動く画像部分
        pyxel.blt( 31,           17, 0, 0,         self.img_border_1, PIC_W/3, PIC_H, 5)
        pyxel.blt( 31+PIC_W/3,   17, 0, PIC_W/3,   self.img_border_2, PIC_W/3, PIC_H, 5)
        pyxel.blt( 31+PIC_W/3*2, 17, 0, PIC_W/3*2, self.img_border_3, PIC_W/3, PIC_H, 5)

        #ボタンの描画
        if self.img_speed_1 != 0:
            pyxel.blt(31, 85, 1, 0, 0, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)
        else:
            pyxel.blt(31, 85, 1, 16, 0, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)

        if self.img_speed_2 != 0:
            pyxel.blt(31+(PIC_W/3)+1, 85, 1, 0, 16, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)
        else:
            pyxel.blt(31+(PIC_W/3)+1, 85, 1, 16, 16, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)

        if self.img_speed_3 != 0:
            pyxel.blt(31+(PIC_W/3)*2+1, 85, 1, 0, 32, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)
        else:
            pyxel.blt(31+(PIC_W/3)*2+1, 85, 1, 16, 32, BUTTOM_WIDTH, BUTTOM_HEIGHT, 5)


import random
def decide_speed():
    return random.randint(1, 3)

def decide_border():
    return random.randint(0, PIC_H)


App()
