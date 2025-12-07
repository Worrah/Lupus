import urllib, random

url = 'https://www.random.org/integers/?num=0&min=0&max=10&col=1&base=10&format=plain&rnd=new'

class emotionalCore:
    def pure_random(self):
        """
        Почти истинный рандом
        """
        try:
            num=int(str(urllib.request.urlopen(url).read()).replace("b'", '').replace("\\n", ' ').replace("'", ''))
        except:
            num=random.randint(0,10)
        return num

    @property
    def mood(self):
        """
        Общее ядро настроения
        """
        current = self.pure_random()
        if current<4:
            return 'Sad'
        elif 4<=current<7:
            return 'Neutral'
        else:
            return 'Happy'
        
    @property
    def will(self):
        """
        Общее ядро желаний
        """
        current = self.pure_random()
        if current<4:
            return 'Depressive'
        elif 4<=current<7:
            return 'Neutral'
        else:
            return 'Curious'
        
    @property
    def impulsivity(self):
        """
        Общее ядро активности
        """
        current = self.pure_random()
        if current<4:
            return 'Passive'
        elif 4<=current<7:
            return 'Neutral'
        else:
            return 'Active'

