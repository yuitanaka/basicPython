def displayListItem(list):
    for i in range(len(list)):
        print(list[i] , end = '')
        if(i == len(list) - 2):
            print(', and ', end = '')
        elif(i < len(list) - 1):
            print(', ', end = '')


spam = ['apples', 'bananas', 'tofu', 'cats']
displayListItem(spam)
