from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, HTML
InteractiveShell.ast_node_interactivity = "all"    # so that all lines printed
from sympy import FiniteSet
from utils.sage_logic import *
import re

TODO = ""

######

javascr_string = """
function ueberpruefen(property) {
var solutions = 
{'kapitel2_1_0': 'RGllIEZsYXNjaGUgaXN0IG5pY2h0IHZvbGwu', 'kapitel2_1_1': 'RGllIEhvc2UgaXN0IG5pY2h0IHNjaHdhcnou', 'kapitel2_2_0': 'RXIgbWFnIGtlaW5lbiBTY2huYXBzIG9kZXIgZXIgbWFnIFNla3Qu', 'kapitel2_2_1': 'U2llIHRhbnp0IG5pY2h0IG9kZXIgZsOkaHJ0IG5pY2h0IFJhZC4=', 'kapitel2_3_0': 'SmE=', 'kapitel2_3_1': 'SmE=', 'kapitel2_3_2': 'SmE=', 'kapitel2_3_3': 'TmVpbg==', 'kapitel2_3_4': 'SmE=', 'kapitel2_3_5': 'TmVpbg==', 'kapitel2_3_6': 'SmE=', 'kapitel2_3_7': 'TmVpbg==', 'kapitel2_4_0': 'QXVzc2FnZWZvcm0=', 'kapitel2_4_1': 'QXVzc2FnZWZvcm0=', 'kapitel2_4_2': 'QXVzc2FnZWZvcm0=', 'kapitel2_4_3': 'V2VkZXIgQXVzc2FnZSBub2NoIEF1c3NhZ2Vmb3Jt', 'kapitel2_4_4': 'QXVzc2FnZQ==', 'kapitel2_4_5': 'QXVzc2FnZQ==', 'kapitel2_4_6': 'V2VkZXIgQXVzc2FnZSBub2NoIEF1c3NhZ2Vmb3Jt', 'kapitel2_4_7': 'QXVzc2FnZQ==', 'kapitel2_5_0': 'ZW50d2VkZXItb2Rlcg==', 'kapitel2_5_1': 'ZW50d2VkZXItb2Rlcg==', 'kapitel2_5_2': 'bG9naXNjaGVzIG9kZXI=', 'kapitel2_5_3': 'ZW50d2VkZXItb2Rlcg==', 'kapitel2_6_0': 'd2Focg==', 'kapitel2_6_1': 'ZmFsc2No', 'kapitel2_6_2': 'd2Focg==', 'kapitel2_6_3': 'ZmFsc2No', 'kapitel2_7_0': 'QXVmesOkaGx1bmcgdm9uIEdlZ2Vuc3TDpG5kZW4=', 'kapitel2_7_1': 'bG9naXNjaGUgS29uanVua3Rpb24=', 'kapitel2_7_2': 'bG9naXNjaGUgS29uanVua3Rpb24=', 'kapitel2_7_3': 'QXVmesOkaGx1bmcgdm9uIEdlZ2Vuc3TDpG5kZW4=', 'kapitel3_1_0': 'RGVmaW5pdGlvbg==', 'kapitel3_1_1': 'VGhlb3JlbQ==', 'kapitel3_1_2': 'RGVmaW5pdGlvbg==', 'kapitel3_1_3': 'VGhlb3JlbQ==', 'kapitel3_1_4': 'RGVmaW5pdGlvbg==', 'kapitel3_1_5': 'VGhlb3JlbQ==', 'kapitel3_2_0': 'QSDihpIgQg==', 'kapitel3_2_1': 'QSDihpAgQg==', 'kapitel3_2_2': 'QSDih5IgQg==', 'kapitel3_2_3': 'QSDih5IgQg==', 'kapitel3_2_4': 'QSDihpAgQg==', 'kapitel3_2_5': 'QSDih5QgQg==', 'kapitel3_3_0': 'a29tbXV0YXRpdg==', 'kapitel3_3_1': 'bmljaHQga29tbXV0YXRpdg==', 'kapitel3_3_2': 'bmljaHQga29tbXV0YXRpdg==', 'kapitel3_3_3': 'bmljaHQga29tbXV0YXRpdg==', 'kapitel3_4_0': 'bmV1dHJhbGVzIEVsZW1lbnQ=', 'kapitel3_4_1': 'a2VpbiBuZXV0cmFsZXMgRWxlbWVudA==', 'kapitel3_4_2': 'a2VpbiBuZXV0cmFsZXMgRWxlbWVudA==', 'kapitel3_4_3': 'bmV1dHJhbGVzIEVsZW1lbnQ=', 'kapitel3_4_4': 'bmV1dHJhbGVzIEVsZW1lbnQ=', 'kapitel3_4_5': 'a2VpbiBuZXV0cmFsZXMgRWxlbWVudA==', 'kapitel3_4_6': 'a2VpbiBuZXV0cmFsZXMgRWxlbWVudA==', 'kapitel3_4_7': 'bmV1dHJhbGVzIEVsZW1lbnQ='}

   form_elements = document.querySelector("#"+property).elements;
   for (i = 0; i < form_elements.length ;i++) {
      var answer = "<font size=5 color='red'>&#10007;</font>";
      if (typeof solutions[form_elements[i].id] !== 'undefined') {
         if (form_elements[i].value == 
             decodeURIComponent(escape(atob(solutions[form_elements[i].id] )))) {
             answer = "<font size=5 color='green'>&#10003;</font>";
         }
      document.querySelector("#" + form_elements[i].id + "_ans").innerHTML=answer;
      }
   }
}
"""

display(HTML('<script type="text/javascript">'+ javascr_string +'</script>'))

###### adding an operator for subjunction:  True -s>> False

class Infix:
    def __init__(self, function):
        self.function = function
    def __rsub__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

s=Infix(lambda x,y: x <= y)

###### printing a truthtable (using sage_logic)

def printtable (exprs):
  exprs = re.sub (r"and","&",exprs)
  exprs = re.sub (r"or","|",exprs)
  exprs = re.sub (r"not","!",exprs)
  exprs = re.sub (r"\-s>>","->",exprs)
  exprs = re.sub (r"<=","->",exprs)
  exprs = re.sub (r"==","<->",exprs)
  try:
     log = SymbolicLogic()
     log.print_table(log.truthtable(log.statement(exprs)))
  except:
     return "malformed formula"
    
########## solutions

def pruefe (exercise,myList):
   solutions = {"t_34_1": FiniteSet(*[x for x in range(0,51) if x % 2 == 0]), 
                "t_34_2": FiniteSet(*[x*y for x in range(0,6) for y in range(0,6) if x % 2 == 0  and y % 2 == 1]),
                "t_34_3": FiniteSet(*[x for x in range(0,51) if x % 2 == 0]) + FiniteSet("Text",FiniteSet(1,2))}

   if exercise == "tutorial 3.4":
       print ("gerade:", myList[0] == solutions["t_34_1"])
       print ("produkte:", myList[1] == solutions["t_34_2"])
       print ("vielfalt:", myList[2] == solutions["t_34_3"])

######### Woche 11

restklasse2 = { x for x in range (-5,6) if x % 3 == 0}
restklasse1 = { x for x in range (-5,6) if x % 3 == 2}
restklasse3 = { x for x in range (-5,6) if x % 3 == 1}
Anzahl_Elemente_in_Z3 = 3

def multInv(n,k):
    return pow(n,-1,k)

def addInv(n,k):
    return -n%k


