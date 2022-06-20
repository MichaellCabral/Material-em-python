from tkinter import * #A linha 1 mostra a importação de todos os elementos disponíveis em tkinter. O objeto janelaPrincipal é do tipo Tk. Um objeto Tk é um elemento que representa a janela GUI. Para que essa janela apareça, é necessário chamar o método mainloop();

def funcClicar():#Para o funcionamento correto do botão, precisamos definir a função funcClicar(), nas linhas 3 e 4. Essa função serve apenas para imprimir na tela a string “Botão pressionado”.
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")  #linhas 4 e 5, com a criação do elemento e o seu posicionamento. O tamanho padrão da janela é 200 X 200 pixels, com o canto superior esquerdo de coordenadas (0,0) e o canto inferior direito de coordenadas (200,200).
texto.pack()

pic = PhotoImage(file="logoEstacio.gif")#Vamos agora incrementar um pouco essa janela. Para isso, vamos acrescentar uma imagem e um botão. A imagem precisa estar na mesma pasta do seu arquivo .py.
#Nas linhas 10, 11 e 12, é feita a criação do objeto Label para conter a imagem e seu posicionamento. Observe que passamos a utilizar o método pack(), que coloca o elemento centralizado e posicionado o mais perto possível do topo, depois dos elementos posicionados anteriormente.
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
#O elemento botão é criado na linha 14, com os atributos text e command, que, respectivamente, são o texto exibido no corpo do botão e a função a ser executada quando o botão for clicado.
botao.pack()

janelaPrincipal.mainloop()

#O pacote tkinter é a interface Python padrão para o Tk GUI (interface gráfica com o usuário) toolkit. Na maioria dos casos, basta importar o próprio tkinter, mas diversos outros módulos estão disponíveis no pacote. A biblioteca tkinter permite a criação de janelas com elementos gráficos, como entrada de dados e botões, por exemplo.

