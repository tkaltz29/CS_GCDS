import random

# Lists for the menu items, prices, and flairs
mains = ["Wagyu Beef", "Unagi Kabayaki", "Pork Tonkatsu", "Sake Salmon", "Vegetable Tempura", "Miso Eggplant", "Bluefin Tuna", "Chicken Karaage", "Hokkaido Scallops"]
prices = [50, 35, 22, 28, 18, 15, 45, 20, 32] # prices match mains by index
flairs = ["with Wasabi Crema", "over Ginger Rice", "with Shiso Leaf", "with Yuzu Glaze", "with Daikon Oroshi", "with Sweet Miso", "with Aged Soy", "with Kewpie Mayo", "with Pickled Plum"]

print("  WELCOME TO THE JAPANESE FOOD-O-MATIC  ")


try:
    num_items = int(input("How many items would you like to generate? ")) # get how many dishes to generate
    
    total_cost = 0 # keeps a running total
    print("\n--- TODAY'S SPECIAL MENU ---")

    for i in range(num_items):
       
        m_index = random.randint(0, len(mains) - 1) # pick a random main
        f_index = random.randint(0, len(flairs) - 1) # pick a random flair (independent of main)
        
        dish_name = mains[m_index] # grab the main name
        dish_flair = flairs[f_index] # grab the flair
        dish_price = prices[m_index] # price is tied to the main, not the flair
        
        print(f"{i + 1}. {dish_name} {dish_flair} - ${dish_price}") # print the dish
        
        total_cost += dish_price # add to total

    print("-" * 30)
    print(f"TOTAL ORDER COST: ${total_cost}")
    print("Gochisousama deshita! (Thank you for the meal!)")

except ValueError:
    print("Oops! Please enter a whole number.") # runs if user types something that isn't a number