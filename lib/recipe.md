# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a coach,
So I know which learners need encouraging to do the first challenge in Golden Square,
I need to keep track of learners who have done that challenge.



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python


class Student:
    def __init__(self):
        # Parameters => None
        # Returns => Nothing
        # Side effects: Empty list in new variable "learners" 
        pass # No code here yet
    def add_learner(self,name):
        # Parameters: name string
        # returns: names of learners
    def track_learners(self, name):
        # Parameters: name string
        # Returns: list of learners
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` 
# Initially there are no names of learners
s = Student() 
s.learners() # => []

# when names of learners are added
s = Student()   
s.learners_list.append(name)    


# => To know who done the challenge
s = Student()   
s.learners_list.append(name)   
s.learner_list() # => []
    if passed_learner in learner_list:         
        leaner_list.remove(passed_learner)  # => learner_list  


```

## Implement the behaviour

"""
When single name is added to list of learners that have the challenge
"""
def test_single_name_added():

"""
When multiple name is added to the list of learners that have done the challenge
"""
def test_multiple_names_added():

"""
When we remove names of learners who have not done the challenge
That will give us the list of learners who have done the challenge
"""
def test_remove_names_of_learners_not_done_challenge():

