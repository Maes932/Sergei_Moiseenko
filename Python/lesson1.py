from ossaudiodev import SNDCTL_DSP_BIND_CHANNEL


rub = 4
kop = 12
product = 5
amount = (rub * 100 + kop)
total = (amount / 100) * product
print("Цена за 5 продуктов-" ,total)
