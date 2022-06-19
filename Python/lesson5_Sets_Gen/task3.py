set_ten = {'Evans', 'Stone', 'Roberts', 'Mills', 'Lewis', 'Morgan'}
set_dota = {'Grant', 'Morgan', 'Evans', 'Mills', 'Jackson', 'Bradley'}
set_litr = {'Grant', 'Morgan', 'Evans', 'Gibson', 'Jackson', 'Barlow', 'Adams'}
print()
print('Увлекаются всем:', set_ten & set_dota & set_litr)
print()
except_ten = set_dota & set_litr - set_ten
print('Увлекаются только дотой и литрболом:', except_ten)
print()
except_dota = set_litr & set_ten - set_dota
print('Увлекаются только тенисом и литрболом:', except_dota)
print()
except_litr = set_ten & set_dota - set_litr
print('Увлекаются только тенисом и дотой:', except_litr)
print()
only_dota = set_dota - set_litr - set_ten
print('Увлекаются только дотой:', only_dota)
print()
only_litr = set_litr - set_dota - set_ten
print('Увлекаются только литрболом:', only_litr)
print()
only_ten = set_ten - set_dota - set_litr
print('Увлекаются только тенисом:', only_ten)
print()
#Увлечения








