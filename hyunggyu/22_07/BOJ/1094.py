def filt(score):
    x = int(score)
    y = [64,32,16,8,4,2,1]
    count = 0
    for i in y:
        if x >=i:
            x -= i
            count +=1
    return count

if __name__ == '__main__':
    print(filt(23))