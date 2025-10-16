from google.adk.agents import Agent

user_history = [
    {"product": "Bluetooth headphones", "category": "electronics", "price": 120},
    {"product": "Running shoes", "category": "sportswear", "price": 80}
]

products = [
    {"product": "Laptop", "category": "Electronics", "price": 1200},
    {"product": "Smartphone", "category": "Electronics", "price": 799},
    {"product": "Smartwatch", "category": "Electronics", "price": 350},
    {"product": "Tablet", "category": "Electronics", "price": 450},
    {"product": "Bluetooth headphones", "category": "electronics", "price": 120},

    {"product": "Coffee Maker", "category": "Home Appliances", "price": 85},
    {"product": "Blender", "category": "Home Appliances", "price": 110},
    {"product": "Microwave Oven", "category": "Home Appliances", "price": 200},
    {"product": "Toaster", "category": "Home Appliances", "price": 40},

    {"product": "Jeans", "category": "Apparel", "price": 65},
    {"product": "Hoodie", "category": "Apparel", "price": 55},
    {"product": "T-shirt", "category": "Apparel", "price": 25},
    {"product": "Sneakers", "category": "Apparel", "price": 90},

    {"product": "Fantasy Novel", "category": "Books", "price": 20},
    {"product": "Cookbook", "category": "Books", "price": 35},
    {"product": "Biography", "category": "Books", "price": 28},
    {"product": "Sci-Fi Novel", "category": "Books", "price": 22},

    {"product": "Yoga Mat", "category": "Sportswear", "price": 30},
    {"product": "Dumbbell Set", "category": "Sportswear", "price": 150},
    {"product": "Running Shoes", "category": "Sportswear", "price": 80},
    {"product": "Water Bottle", "category": "Sportswear", "price": 15},

    {"product": "Desk Chair", "category": "Furniture", "price": 250},
    {"product": "Bookshelf", "category": "Furniture", "price": 180},
    {"product": "Coffee Table", "category": "Furniture", "price": 220},
    {"product": "Bed Frame", "category": "Furniture", "price": 400},

    {"product": "Face Cream", "category": "Beauty", "price": 45},
    {"product": "Sunscreen", "category": "Beauty", "price": 18},
    {"product": "Shampoo", "category": "Beauty", "price": 12},
    {"product": "Lipstick", "category": "Beauty", "price": 24},

    {"product": "Board Game", "category": "Toys", "price": 40},
    {"product": "Action Figure", "category": "Toys", "price": 25},
    {"product": "LEGO Set", "category": "Toys", "price": 75},
    {"product": "Puzzle", "category": "Toys", "price": 18},

    {"product": "Dog Leash", "category": "Pet Supplies", "price": 15},
    {"product": "Cat Food", "category": "Pet Supplies", "price": 50},
    {"product": "Fish Tank", "category": "Pet Supplies", "price": 100},
    {"product": "Cat Tree", "category": "Pet Supplies", "price": 130},

    {"product": "Milk", "category": "Groceries", "price": 4},
    {"product": "Bread", "category": "Groceries", "price": 3},
    {"product": "Eggs", "category": "Groceries", "price": 5},
    {"product": "Apples", "category": "Groceries", "price": 6}
]


def get_user_history() -> dict:
    """
    show user history for all products
    Returns: user_history (dict)

    """
    return {"user_history": user_history}


def buy_new_product(new_product: dict) -> dict:
    """
    Buy a new product and add it to the buy history
    Args:
        new_product (dict): the product that the user wants to buy

    Returns: user_history (dict)

    """

    user_history.append(new_product)
    return {"user_history": user_history}


def get_products() -> dict:
    """
    Get all products
    Returns: products (dict)

    """
    return {"products": products}


recommend_agent = Agent(
    name="recommend_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to recommend products to a customer based on his buy history."
    ),
    instruction=(
        """
        You are a helpful agent who recommend a new category from the products ypu can get from tool get_products
        based on the user history from tool get_user_history then mention why you recommend this category.
        from this category recommend the top 3 products that fit the user
        then Rank them based on user’s price range or inferred preferences.
        """
    ),
    tools=[get_user_history, get_products]
)

buy_agent = Agent(
    name="buy_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to buy a new product or show the buy history of the customer or show all the products."
    ),
    instruction=(
        "You are a helpful agent who can show the user all the products or the buy history or buy new product."
    ),
    tools=[get_user_history, get_products, buy_new_product]
)

root_agent = Agent(
    name="recommend_buy_root_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to buy or recommend products or show buy history"
    ),
    instruction=(
        "You are the root agent who have access to these two agents: buy_agent and recommend_agent"
    ),
    sub_agents=[recommend_agent, buy_agent]
)
