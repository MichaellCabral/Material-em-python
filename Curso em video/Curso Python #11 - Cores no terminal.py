print('\033[0;30;47m cinza / fundo branco \033[m') 
print('\033[1;31;46m vermelho / fundo azul claro\033[m')
print('\033[4;32;45m ciano / fundo lilás \033[m')
print('\033[0;33;44m amarelo / fundo azul escuro \033[m')
print('\033[1;34;43m azul escuro / fundo amarelo \033[m')
print('\033[1;35;42m lilás / fundo ciano \033[m')
print('\033[4;36;41m azul claro / fundo vermelho \033[m')
print('\033[0;37;40m branco / fundo preto \033[m')

print('\033[7;30m cor invertida') 


# _____;____;__________
# style;text;background

# 0 NONE
# 1 BOLD
# 4 UNDERLINE
# 7 NEGATIVE

# COR DE TEXTO       DE 30 A 37
# COR DE BACKGROUND  DE 40 A 47

# Curso Python #11 - Cores no Terminal

# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.