
# A very simple Flask Hello World app for you to get started with...
# @author: Ismagilov A.Z. @amirismagilov
from flask import Flask
from flask import render_template
from datetime import datetime
import sqlite3
import sqlite3 as sql
import random

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    con = sql.connect("/home/maitam/mysite/database.db")
    cur = con.cursor()
    #cur.execute("select username from users")
    cur.execute("select * from structs")

    structs = cur.fetchall()

    con.close()

    randomnews = ['@amirismagilov','#maitam','#amirismagilov','#twitter','#vk','#news','Скотланд-Ярд сообщил, что пострадавших в Эймсбери отравили «Новичком»',
                 'Названа дата прощания с игроком команды КВН «Пирамида» Алборовым','Вице-премьер Дагестана стал фигурантом уголовного дела и лишился поста']
    random1 = random.choice(randomnews)
    return render_template('index.html', name=name,datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), randomnews=random1,structs=structs)

