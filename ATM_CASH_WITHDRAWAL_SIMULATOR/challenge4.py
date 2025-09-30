
cash=int(input("Enter amount to withdraw: "))

if cash%100!=0:
    print("invalid amount")

else:
    note2000=cash//2000
    cash=cash%2000

    note500=cash//500
    cash=cash%500

    note100=cash//100

    if note2000 > 0:
        print("2000 x", note2000)
    if note500 > 0:
        print("500 x", note500)
    if note100 > 0:
        print("100 x", note100)