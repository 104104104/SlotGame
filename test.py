import pyxel
 
HEIGHT = 80
WIDTH = 128
PIC_H = 64
PIC_W = 64
 
class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="揃えろ！")
        #pyxel.image(1).load(0, 0, "./assets/cat_16x16.png")
        pyxel.load("./assets/my_resource.pyxres", True, False, False, False)
        
        #self.img1_x=0
        #self.img1_y=0
        self.img_border_1=0

        pyxel.run(self.update, self.draw)
 

    def update(self):
        self.img_border_1+=1
        if self.img_border_1>=PIC_H:
            self.img_border_1=0



        #アプリ終了操作
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 

    def draw(self):
        pyxel.cls(0)
        pyxel.blt( (WIDTH-PIC_W)/2, (HEIGHT-PIC_H)/2, 0, 0, self.img_border_1, PIC_W, PIC_H, 12)
 
App()
