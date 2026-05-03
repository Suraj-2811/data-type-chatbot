data_types = {

    "int": {
        "definition": "Represents whole numbers without decimals.",

        "python": {
            "code": """
x = 10
y = 5
print(x + y)
print(x * y)
print(x - y)
print(x // y)
""",
            "output": """
15
50
5
2
""",
            "explanation": [
                "Creates integers",
                "Addition",
                "Multiplication",
                "Subtraction",
                "Integer division"
            ]
        },

        "java": {
            "code": """
int x = 10;
int y = 5;
System.out.println(x + y);
System.out.println(x * y);
System.out.println(x - y);
System.out.println(x / y);
""",
            "output": """
15
50
5
2
""",
            "explanation": [
                "Declares integers",
                "Performs addition",
                "Performs multiplication",
                "Performs subtraction",
                "Performs division"
            ]
        },

        "c": {
            "code": """
#include<stdio.h>
int main() {
    int x = 10, y = 5;
    printf("%d\\n", x + y);
    printf("%d\\n", x * y);
    printf("%d\\n", x - y);
    printf("%d\\n", x / y);
    return 0;
}
""",
            "output": """
15
50
5
2
""",
            "explanation": [
                "Declares integers",
                "Performs addition",
                "Performs multiplication",
                "Performs subtraction",
                "Performs division"
            ]
        }
    },

    "str": {
        "definition": "Sequence of characters.",

        "python": {
            "code": """
s = "hello"
print(s.upper())
print(len(s))
print(s[0])
""",
            "output": """
HELLO
5
h
""",
            "explanation": [
                "Creates string",
                "Converts to uppercase",
                "Gets length",
                "Accesses first character"
            ]
        },

        "java": {
            "code": """
String s = "hello";
System.out.println(s.toUpperCase());
System.out.println(s.length());
System.out.println(s.charAt(0));
""",
            "output": """
HELLO
5
h
""",
            "explanation": [
                "Creates string",
                "Converts to uppercase",
                "Gets length",
                "Accesses character"
            ]
        },

        "c": {
            "code": """
#include<stdio.h>
#include<string.h>
int main() {
    char s[] = "hello";
    printf("%d\\n", strlen(s));
    printf("%c\\n", s[0]);
    return 0;
}
""",
            "output": """
5
h
""",
            "explanation": [
                "Creates string",
                "Finds length",
                "Accesses first character"
            ]
        }
    },

    "list": {
        "definition": "Ordered, mutable collection.",

        "python": {
            "code": """
lst = [1,2,3]
lst.append(4)
print(lst)
""",
            "output": """
[1, 2, 3, 4]
""",
            "explanation": [
                "Creates list",
                "Appends value",
                "Prints list"
            ]
        },

        "java": {
            "code": """
import java.util.*;
public class Main {
 public static void main(String[] args){
  ArrayList<Integer> list = new ArrayList<>();
  list.add(1);
  list.add(2);
  list.add(3);
  list.add(4);
  System.out.println(list);
 }
}
""",
            "output": """
[1, 2, 3, 4]
""",
            "explanation": [
                "Creates ArrayList",
                "Adds elements",
                "Prints list"
            ]
        },

        "c": {
            "code": """
#include<stdio.h>
int main(){
 int arr[4]={1,2,3,4};
 for(int i=0;i<4;i++)
  printf("%d ",arr[i]);
 return 0;
}
""",
            "output": """
1 2 3 4
""",
            "explanation": [
                "Creates array",
                "Loops through elements",
                "Prints values"
            ]
        }
    },

    "bool": {
        "definition": "Represents True or False.",

        "python": {
            "code": """
x = True
y = False
print(x and y)
print(x or y)
""",
            "output": """
False
True
""",
            "explanation": [
                "Creates boolean values",
                "AND operation",
                "OR operation"
            ]
        },

        "java": {
            "code": """
boolean x = true;
boolean y = false;
System.out.println(x && y);
System.out.println(x || y);
""",
            "output": """
false
true
""",
            "explanation": [
                "Declares boolean",
                "AND operation",
                "OR operation"
            ]
        },

        "c": {
            "code": """
#include<stdio.h>
int main(){
 int x=1,y=0;
 printf("%d\\n",x&&y);
 printf("%d\\n",x||y);
 return 0;
}
""",
            "output": """
0
1
""",
            "explanation": [
                "Uses integers as boolean",
                "AND operation",
                "OR operation"
            ]
        }
    }
}


def get_full_info(dtype, lang):
    info = data_types.get(dtype)

    if not info:
        return "No data available", "", "", []

    definition = info["definition"]
    lang_data = info.get(lang, {})

    code = lang_data.get("code", "Code not available")
    output = lang_data.get("output", "N/A")
    explanation = lang_data.get("explanation", [])

    return definition, code, output, explanation