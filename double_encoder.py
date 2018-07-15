### SYNTAX  --> double_encode(b'<your BASE64 string>') <-- ###
###for example, IF YOU WANT TO DOUBLE ENCODE '<script>':
#>>>     YOUR SYNTAX SHOULD BE: double_encode(b'<script>')     <<<#


import binascii
def double_encode(stri):
	hexin = binascii.hexlify(stri)
  hexin = str(hexin)[2:].upper()
	i=0
	ls=[]
	while(i < len(hexin)):
		if(i % 2==0):
			try:
				temp += str(hexin[i])
			except:
				temp = str(hexin[i])
		else:
			temp += str(hexin[i])
			ls.append(r'%25'+str(temp))
			temp=""
		i+=1
	return "".join(ls)
