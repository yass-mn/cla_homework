def palindrome(word):
    n=-0
    i=2  
    while(i<(len(word)//2)):
        if(word[i]!=word[n]) : return False
        else :
           n=n-1
           i=i+1
    return True
        
def prime(n):
    if n<=1: return False
    else:
        for i in range(2,n):
            if(n%i)==0: return False
        return True
        
def range1(n,a,b):
    return n in range(a,b+1)

def Factional_num(n):
  if n==0: return 1
  else: 
      return n*Fact(n-1)


def reverse_string (string):
    c=''
    n=-1
    for i in range(len(string)):
        c=c+string[n]
        n=n-1
    return c
     
def sum(List):
    S=0
    for i in List:
       S=S+i
    return S

def max_numbers (a,b,c):
    if (a>b>c or (a>b & b<c)): 
        return a
  elif (a<b<c or (a>b & b<c)) : 
      return c
  else : 
      return b
    