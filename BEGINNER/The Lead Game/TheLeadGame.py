def game():
    num = int(input(""))
    p1_score = 0
    p2_score = 0
    lead = 0
    for _ in range(num):
        score1, score2 = map(int, input().split())
        p1_score = p1_score + score1
        p2_score = p2_score +score2
        diff = p1_score - p2_score
        
        if diff > 0 and diff > lead:
            lead = diff
            leader = 1 
        elif diff < 0 and abs(diff) > lead:
            lead = abs(diff)
            leader = 2 
    print(leader, lead)
    
game()
