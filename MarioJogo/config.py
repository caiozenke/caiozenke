#mapa
blocos_tam= 64
tela_largura =1200
mapa = [
'                            ',#0
'                            ',#1
'                            ',#2
'       XXXX           XX    ',#3
'X  P       X                ',
'XXXXX         XX         XX ',   #64 px
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
#0 
            #64 px

tela_altura =  len(mapa) *blocos_tam

#cores
blocos_cor = '#04BF8A'
personagem_cor = '#03A64A'
back_cor = '#024059'


#Camera Bordas

camera_borda = {
    'direita' : 200 ,
    'esquerda' : 100,
    'top' : 100,
    'baixo' : 150  
} 