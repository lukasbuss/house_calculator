import os
import altair as alt
import pandas as pd
from accomodation import House, Apartment
from expense import NonAccomodationExpense

NET_INCOME = 6000

house = House(area=202, price=550000, mortgage=2300, efficiency_class="G")

appartment = Apartment(rent=1200, area=92, nebenkosten_in_rent=200)

non_accomodation_expense = NonAccomodationExpense(net_income=NET_INCOME)

total_monthly_renting = appartment.monthly_total + non_accomodation_expense.total_cost
total_monthly_owning = house.monthly_total + non_accomodation_expense.total_cost

plotting_data = pd.DataFrame({"Lifestyle_Choice": ["Renting", "Owning"],
               "Monthly_Cost": [total_monthly_renting, total_monthly_owning],
               "Monthly_per_m2": [appartment.monthly_cost_per_m2, house.monthly_cost_per_m2]}
               )

# Create the first chart for Monthly Cost
chart1 = alt.Chart(plotting_data).mark_bar(color='blue').encode(
    x='Lifestyle_Choice',
    y='Monthly_Cost'
).properties(
    title='Comparison of Monthly Costs: Renting vs Owning'
)

# Create the second chart for Monthly Cost per m²
chart2 = alt.Chart(plotting_data).mark_bar(color='green').encode(
    x='Lifestyle_Choice',
    y='Monthly_per_m2'
).properties(
    title='Comparison of Monthly Costs per m²: Renting vs Owning'
)

# Combine the charts vertically
combined_chart = alt.hconcat(chart1, chart2)

# Display the combined chart
combined_chart.save('combined_chart.png')