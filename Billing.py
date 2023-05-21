import math
def flat_10_discount(total):
    if total>200:
        dtotal["flat_10_discount"]=0.1*(total)

def bulk_10_discount(total,s): 
    if s>20:
        dtotal["bulk_10_discount"]=0.1*(total)

def bulk_5_discount():
    total=sum([0.05*(prod[x]*qty[x])for x in prod if qty[x]>10]) 
    dtotal["bulk_5_discount"]=total       

def tiered_50_discount(s): 
    total=sum([0.5*((qty[x]-15)*prod[x])for x in prod if qty[x]>15 and s>30]) 
    dtotal["tiered_50_discount"]=total 

def ship_gift_cal(total_qty):
    g_cost=sum([qty[x] for x in qty if wrap[x] == "y"])
    cnt_packages=math.ceil(total_qty/10)  
    s_cost=5*cnt_packages
    return (g_cost,s_cost)  

prod={"Product A":20,"Product B":40,"Product C":50}
qty={}
wrap={}
dtotal={}
stotal=0
for x,y in prod.items():
    print("How much quantity of "+x+" is required?")
    q=int(input())
    qty[x]=q
    wr=input("Do you want to wrap the product (y/n)")
    wrap[x]=wr.lower()
    stotal+=y*qty[x]
total_qty = sum(qty.values())

flat_10_discount(stotal)
bulk_5_discount()
bulk_10_discount(stotal,total_qty)
tiered_50_discount(total_qty)

print("BILL:")
for x in prod:
    ptotal=prod[x]*qty[x]
    print(x," ",qty[x]," ",ptotal)
print("Subtotal: ",stotal)

maxi=max(dtotal, key=dtotal.get)
if dtotal[maxi]>0:
    print("Discount applied, "+maxi+" and the discount amount is: ",dtotal[maxi])

g_cost, s_cost=ship_gift_cal(total_qty)
print("Shipping fee: ",s_cost)
print("Gift wrap fee: ",g_cost)

gtotal=stotal-dtotal[maxi]+s_cost+g_cost
print("Grand Total: ",gtotal)


