# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell175.csv")

oneCountryBooleanList = lwd["country_name"]=="Philippines"
oneCountryData = lwd.loc[oneCountryBooleanList]

twoCountryBooleanList = lwd["country_name"]=="Uganda"
twoCountryData = lwd.loc[twoCountryBooleanList]

#setting
print("The Philippines has one of the most dynamic economies in the East Asia and Pacific region with growing urbanization and a larger young population. Education is prioritized, but poorer regions of the nation often lack resources and infrastructure to provide it.\n")
print("Uganda remains one of the poorest countries in the world, combined with problems in agriculture and ecological conservation, making it harder for education to be prioritized nationally.")
input("Press return to continue.\n")

#context
print("Understanding the dynamics of education and gender roles in different societies is key to understanding what we might see in the data.  In Uganda, while education itself might be free, the financial burden of supplies and uniforms disproportionately affects families with multiple children. Notably, cultural norms often prioritize the education of sons over daughters, limiting equal opportunity. On the other hand, in the Philippines, legal safeguards promote fairness and equality in girls' education. Data from the Department of Education highlights this promise, showing higher completion rates for girls at both elementary and secondary education levels compared to boys.")
input("Press return to continue.\n")

#characters
print("Consider two young girls each in an average sized household in, which in both the Philippines and Uganda is between 4 and 5 members. Culture and stereotypes might lead one girl into child marriage or force her to leave her education earlier on to complete her familial duties, which many girls deal with in Uganda. Her brother could likely go on to see higher education that she would never witness. However, a similar aged girl growing up in the Philippines in a family of 4 or 5 would be pushed to learn as much as her siblings did, allowing her to seek higher education, potentially to such an extent that her future has her immigrating to the US or Canada for even more opportunities to learn before she settles down. ")
input("Press return to continue.\n")


#research question
print("After conducting background research, the most pressing question I have is: Why is education for men prioritized over women in countries like Uganda, compared to more equal opportunities in places like the Philippines?")
input("Press return to view a scatterplot of data and a conclusion.\n")


#scatterplot
plt.scatter(x="HD_size_defacto_mean", y="ED_educ_years_mean", data=oneCountryData)
plt.scatter(x="HD_size_defacto_mean", y="ED_educ_years_mean", data=twoCountryData)
plt.title("Household members vs Female years of schooling")
plt.xlabel("Average number of household members")
plt.ylabel("Female average/median years of schooling")
plt.legend(["Philippines", "Uganda"])
plt.ylim(2,12)
plt.xlim(3,6)


#small conclusion 
print("Different social norms lead to different lifestyles for females in Uganda compared to in the Philippines. The access to resources they have are different, and although both countries push for child and female education more than they have in the past, the level to which a girl typically takes her education contrasts in similar sized households. 4 to 5 family members indicates that a young girl grows up with 1 or 2 siblings. Many people believe an educated man will grow up to provide for his family, and that is likely a reason that Ugandan girls complete primary and secondary levels of school before settling down and working at home. In a country like the Philippines, where girls are statistcally proven to complete school at a higher level than boys, more are seen soaring above and beyond. This can become a possibility for anyone, anywhere with adequate support and encouragement to change tradition and help a young girl do whatever she dreams she can do.\n")
print("Thank you for joining me on my data narrative.")

plt.show()
