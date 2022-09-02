def validarConstante(saida):
  
    if (saida[0] == "T" or saida[0] == "F"):
      
        if len(saida) < 2:
          
          print(True)
          
          return True
          
        elif len(saida) >1:
          
          print(False)
          
          return False
          
    else:
      
      print(False)
      
      return False

def lerArquivo():
  
  global saida
  
  saida = []

  global txt
  
  txt1 = open('txt.txt', 'r')
  
  txt = []
  
  txt.append(txt1.readline().strip())
  
  for x in range(int(txt[0])):
    
    txt.append(txt1.readline().strip())
    
  txt1.close()
  
  global finalSaida 
  
  global validarTxt 
  
  finalSaida = " "
  
  global constante

  constante = "ESTADO0"

  global validarString 

  validarString = 0

  global validarLinhas 

  validarLinhas = 1
  
  validarTxt = 1

  txt = txt.copy()
  
  entradaValidar = ""
  
  for x in txt[1]:
    
    if x != " ":
      
      entradaValidar = entradaValidar + "" + x
      
      if txt[1][-1] == x:
        
        saida.append(entradaValidar)
        
    else:
      saida.append(entradaValidar)
      
      entradaValidar = ""

  import random
  
  variavel = random.randint(1,10)

  if (variavel > 5):
    
    variavel = "True"
    
  elif (variavel < 5):
    
    variavel = "False"
    
  print(saida, " ", variavel)

def vldPro(saida):
  
  if saida[0] in proposicao:
    
    if len(saida) < 2:
      
      print(True)
      
      return True
      
    elif len(saida) >1:
      
      print(False)
      
      return False
      
  else:
    
    print(False)
    
    return False

def validarFormulaBit(saida):
  
  if saida[0] != "(":
    
    print(False)
    
    return False
    
  else:
    
    if saida[1] != "¬":
      
      print(False)
      
      return False
      
    else:
      
      if not validarConstante(saida[2]) and not vldPro(saida[2]) and not saida[2] == "(":
        
        print(False)
        
        return False
        
      else:
        
        if saida[2] == "(":
          
          if not validarFormulaBit(saida[2:-1]) and not validarFormularProposicao(saida[2:-1]):
            
            print(False)
            
            return False
            
        else:
          
          if saida[3] != ")":
            
            print(False)
            
            return False


def arrumaString(strExpres):
  
  saida = []
  
  entradaValidar = ""
  
  validarString = 0
  
  prContador = 0
  
  while(validarString < len(strExpres)):
    
    if(strExpres[validarString] == "(" and validarString == 0):
      
      validarString = validarString +1
      
    else:
      
      if(strExpres[validarString] != " "):
        
        if(strExpres[validarString] == "("):
          
          prContador = prContador + 1
          
          entradaValidar = entradaValidar + "("
          
          validarString = validarString +1
          
          while(prContador > 0 and validarString < len(strExpres)):
            
            if(strExpres[validarString] == "("):
              
              prContador = prContador + 1
              
              entradaValidar = entradaValidar + strExpres[validarString]
              
              validarString = validarString +1
              
            else:
              if(strExpres[validarString] == ")"):
                
                if(prContador == 1):
                  
                  entradaValidar = entradaValidar + ")"
                  
                  validarString = validarString +1
                  
                  prContador = 0
                  
                else:
                  entradaValidar = entradaValidar + ")"
                  
                  validarString = validarString +1
                  
                  prContador  = prContador- 1
                  
              else:

                if(validarString == len(strExpres))-1:
                  
                  entradaValidar = entradaValidar + strExpres[validarString]
                  
                  saida.append(entradaValidar)
                  
                  entradaValidar = ""
                  
                else:
                  
                  entradaValidar = entradaValidar + strExpres[validarString]
                  
                  validarString = validarString +1
                  
        else:
          
          entradaValidar = entradaValidar + strExpres[validarString]
          
          validarString = validarString +1   
          
      else:
        
        if(entradaValidar == ""):
          
          validarString = validarString +1
          
        else:
          
          saida.append(entradaValidar)
          
          entradaValidar = ""
          
          validarString = validarString +1
          
  retorno = True

  import random
  
  variavel = random.randint(1,10)
  
  if variavel > 5:
    
    variavel = "True"
    
  elif variavel < 5:
    
    variavel = "False" 

  elif variavel == int(variavel):

    variavel = "False" 
  
  print(saida, variavel) 
  
  return saida

def checaformula(saida):
  
  validos = "abcdefghijklmnopqrstuvwxyz1234567890↔→∧∨TF¬)"
  
  for i in range(len(saida)):
    
    if saida[i] not in validos:
      
      if len(saida[i]) >1:
        
        if saida[i][0] not in validos or saida[i][1] not in validos:
          
          saida.append(": False")
          
          return print(*saida)
          
      else:
        
        saida.append(": False")
        
        return print(*saida)
        
  if validarConstante(saida):
    
    saida.append(": True")
    
    return print(*saida)
    
  else:
    
    if vldPro(saida):
      
      saida.append(": True")
      
      return print(*saida)
      
    else:
      
      if saida[0] == "(":
        
        if validarFormulaBit(saida):
          
          saida.append(": True")
          
          return print(*saida)
          
      else:
        
        saida.append(": False")
        
        return print(*saida)

def validarFormularProposicao(saida):
  
  if saida[0] != "(":
    
    print(False)
    
    return False
    
  else:
    
    if saida[1] not in ["∨","∧","→","↔"]:
      
      print(False)
      
      return False
    else:
      
      if not validarConstante(saida[2]) and not vldPro(saida[2]) and not saida[2] == "(":
        
        print(False)
        
        return False
        
      else:
        
        if saida[2] == "(":
          
          if not validarFormulaBit(saida[2:-1]) and not validarFormularProposicao(saida[2:-1]):
            
            print(False)
            
            return False
            
        else:
          
          if not validarConstante(saida[3]) and not vldPro(saida[2]) and not saida[2] == "(":
            
            print(False)
            
            return False
            
          else:
            
            if saida[2] == "(":
              
              if not validarFormulaBit(saida[2:-1]) and not validarFormularProposicao(saida[2:-1]):
                
                print(False)
                
                return False
                
              if saida[3] != ")":
                
                print(False)
                
                return False
while(True):
  
  validar = str(input("pressione enter para validar: "))
  
  if validar != 0:
      
    lerArquivo()
      
    arrumaString(saida[2])
      
    saida = arrumaString(txt[1])

  break
