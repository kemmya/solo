from lib.challenge_tracking import ChallengeTracking

"""
Initially there are no names of learners
"""
def test_initially_no_names_of_learners():
    l = ChallengeTracking() 
    assert l.learners == []

"""
When single name is added to list of learners that have done the challenge
"""
def test_single_name_added():
    l = ChallengeTracking()   
    assert l.add_learner("Kemi") == ["Kemi"]

"""
When multiple names of learners are added and we track the names of learners who have  done the challenge
That will give us the list of learners who have done the challenge
"""
def test_tracked_learners():
    l = ChallengeTracking()
    l.add_learner("Kemi")
    l.add_learner("Reese")
    l.add_learner("Oli")
    assert l.track_learners("Kemi" "Reese" "Oli") == ["Kemi" "Reese" "Oli"]
