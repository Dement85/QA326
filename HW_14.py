 from turtle import *
def draw_square(a):# a -локальная
     for i in range(3):
        forward(a)
        left(90)

for a in range(200, 100, -20):
    draw_square(a)# a -локальная

exitonclick()


def generate_date():
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(1000, 9999)
    sep = random.choice(['.', '/'])
    return f"{day}{sep}{month}{sep}{year}"

print(generate_date())