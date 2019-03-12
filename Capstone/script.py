from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
trie = Trie()
for food_type in types:
  trie.insert(food_type)

#Write code to insert restaurant data into a data structure here. The data is in data.py
hashmap = HashMap(len(types))
for food_type in types:
  linkedlist = LinkedList()
  for restaurant in restaurant_data:
    if food_type == restaurant[0]:
      linkedlist.insert_beginning(restaurant)
      hashmap.assign(food_type, linkedlist)

#Write code for user interaction here
while True:
    user_input = str(input("\nSearch for a food type here. \nType 'quit' anytime to exit.\n")).lower()
    if user_input == 'quit':
      exit()
    #Search for user_input in food types data structure here
    if len(trie.find_words(user_input)) < 1:
      print('No food types found. Try again')
    else:
      if len(trie.find_words(user_input)) > 1:
    	  print("Your choices are: {}".format(trie.find_words(user_input)))
      else:
        user_input_select = str(input("\nThe closest search result is: {}\n Would you like to look at this type? \n 'y' for yes or 'n' for no.\nType 'quit' to exit.\n".format(trie.find_words(user_input)[0]))).lower()
        if user_input_select == 'y':
          ll = hashmap.retrieve(trie.find_words(user_input)[0])
          head_node = ll.get_head_node()
          while head_node.value != None:
            print("\n Name: {0} \n Price: {1} \n Rating: {2} \n Address: {3} \n".format(head_node.value[1], head_node.value[2], head_node.value[3], head_node.value[4]))
            head_node = head_node.get_next_node()
        elif user_input_select == 'quit':
          exit()