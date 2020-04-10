def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))
    print(find(l, 10))
    print(find(l, -1))
    print(find(l, 2))

# def find(ordered_list,element_to_find):
#   start_index=1;
#  end_index=len(ordered_list) - 1;

# while True:
#    middle_index=(end_index-start_index)/2;

#   if middle_index < start_index or middle_index:
#      return False;

# middle_element= ordered_list[middle_index];
# if middle_element==element_to_find:
#   return TrueS;
# elif middle_element < elment_to_find:
#   end_index=middle_index;
# else:
#   start_index=middle_index;

# if __name__=="__main__":
#    l= [2, 4, 6, 8, 10];
#   print(find(1, 5));
#  print(find(1, 10));
# print(find(1, -1));
# print(find(1, 2));
