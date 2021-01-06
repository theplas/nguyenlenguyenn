import random
nh1 = []
nh2 = []
for i in range(1):
    nh1.append(random.randrange(50,1000))
    print('so ngau nhien tu 50 den 1000 la',nh1[i])
    nh2.append(random.randrange(-1000,1000))
    print('so ngau nhien tu -1000 den 1000 la',nh2[i])
    nh2.append(random.randrange(-1000.0,1000.0))
    print('so ngau nhien tu -1000.0 den 1000.0 la',nh2[i])
    # Bài mà sai thầy nói em em chỉnh lại nha thầy! TT