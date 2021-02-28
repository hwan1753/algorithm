def solution(genres, plays):
    song_dict = {}
    num_dict = {}
    for idx in range(len(genres)):
        if genres[idx] not in song_dict:
            song_dict[genres[idx]] = [idx]
            num_dict[idx] = plays[idx]
        else:
            stop = False
            for item in range(len(song_dict[genres[idx]])):
                if plays[idx] > num_dict[song_dict[genres[idx]][item]]:
                    song_dict[genres[idx]].insert(item,idx)
                    stop = True
                    break
            if stop == False:
                song_dict[genres[idx]].append(idx)

            # song_dict[genres[idx]].append(idx)
            num_dict[idx] = plays[idx]
    print(song_dict)
    print(num_dict)
    chk = []
    for key, item in song_dict.items():
        total = 0
        for value in item:
            total += num_dict[value]
        chk.append([total,key])
    chk.sort()
    result = []
    for ord in range(len(chk)-1,-1,-1):
        if len(song_dict[chk[ord][1]]) < 3:
            for res in range(len(song_dict[chk[ord][1]])):
                result.append(song_dict[chk[ord][1]][res])
        else:
            for res in range(2):
                result.append(song_dict[chk[ord][1]][res])
    # print(result)
    return result

a = ["classic", "pop", "classic", "classic", "pop","dance"]
b = [500, 600, 150, 800, 2500,1000]

solution(a,b)
