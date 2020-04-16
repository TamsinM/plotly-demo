import plotly.express as px
import plotly.io as pio

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
# fig.show()

pio.write_html(fig, file='docs/index.html', auto_open=True)