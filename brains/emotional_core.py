import urllib, random

url = 'https://www.random.org/integers/?num=0&min=0&max=10&col=1&base=10&format=plain&rnd=new'

class emotionalCore:
    async def pure_random():
        """
        Почти истинный рандом
        """
        try:
            num=int(str(urllib.request.urlopen(url).read()).replace("b'", '').replace("\\n", ' ').replace("'", ''))
        except:
            num=random.randint(0,10)
        return num

    @property
    async def mood():
        """
        Общее ядро настроения
        """
        if pure_random<4:
            return 'Sad'
        elif 3<pure_random<7:
            return 'Neutral'
        else:
            return 'Happy'
        
    @property
    async def will():
        """
        Общее ядро желаний
        """
        if pure_random<4:
            return 'Depressive'
        elif 3<pure_random<7:
            return 'Neutral'
        else:
            return 'Curious'
        
    @property
    async def impulsivity():
        """
        Общее ядро активности
        """
        if pure_random<4:
            return 'Passive'
        elif 3<pure_random<7:
            return 'Neutral'
        else:
            return 'Active'

