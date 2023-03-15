from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.mouse import*
from PPlay.sound import*
import random

janela = Window(1280,720)
mouseClick = janela.get_mouse()

botao1 = Sprite("Images/Sim.png",1)
botao1.set_position(380,480)
botao2 = Sprite("Images/Nao.png",1)
botao2.set_position(580,480)
mudarTela = 1
while True:
    janela.set_background_color([0,0,0])
    if (mouseClick.is_over_object(botao2) and mouseClick.is_button_pressed(1)):
        botao2.set_position(random.randrange(200,1080),random.randrange(200,520))
    if(mouseClick.is_over_object(botao1) and mouseClick.is_button_pressed(1)):
        mudarTela = 2
    
    if (mudarTela==1):
        botao1.draw()
        botao2.draw()
        janela.draw_text("Quer namorar comigo?",360,200,size=48,font_name="Arial",bold=False,italic=False,color=[255,0,255])
    if (mudarTela==2):
        janela.draw_text("Te amo! S2",500,300,size=48,font_name="Arial",bold=False,italic=False,color=[255,0,255])

    janela.update()