import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('状态码:',r.status_code)

response_dict = r.json()
print('仓库:',response_dict['total_count'])

repo_dicts = response_dict['items']
print('返回存储库:',len(repo_dicts))

repo_dict = repo_dicts[0]
print('\nkeys:',len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

