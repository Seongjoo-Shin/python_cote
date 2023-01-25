import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rooms = []
status = [[False for i in range(9)] for i in range(50)]

for i in range(N):
	rooms.append(input().strip())
rooms.sort()

for _ in range(M):
	room, start, end = input().split()
	start, end = int(start) - 9, int(end) - 9
	for j in range(start, end):
		status[rooms.index(room)][j] = True

for i in range(N):
	print('Room %s:' % rooms[i])
	if False not in status[i]:
		print('Not available')
	else:
		k = 0
		available = []
		while k < 9:
			f, t = 0, 0
			if not status[i][k]:
				f = k
				while k < 9 and not status[i][k]:
					k += 1
				t = k - 1
				available.append([f, t])
				print(available)
			k += 1
		print(len(available), 'available:')
		for o in available:
			print('{}-{}'.format(format(o[0] + 9, '02'), format(o[1] + 10, '02')))
	if i != N - 1:
		print('-----')
	