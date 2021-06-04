in_rubric = False


with open('survey.rst') as fp:
    for cnt, line in enumerate(fp):
       #print("Line {}: {}".format(cnt, line))

       if line == "+-----------------------------------------------------------------------+\n" and not in_rubric:
         in_rubric = True
       elif in_rubric and line.startswith('| .. rubric:: '):
         #line = ".. container:: "+line[14:-2]
         print(".. container:: question")
       elif in_rubric and line.startswith('|    :'):
         line = line[2:-2]
         #print(line)
       elif line == "+-----------------------------------------------------------------------+\n" and in_rubric:
         in_rubric = False
       # Default last   
       elif in_rubric:
         line = "   "+line[2:-2]
         print(line)
       elif not in_rubric:
         print(line, end="")
         