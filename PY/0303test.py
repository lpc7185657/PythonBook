#6-1
me = {
    'first_name':'li',
    'last_name':'peng cheng',
    'age':'29',
    'city':'DaTong'
    }
#for a in me:
  #  print(me[a])
print(me)
#6-3
word = {
    'if':'如果',
    'elif':'否则如果',
    'else':'否则'
}
for key,a in word.items():
    print(key)
for key1,a1 in word.items():
    print('\nKey:' + key1)
    print('Value:' + a1)
for key2,a2 in sorted(word.items()):
    print(key2 , ':' , a2)