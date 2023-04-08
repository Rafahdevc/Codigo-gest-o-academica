#RAFAEL ROBERTO CHINISKI   ------ CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMA
from collections import namedtuple

menu = 1
lista_estudante = []
codigo_estudante = int(0)

while menu != 0:
    print("\n\n####### MENU INICIAL #######\n\n")
    print("(1) Estudante")
    print("(2) Diciplina")
    print("(3) Professor")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(0) Sair")
    menu = int(input("Informe a opção desejada: "))
    if menu == 0:
      print("Codigo finalizado")
      break
  
  #opções de menus
    estudante = 1
    disciplina = 2
    professor = 3
    turmas = 4
    matriculas = 5
    
    
    if menu == 1:
      while estudante != 0:
          print("\n\n------- ESTUDANTE -------\n\n")
          print("(1) Incluir")
          print("(2) Listar")
          print("(3) Atualizar")
          print("(4) Excluir")
          print("(0) Voltar ao menu principal")
          estudante = int(input("Selecione a ação que deseja: "))
        
          if estudante == 1: 
            
            codigo_estudante += 1
            novo_estudante = input("Digite o nome do estudante: ")
            cpf_estudante = input("Digite o CPF do estudante: ")
            cadastro_estudante = {"Codigo": codigo_estudante, "Nome:": novo_estudante, "CPF:" : cpf_estudante}
            lista_estudante.append(cadastro_estudante)
            
          elif estudante == 2:
            if len(lista_estudante) == 0:
              print("\nNão há estudantes cadastrados\n")
            else:
              print("\nLista de estudantes\n")
              for i in range(len(lista_estudante)):
                print(lista_estudante[i])
          
          elif estudante == 3:
            print("\nEm desenvolvimento\n")
          elif estudante == 4:
            romover_estudante = input("Escreva o codigo que deseja remover: ")
            lista_estudante.remove(romover_estudante)
          else:
            print("\n-------Esta opção não existe-------\n")

    elif menu == 2:
      while disciplina != 0:
          print("\n\n------- DISCIPLINA -------\n\n")
          print("\nEm desenvolvimento\n")
          break
          print("(1) Incluir")
          print("(2) Listar")
          print("(3) Atualizar")
          print("(4) Excluir")
          print("(0) Voltar ao menu principal")
          disciplina = int(input("Selecione a ação que deseja: "))
          
    elif menu == 3:
      while professor != 0:
        print("\n\n------- PROFESSOR -------\n\n")
        print("\nEm desenvolvimento\n")
        break
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(0) Voltar ao menu principal")
        professor = int(input("Selecione a ação que deseja: "))
        
    elif menu == 4:
      while turmas !=0:
        print("\n\n------- TURMAS -------\n\n")
        print("\nEm desenvolvimento\n")
        break
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(0) Voltar ao menu principal")
        turmas = int(input("Selecione a ação que deseja: "))
        
    elif menu == 5:
      while matriculas !=0:
        print("\n\n------- MATRÍCULAS -------\n\n")
        print("\nEm desenvolvimento\n")
        break
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(0) Voltar ao menu principal")
        matriculas = int(input("Selecione a ação que deseja: "))
    else:
      print("\n-------Esta opção não existe-------\n")