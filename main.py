import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
website = 'https://dvmn.org/profession-ref-program/alexkipr/X6TXA/'
friend_name = 'Александр'
my_name = 'Алексей'
email = 'alextestki@yandex.ru'

letter = '''From: {email}
To: {email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";\n\nПривет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(email=email, friend_name=friend_name, my_name=my_name, website=website)
letter = letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(login, login, letter)
server.quit()