for _ in range(int(input())):
    tea_goa_dict={}
    team,goal=map(str,input().split())
    tea_goa_dict[team]=int(goal)
    team,goal=map(str,input().split())
    tea_goa_dict[team]=int(goal)
    team,goal=map(str,input().split())
    tea_goa_dict[team]=int(goal)
    team,goal=map(str,input().split())
    tea_goa_dict[team]=int(goal)
    if(tea_goa_dict['RealMadrid']<tea_goa_dict['Malaga']):
        if(tea_goa_dict['Eibar']<tea_goa_dict['Barcelona']):
            print("Barcelona")
        else:
            print("RealMadrid")
    else:
        print("RealMadrid")
        