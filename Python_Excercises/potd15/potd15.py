        count=0
        s=0
        sum={0:1}
        for i in arr:
            s+=i
            if (s-tar) in sum:
                count+=sum[s-tar]
            elif s in sum:
                sum[s]+=1
            else:
                sum[s]=1
        return count
