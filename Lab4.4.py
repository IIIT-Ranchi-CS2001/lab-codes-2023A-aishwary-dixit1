# Generate two sets – first for all singers and second for all dancers of the class using set comprehension. 
# Perform set operations to generate the following sets 
# of all artists of the class
# allrounders of the class
# dancers but not singers
# singers but not dancers
# dancers but not singers cum singers but not dancers

singers_list = list(str(input("Enter the singers name (separate by spaces): ")).split())
dancers_list = list(str(input("Enter the dancers name (separate by spaces): ")).split())

singers = {singer for singer in singers_list}
dancers = {dancer for dancer in dancers_list}

all_artists = singers | dancers 
allrounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
symmetric_diff = singers ^ dancers

print("\nAll artists:", all_artists)
print("\nAllrounders:", allrounders)
print("\nDancers but not singers:", dancers_not_singers)
print("\nSingers but not dancers:", singers_not_dancers)
print("\nDancers but not singers cum Singers but not dancers:", symmetric_diff)
