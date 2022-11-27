import requests
import json
# from lxml import etree
import time
# import xlwt
import sys
import datetime
import re
import tkinter as tk
def go():
    global web
    web =  window_s.get()
    window.destroy()
def go2():
    window.destroy()
def params1_set(fid,pageIndex):
    params1 ={"fid":fid,"count":50,"sortType":0,"pageIndex":pageIndex,"_SessionToken":"r:2f8b51b25e0b2929a4c8514f37f14c2f","_ClientVersion":"js3.4.1","_ApplicationId":"E62VyFVLMiW7kvbtVq3p","g_os":"PCWeb","_InstallationId":"cb899802-f031-4a0c-8739-c2d2a8075728"}
    return  params1
def params2_set(targetId):
    params2 = {"itemsJson":[{"objectId":targetId}],"skipAccessories":0,''"_SessionToken":"r:2f8b51b25e0b2929a4c8514f37f14c2f","_ClientVersion":"js3.4.1","_ApplicationId":"E62VyFVLMiW7kvbtVq3p","g_os":"PCWeb","_InstallationId":"cb899802-f031-4a0c-8739-c2d2a8075728"}
    return params2
def params3_set(ids):
    params3 = {"ids":[ids],"withExtra":1,"_SessionToken":"r:2f8b51b25e0b2929a4c8514f37f14c2f","_ClientVersion":"js3.4.1","_ApplicationId":"E62VyFVLMiW7kvbtVq3p","g_os":"PCWeb","_InstallationId":"cb899802-f031-4a0c-8739-c2d2a8075728"}
    return params3
def params4_set(id):
    params4 = {"id":id,"_SessionToken":"r:2f8b51b25e0b2929a4c8514f37f14c2f","_ClientVersion":"js3.4.1","_ApplicationId":"E62VyFVLMiW7kvbtVq3p","g_os":"PCWeb","_InstallationId":"cb899802-f031-4a0c-8739-c2d2a8075728"}
    return params4
def download(url,headers,params):
    ret = session.post(url = url,headers = headers,data = json.dumps(params))
    # print(type(ret))
    # print(ret.text)
    return ret
