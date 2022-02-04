import instaloader
L = instaloader.Instaloader()
user = "minnnwoo_"
nano_influencer = [] # 계정명들import instaloader
import pandas as pd
import os
data = pd.read_csv('/Users/brightcircle/Desktop/Instagram paper/계산시트_csv.csv',
                   # names=['index','id','post_num','follower','catagory','audi_stat','follower_reach','reach','reach%','ER','posting_term'],
                   encoding='CP949')
insta_id = data['id']
insta_id_val = insta_id.values
insta_id_list = ['yhtmtg', 'minnnwoo_']
L = instaloader.Instaloader()

L.login('minwoodavid@naver.com', 'David2157!')


print(insta_id_list)

for account in insta_id_list:

    while True:
        try:
            result = {}
            comments = []
            profile = instaloader.Profile.from_username(L.context, account)
            posts = profile.get_posts()
            i = 0
            print(account, "시작")
            for post in posts:
                i+=1
                print(i)
                for comment in post.get_comments() :
                    if comment.owner == profile and "#" in comment.text:
                        comments.append(comment.text)
                        break
                    else :
                        break
                if i>=40:
                    break
            result[account] = comments
            print('엑셀로 저장')
            excel_name = str(account)
            data_frame = pd.DataFrame(result)
            data_frame.to_excel('./{}.xlsx'.format(excel_name), sheet_name=excel_name, startrow=0, header=True)
            print("저장완료")
            break
        except:
            print("계정 없음")
            break