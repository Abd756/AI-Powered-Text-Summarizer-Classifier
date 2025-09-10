from classification import train_classifier

texts = [
    "Our new SmartWidget automates daily tasks and improves productivity.",
    "Contact our support team for troubleshooting and repairs.",
    "The SmartWidget comes in three colors and includes a warranty.",
    "We offer remote and on-site customer service.",
    "Product features include AI optimization and user customization.",
    "For assistance, reach out via phone, email, or live chat.",
    "Warranty and product details are available on our website.",
    "I recently purchased the SmartWidget from your store, and while it worked perfectly for the first few weeks, it suddenly stopped responding to my commands. I tried resetting it, but nothing happened. Could you please let me know if this issue is covered under the warranty, and what steps I should take to get it repaired or replaced?",
    "I'm interested in learning more about the advanced features of your latest SmartWidget model. Specifically, I'm curious about how the AI optimization works and whether it can be customized to fit my daily workflow. Any detailed guides or documentation would be appreciated.",
    "Can you tell me more about the features of your latest product?",
    "What is included in the warranty for SmartWidget and how do I claim it?",
    "Can you provide details on the features included in each plan and any available discounts for long-term subscriptions?",
    "I am interested in learning more about your enterprise pricing options. What are the differences between the standard and premium plans?",
    "Do you offer any special rates or discounts for annual subscriptions?",
    "What is the cost breakdown for your monthly and yearly plans, and what features are included in each?",
    "Are there any promotional offers available for new customers signing up for your service?",
    "How do I upgrade my subscription to access more features, and what is the process for changing plans?",
    "Our company is considering using your products for our office automation needs. Before making a decision, we would like to know more about the on-site repair services you offer, including response times, costs, and the types of issues your technicians can handle.",
    "I've been using your customer support services for a while now, and I wanted to ask about the different ways I can reach out for help. Is live chat available 24/7, and do you offer remote troubleshooting for software issues?",
    "What services do you offer for on-site repairs?",
    "How do I contact customer support for troubleshooting?",
    "The weather in Paris is sunny today, and many people are enjoying outdoor activities in the parks.",
    "Local cafes are serving fresh pastries and coffee to visitors.",
    "The football match last night was exciting and ended in a draw.",
    "Mount Everest is the highest mountain in the world.",
    "The recipe for chocolate cake requires flour, eggs, and cocoa powder.",
    "Last weekend, I visited the mountains and enjoyed hiking with my friends. The weather was perfect, and we saw some beautiful wildlife along the way. Afterward, we stopped at a local restaurant for dinner.",
    "Can you tell me who won the tennis championship last year? I’m trying to settle a bet with my friend, and neither of us can remember the winner.",
    "I'm planning a trip to Italy next summer and would love some recommendations for places to visit, local cuisine to try, and cultural events to attend.",
    "My favorite book is a science fiction novel about space travel and artificial intelligence. The story explores how humans and machines interact in a future society.",
    "My name is Abdulah.",
    "Can you tell me a joke?",
    "What is the capital of Australia?",
    "I am just saying hello.",
    "I like pizza.",
    "How do I solve x^2 + 2x + 1 = 0?",
    "What are the health benefits of green tea?",
    "I am planning a family vacation and need advice on travel destinations.",
    "Who won the cricket world cup last year?",
    "I am feeling tired today.",
    "My favorite color is blue.",
    "I am not asking about any product or service.",
    "Can you explain the process for requesting on-site support and what fees might apply for emergency visits?",
    "I had an issue with my order last week, but your support team handled it professionally and offered a quick refund.",
    "How do I request technical support for installation issues?",
    "Is there a way to get remote assistance for software problems?"
    # Product Info
    "The user is asking about the features of the product.",
    "The user wants to know the price of the product.",
    "The user is interested in product warranty details.",
    "The user is requesting information about product colors.",
    "The user is asking about subscription plans and discounts.",
    "The user wants to upgrade their product plan.",
    "The user is inquiring about product availability.",
    "The user likes the features of the product.",
    "The user is asking for product recommendations.",
    "The user wants to know the difference between standard and premium plans.",
    "The user is interested in product specifications.",
    "The user is asking about product compatibility with other devices.",
    "The user wants to know about product updates and new features.",
    "The user is asking about product return policy.",
    "The user is interested in product reviews and ratings.",
    # Service Info
    "The user is asking how to contact customer support.",
    "The user wants to know about on-site repair services.",
    "The user is inquiring about remote assistance for technical issues.",
    "The user is asking about live chat availability for support.",
    "The user wants to know the process for emergency support requests.",
    "The user had an issue with their order and received a quick refund.",
    "The user is asking for help with installation issues.",
    "The user wants to know how to request technical support.",
    "The user is asking about troubleshooting steps for device problems.",
    "The user wants to know about maintenance services for their product.",
    "The user is inquiring about service fees for repairs.",
    "The user is asking about warranty coverage for repairs.",
    "The user wants to know about service response times.",
    "The user is asking about support for software problems.",
    "The user is interested in training sessions for new users.",
    # Irrelevant
    "The user is introducing themselves as Abdulah.",
    "The user is asking for a joke.",
    "The user wants to know the capital of Australia.",
    "The user is just saying hello.",
    "The user likes pizza.",
    "The user is asking how to solve a math equation.",
    "The user wants to know about the health benefits of green tea.",
    "The user is planning a family vacation and needs travel advice.",
    "The user is asking who won the cricket world cup last year.",
    "The user is talking about the weather in Paris.",
    "The user is describing a hiking trip in the mountains.",
    "The user is asking for movie recommendations.",
    "The user is talking about their favorite color.",
    "The user is not asking about any product or service.",
    "The user is sharing a personal story unrelated to products or services."
]
labels = [
    "Product Info",   # 1
    "Service Info",   # 2
    "Product Info",   # 3
    "Service Info",   # 4
    "Product Info",   # 5
    "Service Info",   # 6
    "Product Info",   # 7
    "Product Info",   # 8
    "Product Info",   # 9
    "Product Info",   #10
    "Product Info",   #11
    "Product Info",   #12
    "Product Info",   #13
    "Product Info",   #14
    "Product Info",   #15
    "Product Info",   #16
    "Product Info",   #17
    "Service Info",   #18
    "Service Info",   #19
    "Service Info",   #20
    "Service Info",   #21
    "Irrelevant",     #22
    "Irrelevant",     #23
    "Irrelevant",     #24
    "Irrelevant",     #25
    "Irrelevant",     #26
    "Irrelevant",     #27
    "Irrelevant",     #28
    "Irrelevant",     #29
    "Irrelevant",     #30
    "Irrelevant",     #31
    "Irrelevant",     #32
    "Irrelevant",     #33
    "Irrelevant",     #34
    "Irrelevant",     #35
    "Irrelevant",     #36
    "Irrelevant",     #37
    "Irrelevant",     #38
    "Irrelevant",     #39
    "Irrelevant",     #40
    "Irrelevant",     #41
    "Irrelevant",     #42  <-- was 'Service Info' in your list; made 'Irrelevant'
    "Service Info",   #43
    "Service Info",   #44
    "Service Info",   #45
    "Service Info"    #46  <-- NEW: for "Is there a way to get remote assistance...?"

    # Product Info (15)
    "Product Info", "Product Info", "Product Info", "Product Info", "Product Info",
    "Product Info", "Product Info", "Product Info", "Product Info", "Product Info",
    "Product Info", "Product Info", "Product Info", "Product Info", "Product Info",
    # Service Info (15)
    "Service Info", "Service Info", "Service Info", "Service Info", "Service Info",
    "Service Info", "Service Info", "Service Info", "Service Info", "Service Info",
    "Service Info", "Service Info", "Service Info", "Service Info", "Service Info",
    # Irrelevant (15)
    "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant",
    "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant",
    "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant", "Irrelevant"
]



train_classifier(texts, labels)
print("Classifier trained and model saved.")
