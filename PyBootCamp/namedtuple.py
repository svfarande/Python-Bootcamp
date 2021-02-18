from collections import namedtuple

Car = namedtuple('Car', ['name', 'company', 'CNG', 'PriceStart'])
nexon = Car('Nexon', 'TATA', False, 7)
baleno = Car(company='Suzuki', name='Baleno', PriceStart=5.5, CNG=True)

print(Car)  # <class '__main__.Car'>
print(nexon)    # Car(name='Nexon', company='TATA', CNG=False, PriceStart=7)
print(baleno)   # Car(name='Baleno', company='Suzuki', CNG=True, PriceStart=5.5)

# Accessing via fieldname
print(f"{nexon.name}({nexon.company}) price start is {nexon.PriceStart}L. CNG Present -"
      f" {nexon.CNG}")  # Nexon(TATA) price start is 7L. CNG Present - False

# Accessing via index
print(f"{baleno[0]}({baleno[1]}) price start is {baleno[3]}L. CNG Present - {baleno[2]}")
# Baleno(Suzuki) price start is 5.5L. CNG Present - True
