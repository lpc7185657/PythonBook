users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}
for a,b in users.items():
    print('Username:' + a)
    full_name = b['first'] +' ' +  b['last']
    locations = b['location']
    print('\t' + 'full name:' + full_name.title())
    print('\t' + 'location:' + locations.title() + '\n')


name = '如果你告诉我是谁，我会给你发一条信息。'
name += '\t' + '现在告诉我你是谁：'
name += '\t' + '现在告诉我你是谁：'
name += '\t' + '现在告诉我你是谁：'
name1 = (input(name))
print('欢迎你！ ' + name1)