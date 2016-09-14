import faker
f = faker.Faker()

inventory_data = '/' + str(f.zipcode()) + '/TBN.' + \
                 str(f.domain_name()).replace('.com','')

print (inventory_data)
print(f.company())