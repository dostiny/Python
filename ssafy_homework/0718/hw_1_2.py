score = {'python':80, 'django':89, 'web':83}

score['algorithm'] = 90
score['python'] = 85
total_score = sum(score.values())
subject = len(score)

print(total_score/subject)