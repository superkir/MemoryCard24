questions = []
class Question():
    def __init__(self, text, true, false1, false2, false3):
        self.text = text
        self.true = true
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
        questions.append(self)
    
    def show_question(self, lb, rb1, rb2, rb3, rb4):
        lb.setText(self.text)
        rb1.setText(self.true)
        rb2.setText(self.false1)
        rb3.setText(self.false2)
        rb4.setText(self.false3)

Question("В якому році почала перша світова війна?", "1914", "1896", "1918", "1941")
Question("Який футболіст виграв три Чемпіонати Світу?", "Пеле", "Марадона", "Мессі", "Роналду")
Question("Коли помер Майкл Джексон?", "2009", "2010", "1999", "2012")
Question("В якому році засновано пайтон?", "1991", "1999", "1993", "1997")
Question("В якому році був заснован Windows?", "1985", "1895", "1975", "1986")
Question("В якому році заснували Microsoft?", "1975", "1985", "1979", "1971")
Question("В якому році Мессі отримав перший золотий м'яч?", "2010", "2015", "2011", "2023")
Question("В якому році народився Тарас Шевченко?", "1814", "1824", "1817", "1914")
Question("В якому році почалася друга Світова війна?", "1939", "1945", "1932", "1940")
Question("В якому році народився Мессі?", "1987", "1999", "1989", "1887")
Question("В якому році народилася Леся Українка?", "1871", "1971", "1875", "1877")
Question("В якому році народився Роналду?", "1985", "1982", "1989", "1885")
Question("В якому роцці Роналду виграв свій перший золотий м'яч?", "2013", "2015", "2011", "2017")
Question("Коли народився Іван Франко?", "1856", "1756", "1956", "1877")
Question("Коли було випущено VSC?", "2015", "2017", "2013", "1915")
