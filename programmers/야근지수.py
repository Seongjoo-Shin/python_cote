def solution(n, works):
  answer = 0
  works.sort(reverse=True)
  cnt=n
  while cnt:
    if works[0]==0:
      break
    for i in range(len(works)):
      if cnt==0 or works[0]>works[i]:
        break
      works[i]-=1
      cnt-=1

  for i in works:
    answer+=i*i

  return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))