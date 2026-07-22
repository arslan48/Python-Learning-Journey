import matplotlib.pyplot as plt

categories = ['Smartphones', 'Laptops', 'Accessories', 'Smartwatches', 'Audio']
sales_units = [350, 120, 500, 200, 450]
colors=["#dc8a78","#dd7878","#ea76cb","#8839ef","#d20f39"]

plt.pie(
	sales_units,
	labels=categories,
	colors=colors,
	autopct="%1.1f%%",
	shadow=True,	
	explode=[0,0,0.1,0,0]
)

plt.show()