from django.shortcuts import render


def index(request):
  message = "Hello, Blippi!"
  return render(request, 'dealDecider/index.html', {'message': message})

def decideOnDeal(price_per_unit, count_of_pieces, delivery, promotion, selling_price,Period,Defects, Percent):
  overAllSellingPrice = (count_of_pieces - Defects) * selling_price
  overAllRevenue = overAllSellingPrice- ((price_per_unit*count_of_pieces)+delivery+promotion)
  netTotalunitPrice = ((price_per_unit*count_of_pieces)+delivery+promotion)/count_of_pieces
  Revenues = RevenuePerCompaniance(overAllRevenue, Percent)
  decision = f"Over all selling price: {overAllSellingPrice}\nnetTotalunitPrice: {netTotalunitPrice}\noverAll Revenue: {overAllRevenue}\n{Revenues}" 

  return decision

def RevenuePerCompaniance(overAllRevenue, Percent):
  RevenuePerson1 = overAllRevenue * Percent /100
  RevenuePerson2 = overAllRevenue-RevenuePerson1
  return f"Revenue percent: {RevenuePerson1}\nRevenue Person2: {RevenuePerson2}" 
  



def  process_data(request):
  print ("Processing the data")
  if request.method == 'POST':
    # Get the data from the form
    price_per_unit = float(request.POST.get('PricePerUnit'))
    count_of_pieces = float(request.POST.get('CountOfPieces'))
    delivery = float(request.POST.get('delivery'))
    promotion = float(request.POST.get('Promotion'))
    selling_price = float(request.POST.get('SellingPreice'))
    Period = float(request.POST.get('Period'))
    Defects = float(request.POST.get('Defects'))
    Percent = float(request.POST.get('Percent'))

    results = decideOnDeal(price_per_unit, count_of_pieces, delivery, promotion, selling_price,Period,Defects, Percent)

    # Combine the data (modify this based on your specific logic)
    combined_string = f"Price per unit: {price_per_unit}\nCount of pieces: {count_of_pieces}\nDelivery: {delivery}\nPromotion: {promotion}\nSelling price: {selling_price}"
    # Render the template with the combined string 
    return render(request, 'dealDecider/index.html', {'results': combined_string+"\n----------------\n"+results})
  else:
    return render(request, 'dealDecider/index.html')

