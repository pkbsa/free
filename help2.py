print("************************************************************************************")
print()
print(" ร้านไก่ทอด KFD ")
print()
print("************************************************************************************")
print("1.ไก่ทอด(35บาท) 2.มันบด(20บาท) 3.ขนมปัง(15บาท) 4.เครื่องดื่มโค้ก(25บาท) 5.สิ้นสุดการสั่งซื้อ")
print()
print("************************************************************************************")

menu=[]
amount=[]
name=[]
price=[]

total = 0
i=0

while (1) :
    menu.append(int(input("กรุณาเลือกรายการสินค้า (1-5) : ")))
    if(menu[i] == 5) :
        break;
    amount.append(int(input("จำนวนชิ้น : ")))
    if(menu[i] == 1) :
        name.append("ไก่ทอด")
        price.append(35)
    elif menu[i] == 2 :
        name.append("มันบด")
        price.append(20)
    elif menu[i] == 3 :
        name.append("ขนมปัง")
        price.append(15)
    else :
        name.append("เครื่องดื่มโค้ก")
        price.append(25)
    print(menu,amount,name,price)
    i=i+1;

for i in range (len(menu)-1) :
    print(name[i], price[i],"x",amount[i],"=",(amount[i]*price[i]))
    total = total + (amount[i]*price[i]);
print("รวมเป็นเงิน :",float(total));
