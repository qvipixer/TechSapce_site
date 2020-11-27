import calendar
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
#with open('calendar.html', 'w') as g:
#    print(a.formatyear(2020, width=3), file=g)
print(a.formatyear(2020, width=3))