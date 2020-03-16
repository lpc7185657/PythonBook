#8-3
def make_shirt(size,word):
    '''尺码信息'''
    print('我想订一间T恤，尺码为' + size + '码，' + '上面印有“' + word + '”字样就可以。')
make_shirt('42','我爱你')

#8-4
def make_shirt1(size,word = 'I Love Python'):
    '''尺码信息'''
    print('我想订一间T恤，尺码为' + size + '码，' + '上面印有“' + word + '”字样就可以。')
make_shirt1('大号')
make_shirt1('中号')
make_shirt1(size = '大号',word = '大同')

#8-5
def discribe_city(city,country = 'China'):
    '''城市和国家信息'''
    print(city + ' is in ' + country + '.')
discribe_city(city = 'Da tong')
discribe_city('Da tong')
discribe_city(city = 'Bombay',country = 'India')