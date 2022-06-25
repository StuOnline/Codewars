def points(games):
	score_count=0
	for item in games:
		score_data = item.split(':')
		score_dif = int(score_data[0]) - int(score_data[1])
		
		if score_dif > 0:
			score_count +=3
		elif score_dif == 0:
			score_count +=1




	print(score_count)
 	




points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2'])
