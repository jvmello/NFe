#classe pra usuário com informações mínimas
class User:
    _username = 'Default'
    _usercpf = '000.000.000-00'

    def createUser(self, name, cpf):
        self._username = name
        self._usercpf = cpf

    def getName(self):
        return self._username

    def getCPF(self):
        return self._usercpf


#classe para cada mercado (em dúvida se faz classe para mercado ou para produto, ideias bem vindas)
class Market:
    _product = 'Default'
    _price = 0.00
    _city = 'Santa Maria'
    _unity = 1

    def createMarket(self, p, price, city, unity):
        self._product = p
        self._price = price
        self._city = city
        self._unity = unity

# Pra aprender a mexer com objeto em Python, ignorar
# x = User()
# x.createUser('Filipe', '035.936.600-75')
# print('o usuario foi criado ' + x.getName() + ' com CPF ' + x.getCPF())
