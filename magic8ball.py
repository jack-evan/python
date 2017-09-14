from random import randrange

answers = ['It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good',
'Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Do not count on it','My reply is no',
'My sources say no','Outlook not so good','Very doubtful']

question = raw_input('What would you like to know ')


random_index = randrange(0,len(answers))
print question + ': ' + answers[random_index]


