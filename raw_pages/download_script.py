# https://shell.cloud.google.com/?project=cohesive-beach-456&show=ide%2Cterminal

i=0
for p in Post.get_lastest(200):
	i = i + 1
	f = open('./docs/' + str(i) + '.txt', 'w')
	f.write(p.title.encode('utf-8'))
	f.write('\n')
	f.write(p.date.strftime('%m/%d/%Y, %H:%M:%S'))
	f.write('\n')
	c = p.category if p.category else ''
	f.write(c)
	f.write('\n')
	ts = [t.encode('utf-8') for t in p.tags]
	tt = ','.join(ts) if ts else ''
	f.write(tt)
	f.write('\n')
	f.write(p.content.encode('utf-8'))
	f.write('\n')
	f.write('!@#$%')
	f.write('\n')
	f.close()

