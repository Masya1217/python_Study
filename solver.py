# coding=utf-8 

####課題####
# N本の長さの異なる棒を3本組み合わせて，
# 長さLにする組み合わせの数を数え上げるプログラムを作成してください．

#- 入力
#1行目に，作成する棒の長さL
print u"これはN本の長さの異なる棒を3本組み合わせて，"
print u"長さLにする組み合わせの数を数え上げるプログラムです"
print u""

print "ターゲットとなる長さLを入力してください。"
target_sum = int(raw_input())

#2行目に，棒の数N
print "組み合わせに使える棒の数Nを入力してください。"
stickNum = int(raw_input())

#3行目からN+2行目に，各棒の長さ
print "各棒の長さを入力してください。"
stick_list = []
for num in xrange(stickNum):
	stick_list.append(int(raw_input())) 

#組み合わせの数を入れるカウンター
gCounter = 0

def solve(stick_list, target_sum, tCounter=0, i=0, sum=0):
	global gCounter
	if i == len(stick_list):
		if tCounter == 3:
			return sum == target_sum
		else:
			return False
	if (solve(stick_list, target_sum, tCounter, i + 1, sum)):
		gCounter = gCounter + 1
	if (solve(stick_list, target_sum, tCounter + 1, i + 1, sum + stick_list[i])):
		gCounter = gCounter + 1

print "検索を開始します！"
print "I'm thinking...Umm..."
solve(stick_list, target_sum)
print "組み合わせの数は『" + str(gCounter) + "』でした(^o^b"
