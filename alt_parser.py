from re import findall
conf_matrix_file = open('conflict_matrix.txt', 'r')
conf_total = conf_matrix_file.read()
conf_sections = conf_total.split('Mountain')
conf_sections.remove(conf_sections[0])
course_dict = {}

for sect in conf_sections:
  my_tuple = findall(r'([A-Z]{2}\d{4}),(.+)\r\nCrs#       Title                             Requests,Crs#       Title                             Requests,Crs#       Title                            Requests([\s\S]+)', str(sect))
  course_dict[my_tuple[0][0]] = {}
  course_dict[my_tuple[0][0]]['Course_Title'] = my_tuple[0][1]
  # course_dict[my_tuple[0][0]]['Course_Conflicts'] = findall(r'([A-Z]{2}\d{4}),([\w: ]+),(\d+)', my_tuple[0][2])
  temp_course_confs = findall(r'([A-Z]{2}\d{4}),([\w: ]+),(\d+)', my_tuple[0][2])
  for i in range(len(temp_course_confs)):
    temp_course_confs[i] = {
      'course_id': temp_course_confs[i][0],
      'course_name': temp_course_confs[i][1],
      'conflicts': temp_course_confs[i][2]
    }
  course_dict[my_tuple[0][0]]['Course_Conflicts'] = {}
  for obj in temp_course_confs:
    course_dict[my_tuple[0][0]]['Course_Conflicts'][obj['course_id']] = {
      'Course_Title': obj['course_name'],
      'conflicts': obj['conflicts']
    }

import json

with open('best_conflict_archive.json', 'w') as conf_ar:
  json_string = json.dumps(course_dict)
  conf_ar.write(json_string)


conf_matrix_file.close()