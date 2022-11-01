Importarcopia
Importarsys
Importarpygame
Importaraleatoriamente
ImportarnumpycomoNP

desdela importación de constantes *

# --- CONFIGURACIÓN DE PYGAME ---

pygame. Init()
screen=pygame. pantalla. set_mode( (ANCHO,ALTO) )
pygame. pantalla. set_caption(«TIC TAC TOE AI»)
pantalla. relleno(BG_COLOR )

# --- CLASES ---

Junta de clase:

    def __init__(self):
        yo mismo. cuadrados=np. ceros( (FILAS,COLS) )
        yo mismo. empty_sqrs=yo.  cuadrados# [cuadrados]
        yo mismo. marked_sqrs=0

    deffinal_state(self,show=False):
        '''
@return 0 si aún no hay victoria
@return 1 si el jugador 1 gana
@return 2 si el jugador 2 gana
        '''

        # victorias verticales
        paracolinrange(COLS):
            sies propio. cuadrados[0][col]==yo. cuadrados[1][col]== yo. cuadrados[2][col]!=0:
                Sise muestra:
                    color=CIRC_COLORsiyo. cuadrados[0][col]==2másCROSS_COLOR
                    iPos=(col*SQSIZE+SQSIZE//2,20)
                    fPos=(col*SQSIZE+SQSIZE//2,HEIGHT-20)
                    pygame. dibujar. línea (pantalla, color, iPos, fPos, LINE_WIDTH)
                Volvera sí mismo. cuadrados[0][col]

        # victorias horizontales
        parafilaenel rango (FILAS):
            sies propio. cuadrados[fila][0]==yo. cuadrados[fila][1]== yo. cuadrados[fila][2]!=0:
                Sise muestra:
                    color=CIRC_COLORsiyo. cuadrados[fila][0]==2másCROSS_COLOR
                    iPos=(20,row*SQSIZE+SQSIZE//2)
                    fPos=(WIDTH-20,row*SQSIZE+SQSIZE//2)
                    pygame. dibujar. línea (pantalla, color, iPos, fPos, LINE_WIDTH)
                Volvera sí mismo. cuadrados[fila][0]

        # desc diagonal
        sies propio. cuadrados[0][0]==yo. cuadrados[1] [1] == yo. cuadrados[2][2]!=0:
            Sise muestra:
                color=CIRC_COLORsiyo. cuadrados[1] [1] == 2másCROSS_COLOR
                iPos=(20,20)
                fPos=(WIDTH-20,HEIGHT-20)
                pygame. dibujar. línea (pantalla, color, iPos, fPos, CROSS_WIDTH)
            Volvera sí mismo. cuadrados[1][1]

        # asc diagonal
        sies propio. cuadrados[2][0]==yo. cuadrados[1] [1] == yo. cuadrados[0][2]!=0:
            Sise muestra:
                color=CIRC_COLORsiyo. cuadrados[1] [1] == 2másCROSS_COLOR
                iPos=(20,ALTURA-20)
                fPos=(ANCHO-20,20)
                pygame. dibujar. línea (pantalla, color, iPos, fPos, CROSS_WIDTH)
            Volvera sí mismo. cuadrados[1][1]

        # Aún no hay victoria
        volver0

    defmark_sqr(self,row,col,player):
        yo mismo. cuadrados[fila][col]=jugador
        yo mismo. marked_sqrs+=1

    defempty_sqr(self,row,col):
        Volvera sí mismo. cuadrados[fila][col]==0

    def get_empty_sqrs(self):
        empty_sqrs = []
        parafilaenel rango (FILAS):
            paracolinrange(COLS):
                sies propio. empty_sqr(fila,col):
                    empty_sqrs. append( (fila,col) )
        
        volverempty_sqrs

    def isfull(self):
        Volvera sí mismo. marked_sqrs==9

    def isempty(self):
        Volvera sí mismo. marked_sqrs==0

claseAI:

    def__init__(self,level=1,player=2):
        yo mismo. nivel=nivel
        yo mismo. player=jugador

    # --- --- ALEATORIO

    defrnd(self,board):
        empty_sqrs=tablero. get_empty_sqrs()
        idx=aleatorio. Randrange(0,len(empty_sqrs))

        returnempty_sqrs[idx]# (fila, col)

    # --- MINIMAX ---

    defminimax (propio, tablero, maximización):
        
        # Estuche terminal
        case=tablero. final_state()

        # jugador 1 victorias
        ifcase==1:
            return 1,None# eval, move

        # jugador 2 victorias
        ifcase==2:
            retorno-1,Ninguno

        # sorteo
        Junta ELIF. isfull():
            return0,Ninguno

        Simaximiza:
            max_eval = -100
            best_move=Ninguna
            empty_sqrs=tablero. get_empty_sqrs()

            for(row,col)inempty_sqrs:
                temp_board=copy. deepcopy(tablero)
                temp_board. mark_sqr(fila,col,1)
                eval=self. minimax(temp_board,False)[0]
                Sieval>max_eval:
                    max_eval = eval
                    best_move=(fila,col)

            Volvermax_eval,best_move

        Elifnomaximizando:
            min_eval = 100
            best_move=Ninguna
            empty_sqrs=tablero. get_empty_sqrs()

            for(row,col)inempty_sqrs:
                temp_board=copy. deepcopy(tablero)
                temp_board. mark_sqr(fila,col,self. jugador)
                eval=self. minimax(temp_board,True)[0]
                Sieval<min_eval:
                    min_eval = eval
                    best_move=(fila,col)

            Volvermin_eval,best_move

    # --- EVALUACIÓN PRINCIPAL ---

    defeval(self,main_board):
        sies propio. nivel==0:
            # elección aleatoria
            eval='random'
            mover=self. rnd(main_board)
        De lo contrario:
            # Elección de Algoalgo Minimax
            eval,move=self. minimax(main_board,Falso)

        print(f'AI ha elegido marcar el cuadrado en pos{move}con una evaluación de:{eval}')

        returnmove# fila, col

Juego de clase:

    def __init__(self):
        yo mismo. tablero=Tablero()
        yo mismo. ai=IA()
        yo mismo. jugador = 1 # 1 cruz # 2 círculos
        yo mismo. gamemode='ai'# pvp o ai
        yo mismo. running=True
        yo mismo. show_lines()

    # --- MÉTODOS DRAW ---

    def show_lines(self):
        # bg
        pantalla. relleno(BG_COLOR )

        # vertical
        pygame. dibujar. line(screen,LINE_COLOR, (SQSIZE,0), (SQSIZE,HEIGHT),LINE_WIDTH)
        pygame. dibujar. line(screen,LINE_COLOR, (WIDTH-SQSIZE,0), (WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)

        # horizontal
        pygame. dibujar. line(screen,LINE_COLOR, (0,SQSIZE), (WIDTH,SQSIZE),LINE_WIDTH)
        pygame. dibujar. line(screen,LINE_COLOR, (0,HEIGHT-SQSIZE), (WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)

    defdraw_fig(self,row,col):
        sies propio. jugador==1:
            # Dibujar cruz
            # Línea Desc
            start_desc=(col*SQSIZE+OFFSET,row*SQSIZE+OFFSET)
            end_desc=(col*SQSIZE+SQSIZE-OFFSET,row*SQSIZE+SQSIZE-OFFSET)
            pygame. dibujar. línea(pantalla,CROSS_COLOR,start_desc,end_desc,CROSS_WIDTH)
            # Línea ASC
            start_asc=(col*SQSIZE+OFFSET,row*SQSIZE+SQSIZE-OFFSET)
            end_asc=(col*SQSIZE+SQSIZE-OFFSET,row*SQSIZE+OFFSET)
            pygame. dibujar. línea(pantalla,CROSS_COLOR,start_asc,end_asc,CROSS_WIDTH)
        
        Elifyo. jugador==2:
            # Dibujar círculo
            center=(col*SQSIZE+SQSIZE//2,row*SQSIZE+SQSIZE//2)
            pygame. dibujar. círculo(pantalla,CIRC_COLOR,centro,RADIO,CIRC_WIDTH)

    # --- OTROS MÉTODOS ---

    defmake_move(self,row,col):
        yo mismo. Junta. mark_sqr(fila,col,self. jugador)
        yo mismo. draw_fig(fila,col)
        yo mismo. next_turn()

    def next_turn(self):
        yo mismo. jugador = yo. jugador%2+1

    def change_gamemode(self):
        yo mismo. gamemode='ai'if self. gamemode=='pvp'else'pvp'

    defisover (self):
        Volvera sí mismo. Junta. final_state(show=True)!=0oself. Junta. isfull()

    def reset(self):
        yo mismo. __Init__()

def main():

    # --- OBJETOS ---

    juego=Juego()
    tablero=juego. tabla
    ai=juego. .ai

    # --- MAINLOOP ---

    mientras queVerdadero:
        
        # Eventos de pygame
        paraeventoenpygame. evento. get():

            # Evento Quit
            sievento. tipo==pygame. DEJAR DE FUMAR:
                pygame. renunciar()
                sys. salida()

            # Evento keydown
            sievento. tipo==pygame. KEYDOWN:

                # G-gamemode
                sievento. Clave==pygame. K_g:
                    juego. change_gamemode()

                # r-reinicio
                sievento. Clave==pygame. K_r:
                    juego. restablecimiento()
                    tablero=juego. tabla
                    ai=juego. .ai

                # 0-IA aleatoria
                sievento. Clave==pygame. K_0:
                    ai. nivel=0
                
                # 1-IA aleatoria
                sievento. Clave==pygame. K_1:
                    ai. nivel=1

            # clic en evento
            sievento. tipo==pygame. MOUSEBUTTONDOWN:
                pos=evento. Pos
                row=pos[1]//SQSIZE
                col=pos[0]//SQSIZE
                
                # Marca humana SQR
                sila junta. empty_sqr(fila,col) yjuego. Ejecución:
                    juego. make_move(fila,col)

                    sijuego. isover():
                        juego. running=False


        # Llamada inicial de IA
        sijuego. gamemode=='ai' yjuego. jugador==AI. jugadoryjuego. Ejecución:

            # Actualizar la pantalla
            pygame. pantalla. actualizar()

            # eval
            fila,col=ai. eval(tablero)
            juego. make_move(fila,col)

            sijuego. isover():
                juego. running=False
            
        pygame. pantalla. actualizar()

principal()