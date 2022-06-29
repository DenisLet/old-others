import requests
from bs4 import BeautifulSoup
url_home="https://24score.pro/basketball/team/usa/san_antonio_spurs_(m)/"
url_away="https://24score.pro/basketball/team/usa/miami_heat_(m)/"
def layout(y):
    home_1st,home_2nd,home_3rd,home_4th=[],[],[],[]
    away_1st,away_2nd,away_3rd,away_4th=[],[],[],[]
    home_1sthalf,home_2ndhalf=[],[]
    away_1sthalf,away_2ndhalf=[],[]
    total_1sthalf,total_2ndhalf=[],[]
    firstQwtr, secondQwtr, thirdQwtr, fourthQwtr=[],[],[],[]
    totalHome,totalAway=[],[]
    totalMatch=[]
    for i in y:
        firstQ,secondQ,thirdQ,fourthQ=i[0],i[1],i[2],i[3]
        home1, away1 = int(firstQ.split(":")[0]), int(firstQ.split(":")[1])
        home2, away2 = int(secondQ.split(":")[0]), int(secondQ.split(":")[1])
        home3, away3 = int(thirdQ.split(":")[0]), int(thirdQ.split(":")[1])
        home4, away4 = int(fourthQ.split(":")[0]), int(fourthQ.split(":")[1])
        home_1st.append(home1),home_2nd.append(home2),home_3rd.append(home3),home_4th.append(home4)
        away_1st.append(away1),away_2nd.append(away2),away_3rd.append(away3),away_4th.append(away4)
        home_1sthalf.append(home1+home2),home_2ndhalf.append(home3+home4)
        away_1sthalf.append(away1+away2),away_2ndhalf.append(away3+away4)
        total_1sthalf.append(home1+home2+away1+away2),total_2ndhalf.append(home3+home4+away3+away4)
        firstQwtr.append(home1+away1),secondQwtr.append(home2+away2),thirdQwtr.append(home3+away3),\
        fourthQwtr.append(home4+away4)
        totalHome.append(home1+home2+home3+home4),totalAway.append(away1+away2+away3+away4)
        totalMatch.append(home1 + home2 + home3 + home4 + away1 + away2 + away3 + away4)
    return home_1st,home_2nd,home_3rd,home_4th,away_1st,away_2nd,away_3rd,away_4th,home_1sthalf,home_2ndhalf,\
           away_1sthalf,away_2ndhalf,total_1sthalf,total_2ndhalf,firstQwtr,secondQwtr,thirdQwtr,fourthQwtr,totalHome,\
           totalAway,totalMatch
def cleaning(x):
    scorelist=[]
    for score in x :
        if "— —" in score.text or "Отложен" in score.text or "тех. пор." in score.text:
            continue
        xline=score.findAll(text=True,recursive=False).pop(1).replace("OT","")\
            .replace("(","").replace(")","").replace(" ","").strip().split(",")
        scorelist.append(xline)
    return scorelist
def home_team_homescore(url_home):
    url=url_home
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_home td.score")
    return scores
def home_team_awayscore(url_home):
    url=url_home
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_away td.score")
    return scores
def away_team_homescore(url_away):
    url=url_away
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_home td.score")
    return scores
def away_team_awayscore(url_away):
    url=url_away
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    scores = soup.select("#data_container div.data10_away td.score")
    return scores
def show_total_match(home_1st,home_2nd,home_3rd,home_4th,away_1st,away_2nd,away_3rd,away_4th,home_1sthalf,home_2ndhalf,\
           away_1sthalf,away_2ndhalf,total_1sthalf,total_2ndhalf,firstQwtr,secondQwtr,thirdQwtr,fourthQwtr,totalHome,\
           totalAway,totalMatch,\
           home_1st_22,home_2nd_23,home_3rd_24,home_4th_25,away_1st_26,away_2nd_27,away_3rd_28,away_4th_29,home_1sthalf_30,home_2ndhalf_31,\
           away_1sthalf_32,away_2ndhalf_33,total_1sthalf_34,total_2ndhalf_35,firstQwtr_36,secondQwtr_37,thirdQwtr_38,fourthQwtr_39,totalHome_40,\
           totalAway_41,totalMatch_42,\
           home_1st_43,home_2nd_44,home_3rd_45,home_4th_46,away_1st_47,away_2nd_48,away_3rd_49,away_4th_50,home_1sthalf_51,home_2ndhalf_52,\
           away_1sthalf_53,away_2ndhalf_54,total_1sthalf_55,total_2ndhalf_56,firstQwtr_57,secondQwtr_58,thirdQwtr_59,fourthQwtr_60,totalHome_61,\
           totalAway_62,totalMatch_63,\
           home_1st_64,home_2nd_65,home_3rd_66,home_4th_67,away_1st_68,away_2nd_69,away_3rd_70,away_4th_71,home_1sthalf_72,home_2ndhalf_73,\
           away_1sthalf_74,away_2ndhalf_75,total_1sthalf_76,total_2ndhalf_77,firstQwtr_78,secondQwtr_79,thirdQwtr_80,fourthQwtr_81,totalHome_82,\
           totalAway_83,totalMatch_84):
    print("     FOR HOME TEAM    ")
    max_ever_home=max(totalHome)+max(totalAway)
    min_ever_home=min(totalHome)+min(totalAway)
    print("PROBABLY: ",max_ever_home,min_ever_home)
    print("ACTUALLY: ",max(totalMatch),min(totalMatch))
    print("     FOR AWAY TEAM  ")
    max_ever_away=max(totalAway_83)+max(totalHome_82)
    min_ever_away=min(totalAway_83)+min(totalHome_82)
    print("PROBABLY: ",max_ever_away,min_ever_away)
    print("ACTUALLY: ",max(totalMatch_84),min(totalMatch_84))
    absolutely_max_total=max(max(totalHome),max(totalAway_41))\
                         +max(max(totalAway),max(totalHome_61))
    absolutely_min_total=min(min(totalHome),min(totalAway_41))\
                         +min(min(totalAway_83),min(totalHome_61))
    print("EXTREMUM: ",absolutely_max_total,absolutely_min_total)

