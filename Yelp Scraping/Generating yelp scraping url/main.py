main_url = input("What is the link:  ")
page_number = int(input("How much page:  "))




# Generating yelp link
main_url = input("What is the link:  ")
page_number = int(input("How much page:  "))

page = page_number * 10


for x in range(0, page, 10):
    gen_url = f'{main_url}&start={x}'
    print("'" + gen_url + "',")