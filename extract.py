import ijson
import sys
import os
try:

#Get input and output file location from command line
    path_input = sys.argv[1]
    path_output = sys.argv[2]

#open input and output file
    f = open(path_input)	
    file1 = open(path_output,"a")
	


#Extract ‘data’ array elements from json
    for item in ijson.items(f, "data.item"):
        print(item)
        file1.write('{')		
		#write in output file
        for key, value in item.items():		
            if(list(item.keys())[-1]==key):
			#last key in element 
                file1.write("”"+key+"”"+":"+"”"+value+"”")	
            else:
                file1.write("”"+key+"”"+":"+"”"+value+"”"+",")				
        file1.write('}\n') 		
		
		
    file1.close() 		
#close file



except Exception as e:
    print(e)

