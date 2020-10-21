change = int(input('change : '))
coin = 0
for coinType in [500, 100, 50, 10]:
    coin += change // coinType
    change = change % coinType

print(coin)