def show_total_1st_half(home_1st,home_2nd,home_3rd,home_4th,away_1st,away_2nd,away_3rd,away_4th,home_1sthalf,home_2ndhalf,\
           away_1sthalf,away_2ndhalf,total_1sthalf,total_2ndhalf,firstQwtr,secondQwtr,thirdQwtr,fourthQwtr,totalHome,\
           totalAway,totalMatch,\
           home_1st_22,home_2nd_23,home_3rd_24,home_4th_25,away_1st_26,away_2nd_27,away_3rd_28,away_4th_29,home_1sthalf_30,home_2ndhalf_31,\
           away_1sthalf_32,away_2ndhalf_33,total_1sthalf_34,total_2ndhalf_35,firstQwtr_36,secondQwtr_37,thirdQwtr_38,fourthQwtr_39,totalHome_40,\
           totalAway_41,totalMatch_42,\
           home_1st_43,home_2nd_44,home_3rd_45,home_4th_46,away_1st_47,away_2nd_48,away_3rd_49,away_4th_50,home_1sthalf_51,home_2ndhalf_52,\
           away_1sthalf_53,away_2ndhalf_54,total_1sthalf_55,total_2ndhalf_56,firstQwtr_57,secondQwtr_58,thirdQwtr_59,fourthQwtr_60,totalHome_61,\
           totalAway_62,totalMatch_63,\
           home_1st_64,home_2nd_65,home_3rd_66,home_4th_67,away_1st_68,away_2nd_69,away_3rd_70,away_4th_71,home_1sthalf_72,home_2ndhalf_73,\
           away_1sthalf_74,away_2ndhalf_75,total_1sthalf_76,total_2ndhalf_77,firstQwtr_78,secondQwtr_79,thirdQwtr_80,fourthQwtr_81,totalHome_82,\
           totalAway_83,totalMatch_84):
    print("     FOR HOME TEAM (1ST HALF)   ")
    max_ever_home_1st_half=max(home_1sthalf)+max(away_1sthalf)
    min_ever_home_1st_half=min(home_1sthalf)+min(away_1sthalf)
    print("PROBABLY: ",max_ever_home_1st_half,min_ever_home_1st_half)
    print("ACTUALLY: ",max(total_1sthalf),min(total_1sthalf))
    print("     FOR AWAY TEAM  ")
    max_ever_away_1st_half=max(away_1sthalf_74)+max(home_1sthalf_72)
    min_ever_away_1st_half=min(away_1sthalf_74)+min(home_1sthalf_72)
    print("PROBABLY: ",max_ever_away_1st_half,min_ever_away_1st_half)
    print("ACTUALLY: ",max(total_1sthalf_76),min(total_1sthalf_76))
    # absolutely_max_total=max(max(totalHome),max(totalAway_41))\
    #                      +max(max(totalAway),max(totalHome_61))
    # absolutely_min_total=min(min(totalHome),min(totalAway_41))\
    #                      +min(min(totalAway_83),min(totalHome_61))
    # print("EXTREMUM: ",absolutely_max_total,absolutely_min_total)




show_total_match(
    *layout(cleaning(home_team_homescore(url_home))),
    *layout(cleaning(home_team_awayscore(url_home))),
    *layout(cleaning(away_team_homescore(url_away))),
    *layout(cleaning(away_team_awayscore(url_away)))
)
show_total_1st_half(
    *layout(cleaning(home_team_homescore(url_home))),
    *layout(cleaning(home_team_awayscore(url_home))),
    *layout(cleaning(away_team_homescore(url_away))),
    *layout(cleaning(away_team_awayscore(url_away)))
)




