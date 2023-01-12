from urllib.parse import urlsplit, parse_qsl, unwrap


def parse(url: str) -> dict:
	result = parse_qsl(urlsplit(url).query)
	new_dict = {}
	for item in result:
		new_dict[item[0]] = item[1]
	return dict(result)


if __name__ == '__main__':
	assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
	assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
	assert parse('http://example.com/') == {}
	assert parse('http://example.com/?') == {}
	assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
	assert parse('http://example.com/users/admin?name=Dima') == {'name': 'Dima'}
	assert parse('http://example.com/users/admin/index.php') == {}
	assert parse('http://example.com/cats?name=shinshilla&color=silver') == {'name': 'shinshilla', 'color': 'silver'}
	assert parse('http://example.com/admin/new-cat?breed=british&color=white') == {'breed': 'british', 'color': 'white'}
	assert parse('http://example.com/blog/about/cats?breed=scottish&color=all') == {'breed': 'scottish', 'color': 'all'}
	assert parse('http://example.com/store/laptops/macbook?model=m2&color=all') == {'model': 'm2', 'color': 'all'}
	assert parse('http://example.com/laptops/store/macbook?model=m2&color=all&ram=16gb') == {'model': 'm2', 'color': 'all', 'ram': '16gb'}


def parse_cookie(query: str) -> dict:
	result = unwrap(query).split(";")
	result = (list(filter(lambda x: x, result)))
	result = [item.split('=', 1) for item in result]
	result = [item for i in result for item in i]
	d1 = {result[a]: result[a + 1] for a in range(0, len(result), 2)}
	return d1


if __name__ == '__main__':
	assert parse_cookie('name=Dima;') == {'name': 'Dima'}
	assert parse_cookie('') == {}
	assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
	assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
	assert parse_cookie('user=Dima=Admin;status=noob;') == {'user': 'Dima=Admin', 'status': 'noob'}
	assert parse_cookie('type=car=Lexus;model=ls500h;') == {'type': 'car=Lexus', 'model': 'ls500h'}
	assert parse_cookie('engine=hybrid=3.5;H.P.=400;') == {'engine': 'hybrid=3.5', 'H.P.': '400'}
	assert parse_cookie('suspension=pneumatic;WD=4WD;') == {'suspension': 'pneumatic', 'WD': '4WD'}
	assert parse_cookie('crypto=btc=16500;status=bearmarket;') == {'crypto': 'btc=16500', 'status': 'bearmarket'}
	assert parse_cookie('python=3.11;course=python_pro;') == {'python': '3.11', 'course': 'python_pro'}
