class Pupa:
  def __init__(self):
    self.counter = 0
  def do_work(self, spisok1, spisok2):
    spisok =[]
    for i in range(len(spisok1)):
      spisok.append(spisok1[i] + spisok2[i])
      self.counter +=1
    print("Результат работы Пупы:", spisok)

  def take_salary(self):
    print("Зарплата Пупы:", self.counter * 10)

class Lupa:
  def __init__(self):
    self.counter = 0
  def do_work(self, spisok1, spisok2):
    spisok = []
    for i in range(len(spisok1)):
      spisok.append(spisok1[i] - spisok2[i])
      self.counter +=1
    print("Результат работы Лупы", spisok)

  def take_salary(self):
    print("Зарплата Лупы:", self.counter * 10)

class Accountant:
  def give_salary(self, worker):
    return worker.take_salary()

worker1 = Pupa()
worker2 = Lupa()
accountant = Accountant()
spisok1 = [5*i for i in range(5)]
spisok2 = [i for i in range(5)]
print(spisok1)
worker1.do_work(spisok1, spisok2)
worker2.do_work(spisok1, spisok2)
accountant.give_salary(worker1)
accountant.give_salary(worker2)