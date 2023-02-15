def solution(args):
    args.append(float("inf"))
    i = args[0]
    result = []
    for j, n in zip(args, args[1:]):
        if n - j > 1:
            result.append(str(i) 
                          if i == j 
                          else f"{i}{'-' if j - i > 1 else ','}{j}")
            i = n
    return ",".join(result)
#
print (f"{solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])}")