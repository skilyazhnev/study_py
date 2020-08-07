
# Эмулятор видимости пространства имён Py
#
#   Первым вводим количество команд N
#
#   create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
#   add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#   get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует


glob = {
    'global': {}
}

def search_ns_shell(name, dict):
	dos = []
    
	def search_ns(name, dick):

		if type(dick) is str:
			return 1
		if name in dick:
			return 0
		
		for i in dick:
			if search_ns(name, dick[i]) == 0:
				dos.append(i)
				return 0
		return 1
		
	search_ns(name, dict)

	return dos

def add_ns(name, parent, dick):
    path = search_ns_shell(parent, glob)
    path.reverse()
   
    path.append(parent)

    os = dick

    for i in path:
        os = os[i]
    os.update({name: {}})

def add_var(name, parent, dick):
    path = search_ns_shell(parent, glob) 
    path.reverse()
 
    path.append(parent)
        
    os = dick
        
    for i in path:
        os = os[i]
    os.update({name: ''})

def get_ns(name, parent, dick):
    path = search_ns_shell(parent, glob) 
    path.reverse()
    
    #if len(path)!=0:
    path.append(parent)

    links = []
    names = []
    os = dick

    for i in path:
        links.append(os)
        os = os[i]
        names.append(i)
    links.append(os)

    for s in range(len(links)-1,0,-1):
       # print(name, links[s])
        if name in links[s]:
            return str(names[s-1])
    return 'None'
def main():
    n = int(input())
    
    otvet = []
    
    for i in range(n):
        cmd, namesp, arg = input().split()

        if cmd == 'create': 
            add_ns(namesp, arg, glob)

        if cmd == 'add': 
            add_var(arg, namesp, glob)

        if cmd == 'get': 
            otvet.append(get_ns(arg, namesp, glob))
    print('\n'.join(otvet))
main()
