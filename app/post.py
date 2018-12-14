from facepy import GraphAPI

def post () :
	token = 'EAAD8B9lvyRABAHjCqkvsmJT4PIZCKqJBMRgGiG8Pzif91PcZAKz9EA6QB7RbBCjLAbQmjzlcCEB1gSXI6CPoMBSmqktNr76r5uzKw1tNQREEAFO9GubrCWV6GNdUiaMa7uYmFCDOzZC3RuRidFwWa6aN8k1PASdOPYjhhDuK2iAqVKbaeT3SPLfb3qEZBzLZCG5sgW7azQAZDZD'
	#sempre atualizar o token de acesso
	graph = GraphAPI(token)

	post = graph.get('me/posts')

	quase = post['data']

	li = []
	lin = []
	for i in quase:
	    li.append(i)
	

	for j in range(len(li)):
	    po = ""
	    if 'message' in li[j]:
	        po = li[j]
	        lin.append(po)
	        
	u = graph.get('me')
	usuario = u['name']
	ids = u['id']

	return lin,usuario,ids