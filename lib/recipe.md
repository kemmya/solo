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


class ChallengeTracking:
    def __init__(self):
        # Parameters => None
        # Returns => Nothing
        # Side effects: Empty list in new variable "learners" 
        pass # No code here yet
    def add_learner(self, name):
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
l = ChallengeTracking() 
l.learners # => []

# when names of learners are added
l = ChallengeTracking()   
l.add_learner("Kemi") # => ["Kemi"]

# when multiple names of learners are added
l = ChallengeTracking()
l.add_learner("Kemi")
l.add_learner("Reese")
l.add_learner("Oli")
l.list_learners()    # => ["Kemi", "Reese", "Oli"]




# To track learners who done the challenge
l = ChallengeTracking()   
l.track_learners("Kemi", "Reese", "Oli")    
l.list_learners(tracked)   # => ["Kemi", "Reese", "Oli"]


```

## Implement the behaviour

"""
When single name is added to list of learners that have done the challenge
"""
def test_single_name_added():

"""
When multiple name of learners is added to the list of learners that have done the challenge
"""
def test_multiple_names_added():

"""
When we track names of learners who have  done the challenge
That will give us the list of learners who have done the challenge
"""
def test_tracked_learners():

