import datetime
import math
import random


#help()
# keywords 
'''
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''



# help >> symbols 
#!=                  +                   <=                  __
#"                   +=                  <>                  `
#"""                 ,                   ==                  b"
#%                   -                   >                   b'
#%=                  -=                  >=                  f"
#&                   .                   >>                  f'
#&=                  ...                 >>=                 j
#'                   /                   @                   r"
#'''                 //                  J                   r'
#(                   //=                 [                   u"
#)                   /=                  \                   u'
#*                   :                   ]                   |
#**                  <                   ^                   |=
#**=                 <<                  ^=                  ~
#*=                  <<=                 _

# help() >> topics 
'''
ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING
CONVERSIONS         LISTS               SEQUENCEMETHODS
DEBUGGING           LITERALS            SEQUENCES
'''

def greeting(name):
    print(f"sen ,{name}")
greeting("fikret")
print("----------------------------")
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print("----------------------------")
store_items=['ankara',6,'istanbul',34,'antalya',7,'mersin',33,'diyarbakır',21]
print(store_items[1:10]) # [1]indexden [10]. index e kadar yazdırır 10. index hariç
print(store_items[2:4]) # [0]indexden [4]. index e kadar yazar 4.index hariç
print("----------------------------")
liste = ['python',100,'java',200,'c++',60,'proglamlama',5,'devOps',90,'tensorFlow',150]

print(liste[0:])
print(liste[:4])
print("----------------------------")
fikret_erduran=["topoğraf","veri bilimi","yapay zeka","makine ogrenmesi","AI"]
print(fikret_erduran[0:5])

fikret_erduran[0]="Harita uzmanı"
print(fikret_erduran[0:5])
fikret_erduran[2]="deep learning siencee"
print(fikret_erduran[0:4])
print(type(fikret_erduran))
print("----------------------------")
k=10%5
print(k)
print("----------------------------")
print("Ben bu yapay zeka alanında en iyisi olmak için python ogreniyorum",
      "i am this AI in areas for best be, i am learnin python")

'''
name =input("name : ")
print("merhaba",name)

number =int(input("number: "))
print(number + 5)

number2=float(input("number: "))
print(number2+17.5)
'''
print("----------------------------")
tarihVeSaat= datetime.datetime.now()
print(tarihVeSaat)
print("----------------------------")


sayılar= math.floor(3.25)
print(sayılar)
print("----------------------------")
sas=random.randint(1,100)
print(sas)
print("----------------------------")
print("5+6   ",5+6)
print('9-5   ',9-5)
print("12/4  ",12/4)
print("18*4  ",18*4)
print("9**2  ",9**2)
print("9//2  ",9//2)
print("15%4  ",15%4)

print("----------------------------")
a=10
b=25

print(a,">", b,"=", a>b)
print(a,"<", b,"=", a<b)
print(a,"<=",b,"=", a<=b)
print(a,">=",b,"=", a>=b)
print(a,"==",b,"=", a==b)
print(a,"!=",b,"=", a!=b)
print(a,"==",b,"=", a==b)

# ======and or not operatorleri =====
print("----------------------------")
# and  operatoru
print("True and True and False ","= ",True and True and False)
print("False and True"," = ",False and True)
print("True and False","= ",True and False)
print("False and False","= ",False and False)
print("True and True","= ",True and True)
print("----------------------------")
# or  operatoru
print("True or True","=",True or True)
print("True or False","=",True or False)
print('False or True','=',False or False)
print("False or False",'=',False or False)
print("True or True",'=',True or True)
print("----------------------------")
# not operatoru
print("not true",'=',not True)
print("not false","=",not False)

print("----------------------------")

f1=5
f2=2
f3=f1+f2

ist=f3
tekise=False
ciftise= True

print(f1,'+',f2,'=',f1+f2,"=",True or False)
print(f1,'-',f2,'=',f1-f2,'=',True and False)
print(f1,'**',f2,'=',f1**f2,'=',True and False)

print("----------------------------")

# if elif else 
celsius = 35
if celsius >45:
    print('Hava aşırı sıcak lütfen önlem alın!!!')
elif celsius >30:
    print('cok sıcak💥')
elif 30>= celsius >20:
    print("Hava sıcaklıgı normal💚")
elif  20>= celsius >10:
    print("hava serin💧")
elif 5 <= celsius <10:
    print('Hava soguyor 🔊')
elif -273< celsius <5:
    print('Hava çok soguk ❄')
else:
    print("Bir sorun var")


