from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/one/', methods=['post', 'get'])
def one():
    age = "мы не знаем ваш возраст"
    if request.method == 'POST':
        age = request.form.get("age")
    return render_template("one.html", age=age)

@app.route('/two/', methods=['post', 'get'])
def two():
    mes = ""
    if request.method == "POST":
        num = request.form.get("num")
        num = int(num)
        if num > 10:
            mes = "Это больше чем 10"
        elif num < 10 and num > 0:
            mes = "Это меньше чем 10 и больше чем 0"
        elif num < 0:
            mes = "Это меньше чем 0"
        elif num == 0:
            mes = "Это 0"
        elif num == 10:
            mes = "Это 10"
    return render_template("two.html", mes=mes)

@app.route('/three/', methods=['post', 'get'])
def three():
    mes = ""
    if request.method == "POST":
        num = request.form.get("num")
        num = int(num)
        if num == 1:
            mes = "Понедельник"
        elif num == 2:
            mes = "Вторник"
        elif num == 3:
            mes = "Среда"
        elif num == 4:
            mes = "Четверг"
        elif num == 5:
            mes = "Пятница"
        elif num == 6:
            mes = "Суббота"
        elif num == 7:
            mes = "Воскресенье"
        else:
            mes = "Эй мудила с нижнего тагила ты чё вводишь!?"
    return render_template("three.html", mes=mes)

@app.route('/four/', methods=['post', 'get'])
def four():
    mes = ""
    if request.method == "POST":
        num = request.form.get("num")
        num = int(num)
        for i in range(1, num + 1):
            if i % 2 == 0:
                mes = mes + " {} ".format(i)
                print(i)
    return render_template("four.html", mes=mes)

@app.route('/five/', methods=['post', 'get'])
def five():
    mes_one = ""
    mes_two = ""
    mes_three = ""
    one = 0
    two = 0
    three = 0
    if request.method == "POST":
        num = request.form.get("num")
        num = str(num)
        for i in num:
            if i == "1":
                one += 1
            elif i == "2":
                two += 1
            elif i == "3":
                three += 1
        mes_one = "Единицы - {}".format(one)
        mes_two = "Двойки - {}".format(two)
        mes_three = "Тройки - {}".format(three)
    return render_template("five.html", mes_one=mes_one, mes_two=mes_two, mes_three=mes_three)


if __name__ == '__main__':
    app.run()
