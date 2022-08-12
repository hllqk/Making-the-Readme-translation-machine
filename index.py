#by hllqk，代码特乱，我自己也不知道自己写的是什么垃圾
import re
import requests,json
#不要翻译匹配的关键词
notp=['http','[X','X]','[',']']
def ts(inpu):
	#要翻译匹配的关键词
	ma=['#','*','~','>']
	for i in ma:
		if i in inpu:
			return i
	return False
def translator(text):
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	post_form = {
        'i': text,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15584130884799',
        'sign': '7cb8e5dada47bfefe2cfee6c2e586375',
        'ts': '1558413088479',
        'bv': '66745c2bd404c2f62490e4e8dadb4b0e',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
	response = requests.post(url,data=post_form)
	trans_json = response.text
	trans_dict = json.loads(trans_json)
	result = trans_dict['translateResult'][0][0]['tgt']
	return result
def find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern,"",file)
    return unchinese
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
def check_contain_chinese(t):
  resultt = re.compile(u'[\u4e00-\u9fa5]')
  if resultt.search(t):
     return True
f=open('ch.txt')
ch=f.read()
text=ch.split('\n')
out=open('out.txt','w+')
out.write('')
out.close()
for i in text:
	if check_contain_chinese(i):
		if ts(i)!=False:
			tss=ts(i)
			#print(tss)
			hhh=i.replace(tss, '')
			hhh=hhh.strip()
			for ii in notp:
				if ii in hhh:
					hhh=hhh.replace(ii,'')
			#print(hhh)
			hhh=hhh.strip()
			#print(hhh)
			eng=translator(hhh)
			sb=i.replace(hhh,eng)
		#print(gg)
			eng=sb
		else:	
			#pr
			eng=translator(i)
			#print(i)
	else:
		eng=i
	out=open('out.txt','a+')
	for ii in notp:
		if ii in i:
			out.write(i+'\n')
		else:
			out.write(eng+'\n'+i+'\n')
		break
print('完成，前往out.txt查看')

'''
w=open('out.txt','w')
translation = translator.translate(ch)
w.write(ch)

print(translation)
'''