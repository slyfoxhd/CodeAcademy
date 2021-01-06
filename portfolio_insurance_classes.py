import csv

insured_age = []
insured_sex = []
insured_bmi = []
insured_children = []
insured_smoker = []
insured_region = []
insured_charges = []



def load_data(lst, csv_file, col_name):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            lst.append(row[col_name])

    return lst

age = load_data(insured_age, 'insurance.csv', 'age')
sex = load_data(insured_sex, 'insurance.csv', 'sex')
bmi = load_data(insured_bmi, 'insurance.csv', 'bmi')
children = load_data(insured_children, 'insurance.csv', 'children')
smoker = load_data(insured_smoker, 'insurance.csv', 'smoker')
region = load_data(insured_region, 'insurance.csv', 'region')
charges = load_data(insured_charges, 'insurance.csv', 'charges')



class Insurance():

    def __init__(self, sex, smoker, charges, bmi, region):
        self.sex = sex
        self.smoker = smoker
        self.charges = charges
        self.bmi = bmi
        self.region = region

    def percentage_sex(self):
        count = 0
        for x in self.sex:
            if x == 'female':
                count +=1
                female = count
            else:
                x == 'male'
                count += 1
                male = count
        total = female + male
        female_perc = female/total*100
        male_perc = male/total*100

        return female_perc, male_perc

#sex_perc = Insurance(sex, smoker,charges)
#print(sex_perc.percentage_sex())

    def percentage_smoker(self, gender, zigarrette):

        sum = 0
        count = 0

        premium = [z for x,y,z in zip(self.sex, self.smoker, self.charges) if x == gender and y == zigarrette]

        for z in premium:
            count += 1
            float_num = float(z)
            sum += float_num
        avg = sum/count

        return avg, count

    def obese_region(self, gender, area):

        count = 0
        total_bmi = 0
        total_charges = 0

        obese = [(w,x,y,z) for w,x,y,z in zip(self.sex, self.charges, self.bmi, self.region) if w == gender and z == area]

        for y in range(len(obese)):
            total_bmi += float(obese[y][2])
            count += 1
        avg_bmi = total_bmi/count

        for x in range(len(obese)):
            total_charges += float(obese[x][1])
            count += 1
        avg_charg = total_charges/count

        return avg_bmi, avg_charg


obese_perc = Insurance(sex, smoker, charges, bmi, region)
prem_perc = obese_perc



female_obese = obese_perc.obese_region('female', 'northeast')
print('The average bmi of female in the northeast is {:.2f} with an average premium of {:.2f}'.format(female_obese[0], female_obese[1]))
male_obese = obese_perc.obese_region('male', 'northeast')
print('The average bmi of male in the northeast is {:.2f} with an average premium of {:.2f}'.format(male_obese[0], male_obese[1]))
female_obese = obese_perc.obese_region('female', 'northwest')
print('The average bmi of female in the northwest is {:.2f} with an average premium of {:.2f}'.format(female_obese[0], female_obese[1]))
male_obese = obese_perc.obese_region('male', 'northwest')
print('The average bmi of male in the norhtwest is {:.2f} with an average premium of {:.2f}'.format(male_obese[0], male_obese[1]))
female_obese = obese_perc.obese_region('female', 'southeast')
print('The average bmi of female in the southeast is {:.2f} with an average premium of {:.2f}'.format(female_obese[0], female_obese[1]))
male_obese = obese_perc.obese_region('male', 'southeast')
print('The average bmi of male in the southeast is {:.2f} with an average premium of {:.2f}'.format(male_obese[0], male_obese[1]))
female_obese = obese_perc.obese_region('female', 'southwest')
print('The average bmi of female in the southwest is {:.2f} with an average premium of {:.2f}'.format(female_obese[0], female_obese[1]))
male_obese = obese_perc.obese_region('male', 'southwest')
print('The average bmi of male in the southwest is {:.2f} with an average premium of {:.2f}\n'.format(male_obese[0], male_obese[1]))


premium_female_non_smoker = prem_perc.percentage_smoker('female', 'no')
print('The total premium for female non-smokers is {}'.format(premium_female_non_smoker))
premium_female_smoker = prem_perc.percentage_smoker('female', 'yes')
print('The total premium for female smokers is {}'.format(premium_female_smoker))
premium_male_non_smoker = prem_perc.percentage_smoker('male', 'no')
print('The total premium for male non-smokers is {}'.format(premium_male_non_smoker))
premium_male_smoker = prem_perc.percentage_smoker('male', 'yes')
print('The total premium for male smokers is {}'.format(premium_male_smoker))
print('The total premium of females is {}'.format(premium_female_non_smoker+premium_female_smoker))
print('The total premium of males is {}'.format(premium_male_non_smoker+premium_male_smoker))
