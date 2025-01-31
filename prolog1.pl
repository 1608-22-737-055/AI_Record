sunny.father(john,peter).
father(john,mary).
mother(susan,peter).


% Define facts
father(john, peter).
father(john, mary).
mother(susan, peter).
mother(mary, ann).

% Define rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X, Y) :- father(Z, X), father(Z, Y), X \= Y.
sibling(X, Y) :- mother(Z, X), mother(Z, Y), X \= Y.

% Querying
% ?- parent(john, peter). 
% true.

% ?- parent(susan, peter). 
% true.

% ?- sibling(peter, mary). 
% true.

% ?- sibling(peter, ann). 
% false.


# In this program:

# 1. We define facts about family relationships using the father and mother predicates.
# 2. We define rules using the parent and sibling predicates. The parent rule states that someone is a parent if they are either a father or a mother. 
# The sibling rule states that two people are siblings if they have the same father or mother and are not the same person.
# 3. We query the program using the ?- operator to ask questions like "Is John a parent of Peter?" or "Are Peter and Mary siblings?"

# This is a simple example of how Prolog can be used to represent knowledge and reason about it.