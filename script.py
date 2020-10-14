def ground_shipping(weight):
  if weight <= 2:
    price = weight * 1.50 + 20.00
  elif weight > 2 and weight <= 6:
    price = weight * 3.00 + 20.00
  elif weight > 6 and weight <= 10:
    price = weight * 4.00 + 20.00
  else:
    price = weight * 4.75 + 20.00
  return price
print(ground_shipping(8.4))  

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2:
    price = weight * 4.50
  elif weight > 2 and weight <= 6:
    price = weight * 9.00
  elif weight > 6 and weight <= 10:
    price = weight * 12.00 
  else:
    price = weight * 14.25
  return price
print(drone_shipping(1.5))  



def best_method(weight):
  Ground = ground_shipping(weight)
  Drone = drone_shipping(weight)
  Premium = premium_ground_shipping
  if Ground < Drone and Ground < Premium:
    best = f"Ground shipping is the best method and costs ${Ground}"
  elif Drone < Ground and Drone < Premium:  
    best = f"Drone shipping is the best method and costs ${Drone}"
  else:
    best = f"Premium is the best method and costs ${Premium}"
  return best

print(best_method(4.8)) 
print(best_method(41.5))  






