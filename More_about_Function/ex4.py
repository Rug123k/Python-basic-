# Caller class (when object name is acting like a funcation then it is called caller class_)

class Dept:                                   #          This line starts the definition of the Dept class.
    
    def __init__ (self):                      # __init__ Method: This special method is automatically called when a new instance of the Dept class is created.
        self.depts={'hr':'human resource',    #self.depts: Initializes an instance attribute depts with a dictionary that maps department codes to their respective names.
                    'R':'Rugved',
                    'k':'Kulkarni'
                   }
    def __call__ (self,dept):                 #__call__ Method: This special method allows an instance of the Dept class to be called like a function.
                                              #dept: A parameter for the department code you want to look up
        return self.depts[dept]               #self.depts[dept]: Retrieves the value associated with the key dept from the depts dictionary.        
        
d= Dept()                                     #Instance Creation: This line creates a new instance of the Dept class.
                                              #__init__ Method Call: The __init__ method is invoked to initialize the instance d. During this process, self.depts is set to the dictionary {'hr': 'human resource', 'R': 'Rugved', 'k': 'Kulkarni'}.

print(d('R'))                                 # Instance Call: The instance d is called like a function with 'R' as an argument.

                                              # __call__ Method Execution: When d('R') is called, Python internally invokes the __call__ method of the Dept class.
                                              # self.depts['R']: Inside the __call__ method, it looks up the value for the key 'R' in the self.depts dictionary.
                                              # Return Value: The __call__ method returns 'Rugved', which is the value associated with the key 'R' in the dictionary.