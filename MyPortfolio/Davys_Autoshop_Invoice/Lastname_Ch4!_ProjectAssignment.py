# Part 1: Service pricing
services = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7,
    'car wax': 12
}

# Display available services
print("Davy's Auto Shop Services:")
for service, price in services.items():
    print(f"{service.title()} -- ${price}")

# Initialize cost variables
service1_cost = 0
service2_cost = 0

# Select first service
service1 = input('Select first service (Oil change, Tire rotation, Car wash, Car wax): ').lower()

# Validate first service selection and assign cost
if service1 in services:
    service1_cost = services[service1]
else:
    print('Invalid selection for first service')

# Select second service
service2 = input('Select second service (Oil change, Tire rotation, Car wash, Car wax): ').lower()

# Validate second service selection and assign cost
if service2 in services:
    service2_cost = services[service2]
else:
    print('Invalid selection for second service')

# Calculate total cost
total_cost = service1_cost + service2_cost

# Display invoice
print("\nDavy's Auto Shop Invoice:")
if service1 in services:
    print(f"Service 1: {service1.title()}, ${service1_cost}")
if service2 in services:
    print(f"Service 2: {service2.title()}, ${service2_cost}")
print(f"Total: ${total_cost}")
