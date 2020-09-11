Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Colin')
Mijn naam is Colin
>>> naam = (Colin)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    naam = (Colin)
NameError: name 'Colin' is not defined
>>> naam = 'Colin'
>>> print naam
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(naam)?
>>> print (naam)
Colin
>>> print (naam.upper())
COLIN
>>> print (naam{[0:2])
       
SyntaxError: invalid syntax
>>> print (naam[0:2])
Co
>>> print (naam[::-1])
niloC
>>> leeftijd = 15
>>> print ('Hallo ' +naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Colin ben je al 15 jaar?
>>> leeftijd = leeftijd +1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd
15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
	else:
		
SyntaxError: invalid syntax
>>> else: print('Je bent precies ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	print("asdf")
elif leeftijd < 4:
	print("jong")

	
asdf
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
elif leeftijd > 18:
     hoelang_al18jaar = leeftijd - 18
     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
     print('Je bent precies ' + str(leeftijd) + ' jaar')

     
Traceback (most recent call last):
  File "<pyshell#39>", line 3, in <module>
    print ('Over ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
NameError: name 'hoelang_al18jaar' is not defined
>>> >>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_tot18jaar) + ' jaar geleden dat je 18 werd ;-)')
elif leeftijd > 18:
     hoelang_al18jaar = leeftijd - 18
     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
     print('Je bent precies ' + str(leeftijd) + ' jaar')
     
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_tot18jaar) + ' jaar geleden dat je 18 werd ;-)')
elif leeftijd > 18:
     hoelang_al18jaar = leeftijd - 18
     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
     print('Je bent precies ' + str(leeftijd) + ' jaar')

     
Over 3 jaar geleden dat je 18 werd ;-)
>>> from random import datetime
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    from random import datetime
ImportError: cannot import name 'datetime' from 'random' (C:\Users\colin\AppData\Local\Programs\Python\Python37\lib\random.py)
>>> from random import randit
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    from random import randit
ImportError: cannot import name 'randit' from 'random' (C:\Users\colin\AppData\Local\Programs\Python\Python37\lib\random.py)
>>> from random import randint
>>> randint(0,1000)
727
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
567
>>> print('Willekeurig getal tussen 0 en 1000: ' +str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 567
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:54:03.495714
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 