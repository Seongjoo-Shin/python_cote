from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
qry = list(map(int, input().split()))

ans = []
for q in qry:
  ll = bisect_left(cards, q)
  rr = bisect_right(cards, q)
  ans.append(1 if rr - ll else 0)
  # l = bisect_left(cards, q)
  # if cards[i] == q: 카드 존재

print(*ans)
# print(''.join(map(str, ans)))


# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.


# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다


# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

# 1 0 0 1 1 0 0 1
