#8-6
""" 
def city_country(city,country):
    '''显示国家与城市名称'''
    a = city + ',' + country + '.'
    return a.title()

while True:
    ct = input('City:')
    cn = input('Country:')
    b = city_country(ct,cn)
    print(b)
    break """
#8-7
""" def make_album(singer,edition):
    ''' 显示专辑和歌手名称 '''
    a = {}
    a[edition] = singer
    return a

b = make_album('Skrillex','《First of the year》')
print(b) """

""" def make_album(singer,edition,song = ''):
    ''' 显示专辑和歌手名称 '''
    a = {}
    a[edition] = singer
    if song:
        a['song'] = song
    return a

b = make_album('Skrillex','《First of the year》')
print(b)

c = make_album('Skrillex','《First of the year》','12')
print(c) """

#8-8
def make_album(singer,edition,song = ''):
    ''' 显示专辑和歌手名称 '''
    a = {}
    a[edition] = singer
    if song:
        a['song'] = song
    return a

while True:
    si = input('enter singer:')
    if si == 'q':
        break
    ed = input('enter edition:')
    if ed == 'q':
        break
    so = input('enter song:')
    if so == 'q':
        break
    c = make_album(si,ed,so)
    print(si + ' ' + ed + ' ' + so)