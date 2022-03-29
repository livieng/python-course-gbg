# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

def movieTickets():
    tickets = int(input("Hur många biljetter vill du köpa? "))
    kids = int(input("Hur många är under 18 år? "))
    time = int(input("Viken föreställning (ange klockslag i hela timmar)? "))
    ticket_prize = 100
    kids_prize = 50
    total_prize = kids_prize * kids + ticket_prize * (tickets-kids)
    if time < 18:
        total_prize *= 0.90
    print("Biljetterna kostar sammanlagt " + str(total_prize) + " kr.")
# movieTickets()

# En körning:
# Hur många biljetter vill du köpa? 5
# Hur många är under 18 år? 3
# Viken föreställning (ange klockslag i hela timmar)? 17
# Biljetterna kostar sammanlagt 315.0 kr.

###############################################

def pepLineLength(filename):
    lines = open(filename)
    long_lines = 0
    line_number = 0

    for line in lines:
        line_number += 1
        if len(line) > 79:
            print("line " + str(line_number) + " too long: " + str(len(line))) 
            long_lines += 1

    print(str(long_lines) + " lines are too long")
    lines.close()
# pepLineLength('test')

# gjorde en textfil för att testa: "test"
# En körning med 'test':
# line 4 too long: 119
# line 5 too long: 113
# 2 lines are too long

#############################################
#%%
class Tree:
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees

    def getParts(self):
        return self.root, self.subtrees
    
royal = Tree('CarlGustav', [Tree('Victoria', [Tree('Estelle',[]), Tree('Oscar', [])]), Tree('CarlPhilip', [Tree('Alexander', [])]), Tree('Madeleine', [Tree('Leonore', []), Tree('Nicolas', [])])])
            
def preorder(tree):
    node, childs = tree.getParts()
    royalorder = [node]
    for i in childs:
        node2, childs2 = i.getParts()
        royalorder.append(node2)
        for j in childs2:
            node3, childs3 = j.getParts()
            royalorder.append(node3)
    return royalorder

print(preorder(royal)) #funkar!!

def postorder(tree):
    node, childs = tree.getParts()
    royalorder = []
    if len(childs) == 0:
        return node
        for child in childs:
            royalorder.extend(postorder(child))
        royalorder.append(node)
        print(royalorder)
print(postorder(royal))

# %%
