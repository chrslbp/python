"""Here is the implementation of the Order class"""


class Order:
    goods = []
    amounts = []
    prices = []
    status = 'open'

    def formatting(self):
        for g in range(len(self.goods)):

            if self.goods[g][0].islower():
                 self.goods[g] = self.goods[g].capitalize()

            elif self.goods[g].isupper():
                self.goods[g] = self.goods[g].lower().capitalize()

        return self.goods

    def add_goods(self, name, amount, price):
        if name in self.goods:
            print(f'{name} alredy in order')
        self.goods.append(name)
        self.amounts.append(amount)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for p in range(len(self.prices)):
            total += self.prices[p] + self.amounts[p]

        return f'total: {total}'

    def pay(self, payment_type):
        if payment_type == 'debit':
            print('Processing debit payment type')
        elif payment_type == 'credit':
            print('Processing credit payment type')
        else:
            raise Exception(f'Unknown payment type: {payment_type}')


order = Order()
order.add_goods('Balls', 2, 69)
order.add_goods('Cucumbers', 1, 132)
order.add_goods('peaches', 1, 169)
order.add_goods('BANANAS', 5, 77)
order.add_goods('oranges', 8, 90)
order.add_goods('peaches', 1, 169)
# print(order.total_price())

order.formatting()
