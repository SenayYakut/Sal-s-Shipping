# First off, we need to know how much it costs to ship a package of given weight by normal ground shipping.

def ground_shipping(weight):
 if weight <= 2:
   cost = weight * 1.50 + 20.0
   return cost
 elif weight > 2 and weight <= 6:
   cost = weight * 3.00 + 20.0
   return cost
 elif weight > 6 and weight <= 10:
   cost = weight * 4.00 + 20.0
   return cost
 else:
   cost = weight * 4.75 + 20.0
   return cost     

print(ground_shipping(8.4))  

premium_ground_shipping = 125.00

def drone_shipping(weight):
 if weight <= 2:
   cost = weight * 4.50
   return cost
 elif weight > 2 and weight <= 6:
   cost = weight * 9.00
   return cost
 elif weight > 6 and weight <= 10:
   cost = weight * 12.00
   return cost
 else:
   cost = weight * 14.25
   return cost     

print(drone_shipping(1.5))


def cheapest_method(weight):
  drone = drone_shipping(weight)
  ground = ground_shipping(weight)
  premium_ground_shipping = 125.00
  if drone < ground and drone < premium_ground_shipping:
    return "Drone Shipping: " + str(drone)
  elif ground < drone and ground < premium_ground_shipping:
    return "Ground Shipping: " + str(ground)
  elif  premium_ground_shipping < drone and  premium_ground_shipping < ground:
    return "Premium_ground_shipping:" + str(premium_ground_shipping)
 
    
print(cheapest_method(17))
        
print(cheapest_method(4.8))

print(cheapest_method(41.5))


