# Input meals and receive nutrition information (macro and micronutrients) and target cycle syncing foods
# Add cycle information (last three periods) to estimate dates of each phase of cycle
# List of foods for each phase


menstrual_foods = ['Almonds', 'Avocados', 'Blackberries', 'Blueberries', 'Broccoli', 'Brussels sprouts', 'Cabbage',
                   'Chickpeas', 'Cottage cheese', 'Dark chocolate', 'Dates', 'Eggs', 'Flax seeds', 'Haddock', 'Lentils',
                   'Mackerel', 'Mango', 'Peanut butter', 'Peas', 'Potatoes', 'Pumpkin seeds', 'Red bell peppers',
                   'Rye bread', 'Salmon', 'Scallops', 'Shrimp', 'Spinach', 'Tempeh', 'Tofu', 'Tomatoes', 'Tuna',
                   'Turmeric', 'Whole grains']
follicular_foods = ['Artichokes', 'Avocados', 'Broccoli', 'Brown rice', 'Cabbage', 'Canola oil', 'Carrots',
                    'Chia seeds', 'Chickpeas', 'Eggs', 'Flax seeds', 'Kimchi', 'Lentils', 'Mackerel', 'Mango', 'Oats',
                    'Olive oil', 'Peanut butter', 'Pumpkin seeds', 'Salmon', 'Spinach', 'Strawberries',
                    'Sweet potatoes', 'Tempeh', 'Tofu', 'Yoghurt', 'Zucchini']
ovulation_foods = ['Almonds', 'Avocados', 'Blackberries', 'Blueberries', 'Broccoli', 'Brown rice', 'Cabbage',
                   'Canola oil', 'Chia seeds', 'Coconut', 'Cucumber', 'Eggs', 'Flax seeds', 'Kimchi', 'Lentils', 'Oats',
                   'Olive oil', 'Papaya', 'Pistachios', 'Pumpkin seeds', 'Red bell peppers', 'Salmon', 'Spinach',
                   'Split peas', 'Strawberries', 'Sunflower seeds', 'Sweet potatoes', 'Tahini', 'Tempeh', 'Tofu',
                   'Tomatoes', 'Tuna', 'Turmeric', 'Walnuts']
luteal_foods = ['Apples', 'Artichokes', 'Avocados', 'Bananas', 'Blueberries', 'Broccoli', 'Brown rice',
                'Brussels sprouts', 'Carrots', 'Chia seeds', 'Chickpeas', 'Dark chocolate', 'Dates', 'Eggs',
                'Flax seeds', 'Haddock', 'Lentils', 'Mackerel', 'Oats', 'Olive oil', 'Peaches', 'Peanut butter',
                'Pumpkin', 'Pumpkin seeds', 'Red bell peppers', 'Salmon', 'Scallops', 'Shrimp', 'Spinach', 'Squash',
                'Strawberries', 'Sunflower seeds', 'Sweet potatoes', 'Tahini', 'Tempeh', 'Tofu', 'Tuna', 'Turmeric',
                'Walnuts', 'Whole grains']

# Input start and end dates of last three periods
# import datetime
from datetime import datetime
