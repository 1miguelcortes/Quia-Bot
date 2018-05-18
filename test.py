from quiabot import *

d1 = answers('https://www.quia.com/quiz/4731482.html','miguelcortes834','red54')
d2 = fillinanswers('https://www.quia.com/quiz/4731482.html','miguelcortes834','red54',d1)

d1.close()
d2.close()