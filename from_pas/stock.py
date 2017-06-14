packet = 10000;
print("Вартість пакету акцій = ", packet)

percent = int(input("Введіть зміну ціни 1 акції в процентах, %:\t"))
print("Сумарна вартість 5 частини пакета в", packet, "акцій", "=", (packet - (packet * percent) / 100) /5)
