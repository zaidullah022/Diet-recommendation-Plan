from flask import Flask, render_template, request

app = Flask(__name__)

# Sample meal data
meals = {
    'vegetarian': {
        'maintain': {
            'weight <= 60': {
                'breakfast': 'Oatmeal with almond butter and banana (400 kcal)',
                'lunch': 'Grilled vegetable wrap with hummus (600 kcal)',
                'dinner': 'Vegetable curry with brown rice (500 kcal)',
                'snack': 'Mixed nuts and dried fruits (200 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Avocado toast with scrambled eggs (500 kcal)',
                'lunch': 'Quinoa bowl with chickpeas and vegetables (700 kcal)',
                'dinner': 'Grilled tofu with roasted vegetables (600 kcal)',
                'snack': 'Greek yogurt with granola (300 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Smoothie with spinach, banana, and protein powder (600 kcal)',
                'lunch': 'Vegetarian pasta with garlic bread (800 kcal)',
                'dinner': 'Lentil stew with mashed potatoes (700 kcal)',
                'snack': 'Trail mix with seeds (400 kcal)'
            }
        },
        'weight loss': {
            'weight <= 60': {
                'breakfast': 'Vegetable smoothie with chia seeds (300 kcal)',
                'lunch': 'Lentil salad with olive oil dressing (400 kcal)',
                'dinner': 'Steamed vegetables with tofu (400 kcal)',
                'snack': 'Carrot sticks with hummus (150 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Boiled eggs with avocado slices (350 kcal)',
                'lunch': 'Vegetable stir-fry with quinoa (500 kcal)',
                'dinner': 'Grilled mushrooms with side salad (400 kcal)',
                'snack': 'Low-fat yogurt with fruit (200 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Oatmeal with almond milk and berries (400 kcal)',
                'lunch': 'Vegetable curry with half a portion of rice (500 kcal)',
                'dinner': 'Roasted eggplant with chickpeas (400 kcal)',
                'snack': 'Apple slices with peanut butter (150 kcal)'
            }
        },
        'muscle gain': {
            'weight <= 60': {
                'breakfast': 'Protein pancakes with berries (500 kcal)',
                'lunch': 'Quinoa and lentil curry (700 kcal)',
                'dinner': 'Stir-fried tofu with rice (600 kcal)',
                'snack': 'Protein bar and almonds (300 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Chickpea and avocado toast (600 kcal)',
                'lunch': 'Vegetarian lasagna with greens (800 kcal)',
                'dinner': 'Grilled tofu with sweet potato (700 kcal)',
                'snack': 'Smoothie with whey protein (350 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Omelette with toast and vegetables (700 kcal)',
                'lunch': 'Vegetarian curry with rice and naan (900 kcal)',
                'dinner': 'Mushroom risotto with salad (800 kcal)',
                'snack': 'Trail mix with dried fruits (400 kcal)'
            }
        }
    },
    'non-vegetarian': {
        'maintain': {
            'weight <= 60': {
                'breakfast': 'Scrambled eggs with avocado toast (400 kcal)',
                'lunch': 'Grilled chicken breast with quinoa and vegetables (600 kcal)',
                'dinner': 'Steamed fish with spinach (500 kcal)',
                'snack': 'Boiled eggs with nuts (200 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Omelette with whole-grain toast (500 kcal)',
                'lunch': 'Turkey sandwich with mixed greens (700 kcal)',
                'dinner': 'Baked salmon with broccoli (600 kcal)',
                'snack': 'Greek yogurt with honey (300 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Protein pancakes with maple syrup (600 kcal)',
                'lunch': 'Grilled steak with mashed potatoes (800 kcal)',
                'dinner': 'Chicken curry with rice and naan (700 kcal)',
                'snack': 'Trail mix with nuts (400 kcal)'
            }
        },
        'weight loss': {
            'weight <= 60': {
                'breakfast': 'Boiled eggs and avocado slices (300 kcal)',
                'lunch': 'Grilled chicken salad with olive oil dressing (400 kcal)',
                'dinner': 'Baked fish with steamed broccoli (400 kcal)',
                'snack': 'Cucumber sticks with hummus (150 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Vegetable omelette with toast (350 kcal)',
                'lunch': 'Grilled chicken breast with roasted vegetables (500 kcal)',
                'dinner': 'Salmon with sweet potato (450 kcal)',
                'snack': 'Low-fat yogurt (200 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Scrambled eggs with spinach (400 kcal)',
                'lunch': 'Chicken wrap with vegetables (600 kcal)',
                'dinner': 'Grilled steak with green beans (500 kcal)',
                'snack': 'Protein shake (200 kcal)'
            }
        },
        'muscle gain': {
            'weight <= 60': {
                'breakfast': 'Protein smoothie with banana (500 kcal)',
                'lunch': 'Grilled chicken with rice and broccoli (700 kcal)',
                'dinner': 'Salmon with mashed potatoes (600 kcal)',
                'snack': 'Protein bar (300 kcal)'
            },
            'weight > 60 and weight <= 75': {
                'breakfast': 'Omelette with toast and avocado (600 kcal)',
                'lunch': 'Steak with roasted vegetables (800 kcal)',
                'dinner': 'Chicken curry with rice (700 kcal)',
                'snack': 'Greek yogurt with nuts (350 kcal)'
            },
            'weight > 75': {
                'breakfast': 'Protein pancakes with syrup (700 kcal)',
                'lunch': 'Grilled steak with mashed potatoes (900 kcal)',
                'dinner': 'Roasted chicken with vegetables (800 kcal)',
                'snack': 'Trail mix (400 kcal)'
            }
        }
    }
}


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/FAQs')
def FAQs():
    return render_template('FAQs.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    # Get form data
    diet_preference = request.form.get('diet_preference')
    diet_goal = request.form.get('diet_goal')
    weight = float(request.form.get('weight'))  # Convert weight to float for comparison
    
    # Define weight category
    if weight <= 60:
        weight_category = 'weight <= 60'
    elif 60 < weight <= 75:
        weight_category = 'weight > 60 and weight <= 75'
    else:
        weight_category = 'weight > 75'

    # Retrieve meals based on input
    try:
        meal_plan = meals[diet_preference][diet_goal][weight_category]
    except KeyError:
        # If no matching plan exists
        return render_template('recommendation.html', error='No diet plan found for the selected inputs.')

    # Calculate calories (example logic, replace as needed)
    calories = sum(int(x.split('(')[-1].split()[0]) for x in meal_plan.values())

    # Pass data to the template
    return render_template('recommendation.html', calories=calories, meal_plan=meal_plan)

if __name__ == '__main__':
    app.run(debug=True)