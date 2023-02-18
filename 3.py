class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('salary') + self._income.get('bonus')


worker = Position('Андрей', 'Петров', '1С-программист', 65000, 15000)
print(f'{worker.get_full_name()} - {worker.position}, доход с учетом премии - {worker.get_total_income()} руб.')