def headers_set(content_length):

    headers = {
    #:authority: api.mojidict.com
    #:method: POST
    #:path: /parse/functions/folder-fetchContentWithRelatives
    #:scheme: https
    'accept': '*/*',
    #accept-encoding: gzip, deflate, br
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'content-length': str(content_length),  #250翻页 256单词详细 231自造句子详细 211句子详细
    'content-type': 'text/plain',
    'dnt': '1',
    'origin': 'https://www.mojidict.com',
    'referer': 'https://www.mojidict.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    return headers
def Setting(xyz):
    word = xyz['result']['result'][0]['word']
    details = xyz['result']['result'][0]['details']
    subdetails = xyz['result']['result'][0]['subdetails']
    examples = xyz['result']['result'][0]['examples']

    # dict_keys(['excerpt', 'spell', 'accent', 'pron', 'romaji', 'createdAt', 'updatedAt', 'outSharedNum', 'isFree', 'quality', 'viewedNum', 'objectId'])
    #{'excerpt': '[自动·二类] 游戏，玩耍。（遊び興ずる。無心に遊ぶ。） 说说笑笑，耍笑，闹着玩儿。（ふざけた気持ちで事をする。） ', 'spell': '戯れる', 'accent': '④', 'pron': 'たわむれる', 'romaji': 'tawamureru', 'createdAt': '2019-05-07T03:48:47.619Z', 'updatedAt': '2022-11-04T23:58:12.315Z', 'outSharedNum': 3, 'isFree': 1, 'quality': 1000, 'viewedNum': 228, 'objectId': '198943094'}

    #1111111111111111111111111111111111111111##################################################
    word_spell = word['spell']#单词
    Voice = word_spell

    if 'pron' in word:
        word_pron = word['pron']#假名
    else:
        word_pron = ''
    word_excerpt = word['excerpt']#概述
    # print(word_spell)
    # print(word_pron)

    #222222222222222222222222222222222222###################################################
    # print(details[0])
    # {'title': '自动#二类', 'index': 0, 'createdAt': '2019-05-07T03:48:49.595Z', 'updatedAt': '2019-10-24T12:54:23.314Z', 'wordId': '198943094', 'objectId': '37225'}
    details_title = details[0]['title'].replace('#','・')#词性
    # print(details_title)

    if len(subdetails) > 0:
        #3333333333333333333333333333333333###################################################
        # print(len(subdetails))
        # {'title': '游戏，玩耍。（遊び興ずる。無心に遊ぶ。）', 'index': 0, 'createdAt': '2019-05-07T03:48:50.931Z', 'updatedAt': '2019-10-24T12:59:55.418Z', 'wordId': '198943094', 'detailsId': '37225', 'objectId': '52394'}
        # {'title': '说说笑笑，耍笑，闹着玩儿。（ふざけた気持ちで事をする。）', 'index': 1, 'createdAt': '2019-05-07T03:48:50.596Z', 'updatedAt': '2019-10-24T12:59:48.434Z', 'wordId': '198943094', 'detailsId': '37225', 'objectId': '52395'}
        # {'title': '调戏；挑逗。（男女がみだらな言動をする。）', 'index': 2, 'createdAt': '2019-05-07T03:48:50.421Z', 'updatedAt': '2019-10-24T12:59:46.929Z', 'wordId': '198943094', 'detailsId': '37225', 'objectId': '52396'}

        subdetails_dict = {}
        for i in range(0,len(subdetails)):

            # print(subdetails[i])
            subdetails_title = subdetails[i]['title']  # 全部意思
            subdetails_objectId = subdetails[i]['objectId']#意思和例子对应关系
            subdetails_dict[subdetails_title] = subdetails_objectId

        # print(subdetails_dict)

        #4444444444444444444444444444444###################################################
        # {'title': '女に戯れる。', 'index': 0, 'trans': '调戏妇女。', 'createdAt': '2019-05-07T03:48:52.085Z', 'updatedAt': '2019-10-24T13:07:14.203Z', 'wordId': '198943094', 'subdetailsId': '52396', 'isFree': 1, 'quality': 1000, 'isChecked': 0, 'objectId': '33918', 'notationTitle': '<ruby n5><rb>女</rb><rp>(</rp><rt roma=\'onna\' hiragana=\'おんな\' lemma=\'女\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >に</span><ruby ><rb>戯れる</rb><rp>(</rp><rt roma=\'tawamureru\' hiragana=\'たわむれる\' lemma=\'戯れる\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >。</span>'}
        # {'title': '子どもたちがたわむれて遊んでいる。', 'index': 0, 'trans': '孩子们说说笑笑地玩儿着。', 'createdAt': '2019-05-07T03:48:52.269Z', 'updatedAt': '2019-10-24T13:07:14.467Z', 'wordId': '198943094', 'subdetailsId': '52395', 'isFree': 1, 'quality': 1000, 'isChecked': 0, 'objectId': '33916', 'notationTitle': '<ruby n5><rb>子ども</rb><rp>(</rp><rt roma=\'kodomo\' hiragana=\'こども\' lemma=\'子供\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" n5>たち</span><span class="moji-toolkit-org" >が</span><span class="moji-toolkit-org" >たわむれ</span><span class="moji-toolkit-org" >て</span><ruby n5><rb>遊ん</rb><rp>(</rp><rt roma=\'ason\' hiragana=\'あそん\' lemma=\'遊ぶ\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >で</span><span class="moji-toolkit-org" >いる</span><span class="moji-toolkit-org" >。</span>'}
        # {'title': '子どもがたわむれている。', 'index': 0, 'trans': '小孩在玩耍。', 'createdAt': '2019-05-07T03:48:52.593Z', 'updatedAt': '2019-10-24T13:07:14.929Z', 'wordId': '198943094', 'subdetailsId': '52394', 'isFree': 1, 'quality': 1000, 'isChecked': 0, 'objectId': '33915', 'notationTitle': '<ruby n5><rb>子ども</rb><rp>(</rp><rt roma=\'kodomo\' hiragana=\'こども\' lemma=\'子供\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >が</span><span class="moji-toolkit-org" >たわむれ</span><span class="moji-toolkit-org" >て</span><span class="moji-toolkit-org" >いる</span><span class="moji-toolkit-org" >。</span>'}
        # {'title': '小猫がボールと戯れる。', 'index': 1, 'trans': '小猫嬉球。', 'createdAt': '2019-05-07T03:48:52.189Z', 'updatedAt': '2019-10-24T13:07:14.352Z', 'wordId': '198943094', 'subdetailsId': '52395', 'isFree': 1, 'quality': 1000, 'isChecked': 0, 'objectId': '33917', 'notationTitle': '<ruby ><rb>小猫</rb><rp>(</rp><rt roma=\'koneko\' hiragana=\'こねこ\' lemma=\'子猫\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >が</span><span class="moji-toolkit-org" >ボール</span><span class="moji-toolkit-org" >と</span><ruby ><rb>戯れる</rb><rp>(</rp><rt roma=\'tawamureru\' hiragana=\'たわむれる\' lemma=\'戯れる\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >。</span>'}
        # {'title': '男に戯れる。', 'index': 1, 'trans': '挑逗男人。', 'createdAt': '2019-05-07T03:48:52.206Z', 'updatedAt': '2019-10-24T13:07:14.377Z', 'wordId': '198943094', 'subdetailsId': '52396', 'isFree': 1, 'quality': 1000, 'isChecked': 0, 'objectId': '33919', 'notationTitle': '<ruby n5><rb>男</rb><rp>(</rp><rt roma=\'otoko\' hiragana=\'おとこ\' lemma=\'男\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >に</span><ruby ><rb>戯れる</rb><rp>(</rp><rt roma=\'tawamureru\' hiragana=\'たわむれる\' lemma=\'戯れる\'></rt><rp>)</rp></ruby><span class="moji-toolkit-org" >。</span>'}
        # print(len(examples))
        examples_dict = {}
        for i in range(0,len(examples)):

            # print(examples[i])
            try:
                examples_title = examples[i]['title']+'<br>'+examples[i]['trans']
            except KeyError:
                examples_title = examples[i]['title']
            examples_subdetailsId = examples[i]['subdetailsId']#意思和例子对应关系
            examples_dict[examples_title] = examples_subdetailsId

        # print(examples_dict)

        Total_dict = {}

        for i in subdetails_dict.keys():
            Total_dict[i] = ''
            for j in examples_dict.keys():
                if subdetails_dict[i] == examples_dict[j] :
                    if len(Total_dict[i]) > 0 :
                        Total_dict[i] += '<br>'+j
                    else:
                        Total_dict[i] = j
                        Voice += ','+ j[:j.find("<br>")]
        # print(Total_dict)
        # print(Voice)
        Total_String = ''
        for i in Total_dict.keys():
            if Total_String == '':
                Total_String += i+'<br>'+Total_dict[i]
            else:
                Total_String += '<br>'*2+i+'<br>'+Total_dict[i]

        return word_spell,word_pron,Voice,details_title,Total_String
    else:

        return word_spell, word_pron, Voice,word_excerpt
def Settings(xyz):
# {"result":{"1":[{"name":"DUT西贝同学","email":"907523269@qq.com","createdAt":"2019-03-29T06:05:21.041Z","updatedAt":"2022-11-03T14:17:51.767Z","followedFoldersNum":16,"followedUsersNum":20,"fansNum":12,"activityNum":1306,"sharedFoldersNum":1,"activityNumByOthers":248,"gender":2,"hasAvatar":1,"unionId":"JP120638","objectId":"zNYGRnQqE3"}],"result":[{"createdBy":"zNYGRnQqE3","langEnv":"zh-CN_ja","title":"無限大の均一磁界において","trans":"在无限大的均匀磁场中","createdAt":"2021-04-19T16:17:24.088Z","updatedAt":"2022-11-05T06:29:42.704Z","viewedNum":1,"objectId":"NQSpHPJg1N","notationTitle":"<ruby n2><rb>無限</rb><rp>(</rp><rt roma='mugen' hiragana='むげん' lemma='無限'></rt><rp>)</rp></ruby><ruby ><rb>大</rb><rp>(</rp><rt roma='dai' hiragana='だい' lemma='大-大学'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >の</span><ruby ><rb>均一</rb><rp>(</rp><rt roma='kin'itu' hiragana='きんいつ' lemma='均一'></rt><rp>)</rp></ruby><ruby ><rb>磁界</rb><rp>(</rp><rt roma='zikai' hiragana='じかい' lemma='磁界'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >に</span><span class=\"moji-toolkit-org\" >おい</span><span class=\"moji-toolkit-org\" >て</span>"}],"code":200}}
    title = xyz['result']['result'][0]['title']#得到日语句子
    trans = xyz['result']['result'][0]['trans']#得到翻译
    Voice = title
    return title,trans,Voice
def Settingss(xyz):
   # {"result":{"1":{"name":"DUT西贝同学","email":"907523269@qq.com","createdAt":"2019-03-29T06:05:21.041Z","updatedAt":"2022-11-03T14:17:51.767Z","followedFoldersNum":16,"followedUsersNum":20,"fansNum":12,"activityNum":1306,"sharedFoldersNum":1,"activityNumByOthers":248,"gender":2,"hasAvatar":1,"unionId":"JP120638","objectId":"zNYGRnQqE3"},"102":{"createdBy":"zNYGRnQqE3","langEnv":"zh-CN_ja","updatedBy":"zNYGRnQqE3","spell":"均一磁界","pron":"きんいつじかい","accent":"◎","createdAt":"2021-04-19T16:10:48.744Z","updatedAt":"2021-04-19T16:10:48.817Z","excerpt":"[固有名詞] 均匀磁场","objectId":"QQLCWSRd4g"},"result":{"createdBy":"zNYGRnQqE3","wordId":"QQLCWSRd4g","updatedBy":"zNYGRnQqE3","title":"均一磁界とは磁束密度Bの均一性を有する磁界というである。","trans":"均匀磁场是指磁场内每一点的磁感应强度（磁通密度）B的大小相等方向相同的磁场。","index":0,"subdetailsId":"JnBGQ2FFrP","createdAt":"2021-04-19T16:10:48.792Z","updatedAt":"2022-11-05T07:08:07.681Z","viewedNum":1,"objectId":"aszQuRoBD1","notationTitle":"<ruby ><rb>均一</rb><rp>(</rp><rt roma='kin'itu' hiragana='きんいつ' lemma='均一'></rt><rp>)</rp></ruby><ruby ><rb>磁界</rb><rp>(</rp><rt roma='zikai' hiragana='じかい' lemma='磁界'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >と</span><span class=\"moji-toolkit-org\" >は</span><ruby ><rb>磁束</rb><rp>(</rp><rt roma='zisoku' hiragana='じそく' lemma='磁束'></rt><rp>)</rp></ruby><ruby n1><rb>密度</rb><rp>(</rp><rt roma='mitudo' hiragana='みつど' lemma='密度'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >B</span><span class=\"moji-toolkit-org\" >の</span><ruby ><rb>均一</rb><rp>(</rp><rt roma='kin'itu' hiragana='きんいつ' lemma='均一'></rt><rp>)</rp></ruby><ruby ><rb>性</rb><rp>(</rp><rt roma='sei' hiragana='せい' lemma='性'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >を</span><ruby n1><rb>有する</rb><rp>(</rp><rt roma='yuusuru' hiragana='ゆうする' lemma='有する'></rt><rp>)</rp></ruby><ruby ><rb>磁界</rb><rp>(</rp><rt roma='zikai' hiragana='じかい' lemma='磁界'></rt><rp>)</rp></ruby><span class=\"moji-toolkit-org\" >と</span><span class=\"moji-toolkit-org\" n5>いう</span><span class=\"moji-toolkit-org\" >で</span><span class=\"moji-toolkit-org\" n4 n5>ある</span><span class=\"moji-toolkit-org\" >。</span>"},"code":200}}
    title = xyz['result']['result']['title']  # 得到日语句子
    trans = xyz['result']['result']['trans']  # 得到翻译
    Voice = title
    return title, trans, Voice
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
# 1.先post一次，得到itemsNum，计算出需要的pageIndex页数，targetId个数代表导出个数，得到该页下的targetId做成列表，
# 2.如果itemsNum小于50，则按照targetId个数来进行下一步，如果itemsNum大于50，则通过itemsNum/


# web = input("输入网址，若未输入则使用默认收藏夹开始下载:")
web = ''
window = tk.Tk()
window.title('请输入网址')
# window.minsize(200,60)
window.geometry('600x100')
window.geometry('+1000+550')
window_v = tk.Button(window,text = '确认',command=go)
window_v.place(relx=0.5,rely=0.65,anchor='n')
window_s = tk.Entry(window,width=80)
window_s.place(relx=0.5,rely=0.5,anchor = 'center')
window.mainloop()

if len(web) == 0 :
    web = 'https://www.mojidict.com/collection/6qoIu0UC8O?path=%2Fcollection_%2Fcollection%2F6qoIu0UC8O' #默认收藏夹

fid=web[-10:]
# print(fid)
session = requests.session()

url1 = 'https://api.mojidict.com/parse/functions/folder-fetchContentWithRelatives'#翻页
url2='https://api.mojidict.com/parse/functions/nlt-fetchManyLatestWords'#详细单词 102
url3 = 'https://api.mojidict.com/parse/functions/nlt-fetchManySentences'#详细自造句子 120
url4 = 'https://api.mojidict.com/parse/functions/nlt-fetchExample' #详细句子 103
params1=params1_set(fid,1)

ret = download(url1,headers_set(250),params1)

# print(ret.text)
itemsNum =json.loads(ret.text)['result']['1000'][0]['itemsNum']#该收藏下单词个数
totalPage = json.loads(ret.text)['result']['totalPage']#该收藏下总页数
File_name = json.loads(ret.text)['result']['1000'][0]['title']#该收藏目录名字
print(File_name)

Num_list = json.loads(ret.text)['result']['result']

targetId_dict = {}
targetId_list = []
for i in Num_list:

    targetId = i['targetId']  # 得到单个单词的targetId
    targetType = i['targetType']#得到单个单词的targetType

    if targetType == 1000 or targetType == 10:#1000为收藏夹 10为外部链接
        continue
    targetId_dict[targetId] = targetType
    targetId_list.append(targetId)

if itemsNum > 50:
    for j in range(2,totalPage+1):
        params1 = params1_set(fid, j)
        ret = download(url1, headers_set(250), params1)
        Num_list = json.loads(ret.text)['result']['result']
        for i in Num_list:
            targetId = i['targetId']  # 得到单个单词的targetId
            targetType = i['targetType']#得到单个单词的targetType
            if targetType == 1000 or targetType == 10:
                continue
            targetId_dict[targetId] = targetType
            targetId_list.append(targetId)
        time.sleep(1)
print(len(targetId_dict))
# print(targetId_list)
if len(targetId_dict) == 0:
    print("targetId_dict为零")
    sys.exit()

# print(targetId_dict)
# print(len(targetId_list))

# dict_keys(['createdBy', 'langEnv', 'updatedBy', 'spell', 'pron', 'accent', 'createdAt', 'updatedAt', 'excerpt', 'outSharedNum', 'viewedNum', 'objectId'])
# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('sheet 1')

# print(len(targetId_list))
now_time = str(datetime.datetime.now().replace(microsecond = 0)).replace(':','-')
f = open(now_time+deEmojify(File_name)+'.txt','w+',encoding='utf-8')
op = 0
for h in range(0,len(targetId_dict)):
    targetId = list(targetId_dict.keys())[h]
    targetType = targetId_dict[targetId]
    print(targetId)
    print(h)
    print(targetType)
    if targetType == 120 :
        params3 = params3_set(targetId)
        ret = download(url3, headers_set(231), params3)
        time.sleep(1)
        print(ret.text)
        Response_dict = json.loads(ret.text)
        try:
            Response_dict['result']['result'][0]['title']  # 得到日语句子
        except KeyError:
            op += 1
            continue
        Total_truple = Settings(Response_dict)
        sentence_title = Total_truple[0]
        sentence_trans = Total_truple[1]
        sentence_Voice = Total_truple[2]
        f.writelines((str(h+1) + '\t' + str(sentence_title) + '\t' +''+'\t'+str(sentence_trans) + '\t' + str(sentence_Voice)).replace('\n','<br>') + '\n')
        # sheet.write(h, 0, str(h+1))
        # sheet.write(h, 1, sentence_title)
        # sheet.write(h, 3, sentence_trans)
        # sheet.write(h, 4, sentence_Voice)
    elif targetType == 102 :
        params2 = params2_set(targetId)
        ret = download(url2,headers_set(256),params2)
        time.sleep(1)
        print(ret.text)
        Response_dict = json.loads(ret.text)
        try:
            Response_dict['result']['result'][0]['word']  # 得到日语句子
        except KeyError:
            op += 1
            continue
        # print(Response_dict)
        Total_truple = Setting(Response_dict)
        Total_String = ''
        if len(Total_truple) == 5:
            #word_spell,word_pron,word_excerpt,Total_dict,Voice,details_title#词性 6
            Total_String = Total_truple[3]+'<br>'+Total_truple[4]
        else:
            Total_String = Total_truple[3]
        word_spell = Total_truple[0]
        word_pron = Total_truple[1]
        Voice = Total_truple[2]
        # print(word_spell)
        # print(word_pron)
        # print(Voice)
        # print(Total_String)
        # sheet.write(h,0,str(h+1))
        # sheet.write(h,1,word_spell)
        # sheet.write(h,2,word_pron)
        # sheet.write(h,3,Total_String)
        # sheet.write(h,4,Voice)
        f.writelines((str(h+1) + '\t' + str(word_spell) + '\t' + str(word_pron)+ '\t' + str(Total_String) + '\t' + str(Voice)).replace('\n','<br>') + '\n')
    elif targetType == 103 :
        params4 = params4_set(targetId)
        ret = download(url4, headers_set(211), params4)
        time.sleep(1)
        print(ret.text)
        Response_dict = json.loads(ret.text)
        try:
            Response_dict['result']['result']['title']   # 得到日语句子
        except KeyError:
            op += 1
            continue
        Total_truple = Settingss(Response_dict)
        sentence_title = Total_truple[0]
        sentence_trans = Total_truple[1]
        sentence_Voice = Total_truple[2]

        # sheet.write(h, 0, str(h+1))
        # sheet.write(h, 1, sentence_title)
        # sheet.write(h, 3, sentence_trans)
        # sheet.write(h, 4, sentence_Voice)
        f.writelines((str(h+1) + '\t' + str(sentence_title) + '\t' +''+'\t'+str(sentence_trans) + '\t' + str(sentence_Voice)).replace('\n','<br>') + '\n')
# now_time = str(datetime.datetime.now().replace(microsecond = 0)).replace(':','-')
f.close()
print(op)
# wbk.save(now_time+deEmojify(File_name)+'.xls')
window = tk.Tk()
window.title('导出结束')
# window.minsize(200,60)
window.geometry('250x100')
window.geometry('+1000+500')
window_v = tk.Button(window,text = '确认',command=go2)
window_v.place(relx=0.5,rely=0.65,anchor='n')
window.mainloop()


