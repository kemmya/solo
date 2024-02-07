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


class Result:
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
r = Result()
r.learners # => []

self.name = name          # => when names of learners are added
self.learners.append(name)

if learner not in learner_list:      # => To know that learner name has been added to list
learner_list.append(learner)        
return learner_list


if learner in learner_list:         # => To know who passed the challenge
leaner_list.remove(learner)
return learner_list 


```

## Implement the behaviour

