import pandas as pd
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb'],
    'bedrooms': [3, 5, 6, 4],
    'area_sqft': [1500, 2500, 3500, 2000],
    'listing_price': [300000, 500000, 600000, 400000]
})

avg_listing_price_per_location = property_data.groupby('location')['listing_price'].mean()

properties_with_more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

largest_property = property_data.loc[property_data['area_sqft'].idxmax()]

print(f"Average listing price per location:\n{avg_listing_price_per_location}\n")
print(f"Number of properties with more than 4 bedrooms: {properties_with_more_than_4_bedrooms}\n")
print(f"Largest property details:\n{largest_property}")
