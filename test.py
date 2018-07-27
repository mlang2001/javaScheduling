import json
file = json.load(open('best_conflict_archive.json'))
print(file['BC3010']['Course_Conflicts']['BC2030']['conflicts'])