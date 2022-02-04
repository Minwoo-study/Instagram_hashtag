import instaloader
import pandas as pd
import os
data = pd.read_csv('C:/Users/SeungJong/Desktop/학회/계산시트_csv.csv',
                   # names=['index','id','post_num','follower','catagory','audi_stat','follower_reach','reach','reach%','ER','posting_term'],
                   encoding='CP949')
insta_id = data['id']
insta_id_val = insta_id.values
insta_id_list = insta_id_val.tolist()
L = instaloader.Instaloader()

L.login('sample_life_ta', 'sample1234*')


print(insta_id_list)
for account in insta_id_list:
    while True:
        try:
            result = {}
            hashtag = []
            profile = instaloader.Profile.from_username(L.context, account)
            posts = profile.get_posts()
            i = 0
            print(account, "시작")
            for post in posts:
                hashtag += post.caption_hashtags
                i += 1
                if i >= 40:
                    break
            result[account] = hashtag
            print('엑셀로 저장')
            excel_name = str(account)
            data_frame = pd.DataFrame(result)
            data_frame.to_excel('./{}.xlsx'.format(excel_name), sheet_name=excel_name, startrow=0, header=True)
            print("저장완료")
            break
        except:
            print("계정 없음")
            break
