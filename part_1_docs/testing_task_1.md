### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # should use the == (not =) operator to test a value is equal to another.
    if card.value = 1:
      return True
    # missing :
    else
      return False
   
# should use def not dif to define a function
# coma missing between card1 and card2
  dif highest_card(self, card1 card2):
  # bad indentation
  if card1.value > card2.value:
    # card parameter does not exist should be card1
    return card
  else:
    return card2
  

# not indented correctly
# cards is not defined - need to define first - would be better to phrase as card1, card2 then define a cards list that includes these two.
def cards_total(self, cards):
  # total is not defined should be total = 0.
  total
  for card in cards:
    total += card.value
    # badly indented and bad concatenation cause not two strings - use f""
    return "You have a total of" + total
  
```
