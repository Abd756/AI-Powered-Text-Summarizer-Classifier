from classification import train_classifier

texts = [
    "Our new SmartWidget automates daily tasks and improves productivity.",
    "Contact our support team for troubleshooting and repairs.",
    "AsapStudio was founded in 2010 and publishes helpful guides.",
    "The SmartWidget comes in three colors and includes a warranty.",
    "We offer remote and on-site customer service.",
    "Learn more about our company history and mission.",
    "Product features include AI optimization and user customization.",
    "For assistance, reach out via phone, email, or live chat.",
    "Our blog shares tips for getting the most out of our products.",
    "Warranty and product details are available on our website.",
    # Longer and realistic Product Info examples
    "I recently purchased the SmartWidget from your store, and while it worked perfectly for the first few weeks, it suddenly stopped responding to my commands. I tried resetting it, but nothing happened. Could you please let me know if this issue is covered under the warranty, and what steps I should take to get it repaired or replaced?",
    "I'm interested in learning more about the advanced features of your latest SmartWidget model. Specifically, I'm curious about how the AI optimization works and whether it can be customized to fit my daily workflow. Any detailed guides or documentation would be appreciated.",
    "Can you tell me more about the features of your latest product?",
    "What is included in the warranty for SmartWidget and how do I claim it?",
    # Added: Pricing, plans, discounts, subscriptions
    "Can you provide details on the features included in each plan and any available discounts for long-term subscriptions?",
    "I am interested in learning more about your enterprise pricing options. What are the differences between the standard and premium plans?",
    "Do you offer any special rates or discounts for annual subscriptions?",
    "What is the cost breakdown for your monthly and yearly plans, and what features are included in each?",
    "Are there any promotional offers available for new customers signing up for your service?",
    "How do I upgrade my subscription to access more features, and what is the process for changing plans?",
    # Longer and realistic Service Info examples
    "Our company is considering using your products for our office automation needs. Before making a decision, we would like to know more about the on-site repair services you offer, including response times, costs, and the types of issues your technicians can handle.",
    "I've been using your customer support services for a while now, and I wanted to ask about the different ways I can reach out for help. Is live chat available 24/7, and do you offer remote troubleshooting for software issues?",
    "What services do you offer for on-site repairs?",
    "How do I contact customer support for troubleshooting?",
    # Longer and realistic Other examples
    "AsapStudio regularly publishes articles and guides to help users get the most out of our products. Where can I find these resources?",
    "Learn more about our company history and mission.",
    "Where can I find guides to use your products more effectively?",
    # Irrelevant examples
    "The weather in Paris is sunny today, and many people are enjoying outdoor activities in the parks.",
    "Local cafes are serving fresh pastries and coffee to visitors.",
    "The football match last night was exciting and ended in a draw.",
    "Mount Everest is the highest mountain in the world.",
    "The recipe for chocolate cake requires flour, eggs, and cocoa powder.",
    "Last weekend, I visited the mountains and enjoyed hiking with my friends. The weather was perfect, and we saw some beautiful wildlife along the way. Afterward, we stopped at a local restaurant for dinner.",
    "Can you tell me who won the tennis championship last year? I’m trying to settle a bet with my friend, and neither of us can remember the winner.",
    "I'm planning a trip to Italy next summer and would love some recommendations for places to visit, local cuisine to try, and cultural events to attend.",
    "My favorite book is a science fiction novel about space travel and artificial intelligence. The story explores how humans and machines interact in a future society."
]
labels = [
    "Product Info",
    "Service Info",
    "Other",
    "Product Info",
    "Service Info",
    "Other",
    "Product Info",
    "Service Info",
    "Other",
    "Product Info",
    # Longer and realistic Product Info labels
    "Product Info",
    "Product Info",
    "Product Info",
    "Product Info",
    # Added: Pricing, plans, discounts, subscriptions
    "Product Info",
    "Product Info",
    "Product Info",
    "Product Info",
    "Product Info",
    "Product Info",
    # Longer and realistic Service Info labels
    "Service Info",
    "Service Info",
    "Service Info",
    "Service Info",
    # Longer and realistic Other labels
    "Other",
    "Other",
    "Other",
    # Irrelevant labels
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant",
    "Irrelevant"
]

train_classifier(texts, labels)
print("Classifier trained and model saved.")
