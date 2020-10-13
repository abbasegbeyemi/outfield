# Playing around with hashtables
from psolv_ch_6.abstract_data_types import HashTable

H = HashTable(11)

H[19] = "abbas"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

H[19] = "ruki"

H["samael"] = 'funto'
H["leamas"] = 'Wale'
H[1] = 'Toyyibat'

print(H.data)
print(H.slots)
