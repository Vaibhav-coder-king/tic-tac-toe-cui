import pyfiglet as p
import random as r 
from itertools import permutations as pr

def default_game(a,b,c,d,e,f,i,j,k):
	print(f'	{a}|{b}|{c}\n	_ _ _\n	{d}|{e}|{f}\n	_ _ _\n	{i}|{j}|{k}')
	print()
	
def xturn():
	print("It's X Turn:-")
	return'X'

def oturn():
	print("It's O Turn:-")
	return'O'

def ch_(n):
	try:
		ch=int(input(f'{n} enter your choice b/w 1 to 9='))
		return ch
	except:
		print("plz,enter value b/w 1 to 9.")
		
		
def display(n,ch):
	global a,b,c,d,e,f,i,j,k
	if ch==1:
		a=n
	elif ch==2:
		b=n
	elif ch==3:
		c=n
	elif ch==4:
		d=n
	elif ch==5:
		e=n
	elif ch==6:
		f=n
	elif ch==7:
		i=n
	elif ch==8:
		j=n	
	elif ch==9:
		k=n
		
def vchk(data):
	result=[list(p) for p in pr(data, 3)]
	for l in result:
		if l in win:
			return True
		else:
			continue 
	return False
		
win=[[1,2,3],[1,5,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]

def onep_game():
	s=[l for l in range(1,10)]
	x=[]
	o=[]
	global a,b,c,d,e,f,i,j,k
	default_game(a,b,c,d,e,f,i,j,k)
	t=1
	while True:
		if vchk(x):
			default_game(a,b,c,d,e,f,i,j,k)
			print(p.figlet_format("!!!!!\nX wins! ",font="small"))
			break 
		if vchk(o):
			default_game(a,b,c,d,e,f,i,j,k)
			print(p.figlet_format("!!!!!\nO wins! ",font="small"))
			break 
		if s==[]:
			default_game(a,b,c,d,e,f,i,j,k)
			print(p.figlet_format("It's a tie",font="small"))
			break
		else:
			pass
		if t%2!=0:
			print("It's Your Turn:-")
			n='X'
		else:
			n='O'
		t+=1
		if n=='X':
			ch=ch_(n)
		elif n=='O':
			ch=r.randint(1,10)
		if ch==None:
			t-=1
			continue
		if ch in s:
			display(n,ch)
			if n=='X':
				x.append(ch)
				s.remove(ch)
			elif n=='O':
				o.append(ch)
				s.remove(ch)
				default_game(a,b,c,d,e,f,i,j,k)
			x.sort()
			o.sort()
		elif n=='X' and ch in range(1,10):
			print('Place is already occupied.')
			t-=1
		elif n=="O" and ch in range(1,10):
			t-=1
		else:
			print("plz,enter value b/w 1 to 9.")
			t-=1
def twop_game():
	s=[l for l in range(1,10)]
	x=[]
	o=[]
	global a,b,c,d,e,f,i,j,k
	default_game(a,b,c,d,e,f,i,j,k)
	t=1
	while True:
		if s==[]:
			print(p.figlet_format("It's a tie",font="small"))
			break
		else:
			pass
		if vchk(x):
			default_game(a,b,c,d,e,f,i,j,k)
			print(p.figlet_format("!!!!!\nX wins!",font="small"))
			break 
		if vchk(o):
			default_game(a,b,c,d,e,f,i,j,k)
			print(p.figlet_format("!!!!!\nO wins!",font="small"))
			break 
		if t%2!=0:
			n=xturn()
		else:
			n=oturn()
		t+=1
		ch=ch_(n)
		if ch==None:
			t-=1
			continue
		if ch in s:
			display(n,ch)
			default_game(a,b,c,d,e,f,i,j,k)
			if n=='X':
				x.append(ch)
				s.remove(ch)
			elif n=='O':
				o.append(ch)
				s.remove(ch)
			x.sort()
			o.sort()
		elif ch in range(1,10):
			print('Place is already occupied.')
			t-=1
		else:
			print("plz,enter value b/w 1 to 9.")
			t-=1
ask_=True		
while ask_:
	a,b,c,d,e,f,i,j,k=" "," "," "," "," "," "," "," "," "
	print(p.figlet_format("Tic Tac Toe",font='slant'))
	ask=input("Wanna play against bot?🤔(y or n)=").lower ()
	if ask=="y":
		onep_game()
	elif ask=="n":
		twop_game()
	else:
		print("plz,input y or n")
		continue
	ans_=True
	while ans_:
		ans=input("wanna play again?🤔(y or n)").lower()
		if ans=='y':
			break
		elif ans=='n':
			print(p.figlet_format("bye-bye",font='small'))
			ans_=False
			ask_=False
		else:
			print("plz,input y or n")
			continue
