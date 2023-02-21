Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import maths
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
number=int(input("enter the number:"))
enter the number:5
print("The multiplication Table of:",number)
The multiplication Table of: 5
for count in range(1,11):
    print(number,'x',count,'=',number*count)

    
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
cls
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
clr
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    clr
NameError: name 'clr' is not defined. Did you mean: 'chr'?
from math import sqrt
n=9
flag=0
if(n>1):
    for k in range(2,int(sqrt(n))+1):
        if(n%k==0):
            flag=1
            break
        if(flag==0):
            print(n,"is a prime number.")
            else:
                
SyntaxError: invalid syntax
num=11
if(num>1):
    for i in range(2,int(num/2)+1):
        if(num%i)==0
        
SyntaxError: incomplete input
num=29
flag=False
if num==1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
        if flag:
            print(num,"is not a prime number")
            else:
                
SyntaxError: invalid syntax
def PrimeChecker(a): 
SyntaxError: invalid non-printable character U+00A0
if a > 1:
    
SyntaxError: invalid non-printable character U+00A0
num = 15
flag = 0
if num<2:
   flag = 1
   else:
       
SyntaxError: invalid syntax
num = 15
flag = 0
if num<2:
    flag = 1
    elif:
        
SyntaxError: invalid syntax
E={0,2,4,6,8}
N={1,2,3,4,5}
print("Union of t and n is",E|N)
Union of t and n is {0, 1, 2, 3, 4, 5, 6, 8}
#SET intersection
print("Intersection of E and N",E&N)
Intersection of E and N {2, 4}
#SET differnce
print("Difference of E and N is",E-N)
Difference of E and N is {0, 8, 6}
#SET symmetric Difference
print("symmetric difference of E&N",E^N)
symmetric difference of E&N {0, 1, 3, 5, 6, 8}
FROM
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    FROM
NameError: name 'FROM' is not defined
from chatterbot import chatbot
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    from chatterbot import chatbot
ModuleNotFoundError: No module named 'chatterbot'
from chatterboat import chatbot
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    from chatterboat import chatbot
ModuleNotFoundError: No module named 'chatterboat'
import re
import chatterbot from chatbot
SyntaxError: invalid syntax
graph={}
graph={}






graph
{}
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
visited=[]
queue=[]
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="")
        for neighbour in graph[m]:
            visited.append(neighbour)
            queue.append(neighbour)
            print("Following is the BFS")
...             bfs(visited,graph,'5')
... 
...             
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def bfs(visited, graph, node):
...     visited.append(node)
...     queue.append(node)
...     while queue:
...         m=queue.pop(0)
...         print(m,end="")
...         for neighbour in graph[m]:
...             visited.append(neighbour)
...             queue.append(neighbour)
...             
...             print("Following is the BFS")
...             bfs(visited,graph,'5')
... 
...             
>>> 
>>> 5456
5456
>>> 632211
632211
>>> 33333
33333
>>> def bfs(visited, graph, node):
...     visited.append(node)
...     queue.append(node)
...     while queue:
...         m=queue.pop(0)
...         print(m,end="")
...         for neighbour in graph[m]:
...             visited.append(neighbour)
...             queue.append(neighbour)
... 
...             print("Following is the BFS")
...             bfs(visited,graph,'5')
>>> [DEBUG ON]
>>> [DEBUG OFF]
