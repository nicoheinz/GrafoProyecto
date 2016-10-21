#editando
#Hello

class Cola:
    def __init__(self):
        self.items = []

    def Vacia(self):
        return self.items == []

    def Encolar(self, item):
        self.items.insert(0,item)

    def Desencolar(self):
        return self.items.pop()

    def Tamano(self):
        return len(self.items)

class Nodo():
    def __init__(self,valor):
        self.key=valor
        self.color= None
        self.ancestro= None
        self.distancia=None
        self.tiempof=0

class Grafo():
    def __init__(self):
        self.lista={}
        self.Nodos={}
        self.Aristas={}

    def CrearLista(self):
        for x in self.Nodos :
            self.lista[x]=[]
        for (x,j) in self.Aristas :
            self.lista[x].append(j)

    def BFS(self, ini):
        for x in self.Nodos :
            x.color= "Blanco"
            x.ancestro= None
            x.distancia=None
        ini.color="Gris"
        ini.distancia= 0
        cola=Cola()
        cola.Encolar(ini)
        while(cola.Vacia() is False):
            b=cola.Desencolar()
            for (u,v) in self.Aristas:
                if(b is u):
                    if(v.color == "Blanco"):
                        v.ancestro = b
                        v.color = "Gris"
                        v.distancia = b.distancia + 1
                        cola.Encolar(v)
            b.color= "Negro"
            
    def VisitaDFS(self,u,tiempo1):
        u.distancia= tiempo1
        u.color= "Gris"
        for v in self.lista[u] :  
             if (v.color == "Blanco"):
               v.ancestro=u
               self.VisitaDFS(v,tiempo1+1)
        u.color= "Negro"
        u.tiempof=tiempo1+1


    def DFS(self):
        for u in self.Nodos :
            u.color= "Blanco"
            u.ancestro= None
        tiempo=0
        for u in self.Nodos :
           if (u.color== "Blanco"):
                self.VisitaDFS(u,tiempo+1)
      
if __name__ == '__main__':
    g=Grafo()
    z=Nodo(0)
    a=Nodo(1)
    b=Nodo(2)
    c=Nodo(3)
    d=Nodo(4)
    e=Nodo(5)
    f=Nodo(6)
    h=Nodo(7)
    g.Nodos=[z,a,b,c,d,e,f,h]
    ##g.Aristas=[(c,e),(e,h),(e,a),(a,f),(f,b),(b,f),(f,h),(b,d),(c,h),(z,d),(f,e)]
    ##g.Aristas=[(b,d),(b,e),(d,f),(b,z),(b,a)]
    g.CrearLista()
    print("B  F  S")
    g.BFS(b)
##    print(b.distancia,b.key,b.color,b.ancestro)
##    print(e.distancia,e.key,e.color,e.ancestro)
##    print(f.distancia,f.key,f.color,f.ancestro)
##    print(d.distancia,d.key,d.color,d.ancestro)
##    print(z.distancia,z.key,z.color,z.ancestro)
##    print(a.distancia,a.key,a.color,a.ancestro)
##    print(h.distancia,h.key,h.color,h.ancestro)
    
    print("D  F	 S")
    g.DFS()
    print(c.distancia,c.tiempof,c.key,c.color,c.ancestro)
    print(e.distancia,e.tiempof,e.key,e.color,e.ancestro.key)
    print(h.distancia,h.tiempof,h.key,h.color,h.ancestro.key)
    print(a.distancia,a.tiempof,a.key,a.color,a.ancestro)
    print(f.distancia,f.tiempof,f.key,f.color,f.ancestro.key)
    print(b.distancia,b.tiempof,b.key,b.color,b.ancestro.key)
    print(d.distancia,d.tiempof,d.key,d.color,d.ancestro.key)
    print(z.distancia,z.tiempof,z.key,z.color,z.ancestro)
    
    
   
